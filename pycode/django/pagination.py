"""
分页功能封装:
  参数如下:
           requery    请求
          queryset   从数据库获取的需要分页的原始数据
         page_size   每页需要显示的数据条数,此参数不传默认是10
              plus   分页按钮中当前页前后显示的按钮数,默认是5
        page_param   get请求的参数名称,默认是page

     属性:  page_queryset:   pagination.page_queryset  每页显示的数据

     方法:  html           pagination.html()          传给i请前端的分页按钮html字符串代码
   调用案例:
       page_object = Pagination(request,queryset)
       page_queryset = page_object.page_queryset
       page_str = page_object.html()
       context = {
        'queryset': page_queryset,
        "page_str": page_str,
        "search_data": search_data,
       }
       return render(request, 'pretty_list.html', context)
   前端网页:
       {% for obj in queryset %}
            {{obj.xxx}}
        {% endfor %}

        <ul class="pagination">
            {{ page_str }}
        </ul>

"""

from django.utils.safestring import mark_safe


class Pagination(object):
    def __init__(self,request,queryset,page_size=10,page_param="page",plus=5):
        page = request.GET.get(page_param,"1")
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        self.page_size = page_size
        self.start = (page - 1) * self.page_size
        self.end = page * self.page_size
        self.page_queryset = queryset[self.start:self.end]
        self.plus = plus
        total_count = queryset.count()
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count

    def html(self):
        if self.total_page_count <= 2 * self.plus + 1:
            start_page = 1
            end_page = self.total_page_count
        else:
            # 当前页< 5
            if self.page <= self.plus:
                start_page = 1
                end_page = self.page + self.plus + 1
            else:
                # 当前页 > 5
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus + 1

        page_str_list = []

        page_str_list.append('<li ><a class="page-link" href="?page={}">首页</a></li>'.format(1))
        # 上一页
        if self.page > 1:
            prev = '<li ><a class="page-link" href="?page={}">上一页</a></li>'.format(self.page - 1)
        else:
            prev = '<li ><a class="page-link" href="?page={}">上一页</a></li>'.format(1)
        page_str_list.append(prev)
        for i in range(start_page, end_page):
            if i == self.page:
                ele = '<li class="page-item active"><a class="page-link" href="?page={}">{}</a></li>'.format(i, i)
            else:
                ele = '<li ><a class="page-link" href="?page={}">{}</a></li>'.format(i, i)
            page_str_list.append(ele)

        # 下一页
        if self.page < self.total_page_count:
            prev = '<li ><a class="page-link" href="?page={}">下一页</a></li>'.format(self.page + 1)
        else:
            prev = '<li ><a class="page-link" href="?page={}">下一页</a></li>'.format(self.total_page_count)
        page_str_list.append(prev)

        page_str_list.append('<li ><a class="page-link" href="?page={}">尾页</a></li>'.format(self.total_page_count))
        # 必须把字符串转为安全的数据才能传给前端生成HTML
        page_str = mark_safe(''.join(page_str_list))
        return page_str
