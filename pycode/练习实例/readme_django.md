# 知识点 Django

- 格式化快捷键Ctrl + Alt + L
- os.path.join(BASE_DIR,template)
- 静态app中建static文件夹
  ![img.png](img.png)

  配置文件setting中

  ![image-20240326115140200](C:\Users\cssd\AppData\Roaming\Typora\typora-user-images\image-20240326115140200.png)

## 1.1 命令行创建python虚拟环境

1 执行 python -m venv venv01  创建 venv01的虚拟环境

2 执行venv01\scripts\activate  激活虚拟环境
3 虚拟环境提示符下(venv01)执行  pip list 查看安装的应用
4 虚拟环境提示符下(venv01)执行 pip install django 安装应用
5 在虚拟环境提示符下(venv01)执行 deactivate 退出虚拟环境

6 django-admin startproject mysite  新建项目

7 python manage.py startapp polls  新建app

8 python manage.py runserver  启动django项目   python manage.py runserver  192.168.1.168:8080  指定ip和端口

9  pip freeze > requirements.txt   把项目虚拟环境安装的所有应用清单名存到文件中  

10 python manage.py collectstatic  根目录下执行此命令,会把静态文件汇总归集到一个目录

```
uwsgi.ini 配置文件和settings.py处于同一目录

[uwsgi]
http=127.0.0.1:8000    #如果用nginx反向代理 http改为 socket
chdr=D:\code\py\pycode\drf_xm
wsgi-file = drf_xm\wsgi.py
process=4
threads=2
pidfile=uwsgi.pid
daemonize=uwsgi.log
master=True
########
启动uwsgi
cd 到 uWSUI配置文件所在目录
uwsgi --ini uwsgi.ini

停止uwsgi
uwsgi --stop uwsgi.pid
**
nginx 配置文件
location / {
    uwsgi_pass 127.0.0.1:8000;
    include  /路径/uwsgi_params;

}


```

### 1.1.1  nginx+waitress配置

```
以下是nginx+waitress配置
启动nginx命令  start nginx
             nginx -s reload  重新加载  
nginx 为了反向代理waitress，做如下配置

charset utf-8;    # 设置显示中文字符
server {
        listen       80;
        server_name  localhost;

        location / {
                    proxy_set_header Host $host;
                    proxy_pass http://127.0.0.1:8001;
                }
        location /static {
                    alias D:\code\py\pycode\drf_xm\static;      
                }
        
        #error_page  404              /404.html;
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }        

server {
        listen       88;
        server_name  localhost;

        location / {
            root   html;          # 网站根目录,默认显示nginx下html目录的index.html
            index  index.html index.htm;
        }

        #error_page  404              /404.html;

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
        
Nginx的location匹配规则如下：
   精确匹配 =
   前缀匹配 ^~ /bk   
   正则    ~* \.(gif|jpg|jpeg) {}
   匹配所有 /
   vue工程匹配  
   location / {
      root  /www;
      try_files  $uri  $uri/  $uri/index.html  $uri.html  /index.html;
   }
   
   
waitress配置
在项目根目录创建run.py
from waitress import serve
from drf_xm.wsgi import application
if __name__ == "__main__":
    serve(application, host='127.0.0.1', port=8001, threads=4)


settings.py

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')

根urls
urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),  # 获取自动生成的token的接口
    path('admin/', admin.site.urls),
    path('app/', include('app.urls'))

] + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
```







## 1.2 模板语法

- 安装Django    pip install django
- 安装 pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  djangorestframework
- 创建Django项目 django-admin startproject  mysite
- 创建APP    python manage.py startapp student
- 创建迁移文件 python manage.py makemigrations student
- 执行迁移文件 python manage.py migrate
- 创建后台登陆的超级用户  python manage.py createsuperuser
- pycharm 中可以点击菜单工具--运行manage.py任务,直接调用django命令: 可以输入startapp app01 来创建应用
- ```
  ex = models.PrettyNum.objects.filter(moblie='138666').exists()
  如果数据库中存在138666的记录,这返回true否则false
  
  排除自己,如果数据库还存在有相同的数据
  ex = models.PrettyNum.objects.exclude(self.instance.pk).filter(moblie='138666').exists()
  
  把数据库注册到django后台,并可以用django自带的后台管理功能来管理
  @admin.register(Course)
  class CourseAdmin(admin.ModelAdmin):
      # 设置在django后台数据库展示的字段
      list_display= ('name','introduction','teacher','price')
      search_fields = list_display
      list_filter = list_display
  
  ```

## 1.3 命名空间

```
在url路由文件中加一句 app_name = 'polls' 给app命名
随后在html文件中可以引用 
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
即跳转到polls中的name=detail的路由
```

## 1.4 数据库操作

- 基本操作

```
# 增
    #
    # models.Tb1.objects.create(c1='xx', c2='oo')  增加一条数据，可以接受字典类型数据 **kwargs
      obj={"c1":"xx","c2":'oo'}
      models.Tb1.objects.create(**obj)  用字典参数
  
    # obj = models.Tb1(c1='xx', c2='oo')
    # obj.save()

    # 查
    #
    # models.Tb1.objects.get(id=123)         # 获取单条数据，不存在则报错（不建议）
    # models.Tb1.objects.all()               # 获取全部
    # models.Tb1.objects.filter(name='seven') # 获取指定条件的数据

    # 删
    #
    # models.Tb1.objects.filter(name='seven').delete() # 删除指定条件的数据

    # 改
    # models.Tb1.objects.filter(name='seven').update(gender='0')  # 将指定条件的数据更新，均支持 **kwargs
    # obj = models.Tb1.objects.get(id=1)
    # obj.c1 = '111'
    # obj.save()                                                 # 修改单条数据

基本操作
```

- 进阶操作（了不起的双下划线）  利用双下划线将字段和对应的操作连接起来

```
# 获取个数
        #
        # models.Tb1.objects.filter(name='seven').count()

        # 大于，小于
        # models.PrettyNum.objects.all()[0:10]           #获取数据库1到10条数据,包含后不包含前 
        # models.Tb1.objects.filter(id__gt=1)              # 获取id大于1的值
        # models.Tb1.objects.filter(id__gte=1)              # 获取id大于等于1的值
        # models.Tb1.objects.filter(id__lt=10)             # 获取id小于10的值
        # models.Tb1.objects.filter(id__lte=10)             # 获取id小于10的值
        # models.Tb1.objects.filter(id__lt=10, id__gt=1)   # 获取id大于1 且 小于10的值

        # in
        #
        # models.Tb1.objects.filter(id__in=[11, 22, 33])   # 获取id等于11、22、33的数据
        # models.Tb1.objects.exclude(id__in=[11, 22, 33])  # not in

        # isnull
        # Entry.objects.filter(pub_date__isnull=True)

        # contains
        #
        # models.Tb1.objects.filter(name__contains="ven")
        # models.Tb1.objects.filter(name__icontains="ven") # icontains大小写不敏感
        # models.Tb1.objects.exclude(name__icontains="ven")

        # range
        #
        # models.Tb1.objects.filter(id__range=[1, 2])   # 范围bettwen and

        # 其他类似
        #
        # startswith--开始，istartswith, endswith, iendswith, contains--包含

        # order by
        #
        # models.Tb1.objects.filter(name='seven').order_by('id')    # asc
        # models.Tb1.objects.filter(name='seven').order_by('-id')   # desc

        # group by
        #
        # from django.db.models import Count, Min, Max, Sum
        # models.Tb1.objects.filter(c1=1).values('id').annotate(c=Count('num'))
        # SELECT "app01_tb1"."id", COUNT("app01_tb1"."num") AS "c" FROM "app01_tb1" WHERE "app01_tb1"."c1" = 1 GROUP BY "app01_tb1"."id"

        # limit 、offset
        #
        # models.Tb1.objects.all()[10:20]  获取10到20之间的数据

        # regex正则匹配，iregex 不区分大小写
        #
        # Entry.objects.get(title__regex=r'^(An?|The) +')
        # Entry.objects.get(title__iregex=r'^(an?|the) +')

        # date
        #
        # Entry.objects.filter(pub_date__date=datetime.date(2005, 1, 1))
        # Entry.objects.filter(pub_date__date__gt=datetime.date(2005, 1, 1))

        # year
        #
        # Entry.objects.filter(pub_date__year=2005)
        # Entry.objects.filter(pub_date__year__gte=2005)

        # month
        #
        # Entry.objects.filter(pub_date__month=12)
        # Entry.objects.filter(pub_date__month__gte=6)

        # day
        #
        # Entry.objects.filter(pub_date__day=3)
        # Entry.objects.filter(pub_date__day__gte=3)

        # week_day
        #
        # Entry.objects.filter(pub_date__week_day=2)
        # Entry.objects.filter(pub_date__week_day__gte=2)

        # hour
        #
        # Event.objects.filter(timestamp__hour=23)
        # Event.objects.filter(time__hour=5)
        # Event.objects.filter(timestamp__hour__gte=12)

        # minute
        #
        # Event.objects.filter(timestamp__minute=29)
        # Event.objects.filter(time__minute=46)
        # Event.objects.filter(timestamp__minute__gte=29)

        # second
        #
        # Event.objects.filter(timestamp__second=31)
        # Event.objects.filter(time__second=2)
        # Event.objects.filter(timestamp__second__gte=31)

进阶操作
```

- 其他操作

```
# extra
    #
    # extra(self, select=None, where=None, params=None, tables=None, order_by=None, select_params=None)
    #    Entry.objects.extra(select={'new_id': "select col from sometable where othercol > %s"}, select_params=(1,))
    #    Entry.objects.extra(where=['headline=%s'], params=['Lennon'])
    #    Entry.objects.extra(where=["foo='a' OR bar = 'a'", "baz = 'a'"])
    #    Entry.objects.extra(select={'new_id': "select id from tb where id > %s"}, select_params=(1,), order_by=['-nid'])

    # F
    #
    # from django.db.models import F
    # models.Tb1.objects.update(num=F('num')+1)


    # Q
    #
    # 方式一：
    # Q(nid__gt=10)
    # Q(nid=8) | Q(nid__gt=10)
    # Q(Q(nid=8) | Q(nid__gt=10)) & Q(caption='root')
    # 方式二：
    # con = Q()
    # q1 = Q()
    # q1.connector = 'OR'
    # q1.children.append(('id', 1))
    # q1.children.append(('id', 10))
    # q1.children.append(('id', 9))
    # q2 = Q()
    # q2.connector = 'OR'
    # q2.children.append(('c1', 1))
    # q2.children.append(('c1', 10))
    # q2.children.append(('c1', 9))
    # con.add(q1, 'AND')
    # con.add(q2, 'AND')
    #
    # models.Tb1.objects.filter(con)


    # 执行原生SQL
    #
    # from django.db import connection, connections
    # cursor = connection.cursor()  # cursor = connections['default'].cursor()
    # cursor.execute("""SELECT * from auth_user where id = %s""", [1])
    # row = cursor.fetchone()

其他操作
```

## 1.5 分页算法

```
    # 根据用户的页码计算页码起止位置
    """靓号列表"""
def pretty_list(request):
    # for i in range(100):
    #     t = 13559900020
    #     t = t + i
    #     t = str(t)
    #     models.PrettyNum.objects.create(mobile=t,price=1000,level=1,status=2)
        # print(type(t))
    data_dict = {}
    search_data = request.GET.get('q',"")
    if search_data is not None:
        data_dict["mobile__contains"] = search_data
    # 根据用户的页码计算页码起止位置
    page = int(request.GET.get('page',1))
    page_size = 10
    start = (page - 1) * page_size
    end = start + page_size
    queryset = models.PrettyNum.objects.filter(**data_dict).order_by("-level")[start:end]
    # 页码总条数
    total_count = models.PrettyNum.objects.filter(**data_dict).count()
    # 计算总页码
    total_page_count,div = divmod(total_count,page_size)
    if div:
        total_page_count += 1

    # 显示当前页的前5页,后5页
    plus = 5
    if total_page_count <= 2*plus +1 :
        start_page = 1
        end_page = total_page_count
    else:
        # 当前页< 5
        if page <= plus:
            start_page = 1
            end_page = page + plus +1
        else:
            # 当前页 > 5
            if (page + plus) > total_page_count:
                start_page = total_page_count - 2*plus
                end_page = total_page_count
            else:
                start_page = page - plus
                end_page = page + plus +1

    page_str_list = []
    # 上一页
    if page > 1:
        prev = '<li ><a class="page-link" href="?page={}">上一页</a></li>'.format(page-1)
    else:
        prev = '<li ><a class="page-link" href="?page={}">上一页</a></li>'.format(1)
    page_str_list.append(prev)
    for i in range(start_page,end_page):
        if i == page:
            ele = '<li class="page-item active"><a class="page-link" href="?page={}">{}</a></li>'.format(i,i)
        else:
            ele = '<li ><a class="page-link" href="?page={}">{}</a></li>'.format(i,i)
        page_str_list.append(ele)

    # 下一页
    if page < total_page_count:
        prev = '<li ><a class="page-link" href="?page={}">下一页</a></li>'.format(page + 1)
    else:
        prev = '<li ><a class="page-link" href="?page={}">下一页</a></li>'.format(total_page_count)
    page_str_list.append(prev)

    # 必须把字符串转为安全的数据才能传给前端生成HTML
    page_str = mark_safe(''.join(page_str_list))
    content = {
        'queryset': queryset,
        "search_data": search_data,
        "page_str": page_str
    }
    return render(request, 'pretty_list.html', content)
  



保留原有搜索条件
import copy

query_dict =  copy.deepcopy(request.GET)
query_dict._mutable = true
self.query_dict = query_dict
self.page_param = page_param

self.query_dict.setlist(self.page_param,[1])

page_str_list.append('<li ><a class="page-link" href="?{}">首页</a></li>'.format(self.query_dict.urlencoder()))


```

## 1.6 django案例代码

```
1 views中代码

class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserModelForm, self).__init__(*args, **kwargs)
        # 给自动生成的表单增加样式form-control
        for name,field in self.fields.items():
            if field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {
                    'class':'form-control',
                'placeholder':field.label
                }
              
              
              
2  中间件
# 中间件
from django.shortcuts import render, redirect
from django.utils.deprecation import MiddlewareMixin

class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 排除不需要登陆就能访问的页面
        if request.path_info =='/login/':
            return
        # print('M登陆了')
        info_dict = request.session.get('info')
        if info_dict:
            return
        return redirect('/login/')

    def process_response(self, request, response):
        # print('M1退出了')
        return response
      
 setting中加上
 MIDDLEWARE = [
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app01.middleware.auth.AuthMiddleware',
]

views中加上
def logout(request):
    """注销"""
    request.session.clear()
    return redirect('/login/')

```

## 2.0 django-drf 应用

```
1 前后端开发分离，前端发请求，后端只返回JSON字符串，前端收到后负责页面渲染
2 DRF中后端通过请求类型来区分功能，get查询 post 新增  put修改  delete删除
3 django中view类也具有CBV功能，
4 DRF中APIview继承自view,
5 pip install djangorestframework  安装 DRF

drf配置:  settings.py
INSTALLED_APPS = [
    'app.apps.AppConfig',
    'rest_framework.authtoken'  # drf自带认证
    'rest_framework'
]
REST_FRAMEWORK = {
 "UNAUTHENTICATED_USER":None
}
根路由加上：
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

# DRF全局配置
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS_CLASSES': ',rest_framework.pagination.pagination',
    'PAGE_SIZE':50,
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ],
    'DEFAULT_PARSER_CLASSES':[     #解析request.data
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BaseAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    ]
}



模型:
class Course(models.Model):
    name = models.CharField(max_length=255,unique=True ,verbose_name="课程名称",help_text="课程名称")
    introduction = models.TextField(verbose_name="介绍",help_text="课程介绍")
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="讲师",on_delete=models.CASCADE,help_text="课程讲师")
    price = models.DecimalField(verbose_name="价格",max_digits=6, decimal_places=2, default=0,help_text="课程价格")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = '课程名称'
        verbose_name_plural = '课程名称'
        ordering = ('price',)

    def __str__(self):
        return self.name
      
路由:
from django.contrib import admin
from django.urls import path,re_path,include
from app.views import LoginView,LoginDetailView

主
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls'))
]
# 子路由:
from django.urls import path
from app import views

urlpatterns = [
    path('fbv/list/',views.course_list,name='course_list'),
    path('fbv/detail/<int:pk>/',views.course_detail,name='course_detail')
]

# 序列化器:  app下建文件 serializers.py
from rest_framework import serializers
from .models import Course
#导入系统自带的管理用户表
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # 应用django内置的用户库
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    #设置显示讲师的名称,.关联外键的数据库表的名称
    teacher = serializers.ReadOnlyField(source='teacher.username')
    class Meta:
        model = Course
        fields = ('id','name', 'teacher','introduction','price')


views 视图

```

- view 视图  一 drf 函数式编程  Function Based View

```
from rest_framework.decorators import api_view
from .serializers import CourseSerializer
@api_view(['POST','GET'])
def course_list(request):
    if request.method == 'GET':
        s = CourseSerializer(instance=Course.objects.all(), many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # partial = True  表示部分更新.即前端只传过来了部分字段的值
        s = CourseSerializer(data=request.data,partial=True)
        # 对前端传过来的数据进行校验
        if s.is_valid():
            s.save(teacher=request.user)   # 设置teacher字段等于当前登陆的用户
            return Response(data=s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def course_detail(request,pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(data={'message':'没有此课程信息'}, status=status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'GET':
            s = CourseSerializer(instance=course, many=False)
            return Response(s.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            s = CourseSerializer(instance=course, data=request.data,partial=True)
            if s.is_valid():
                s.save()
                return Response(s.data, status=status.HTTP_200_OK)
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
```

- 二 类视图
- rest_framework全局配置

```
在 setting.py中配置认证
REST_FRAMEWORK={
    "UNAUTHENTICATED" : None,
    "值": ["认证组件路径"]
}

class CourseList(APIView):
    def get(self, request):
        queryset = Course.objects.all()
        s = CourseSerializer(instance=queryset, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request):
        s = CourseSerializer(data=request.data)
        if s.is_valid():
            s.save(teacher=self.request.user)
            return Response(data=s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(APIView):

    @staticmethod  # 注明是静态方法
    def get_object(pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return

    def get(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response(data={'message': '没有此课程信息'}, status=status.HTTP_404_NOT_FOUND)
        s = CourseSerializer(instance=obj)
        return Response(s.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response(data={'message': '没有此课程信息'}, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response(data={'message': '没有此课程信息'}, status=status.HTTP_404_NOT_FOUND)
        s = CourseSerializer(instance=obj, data=request.data)
        if s.is_valid():
            s.save()
            return Response(data=s.data, status=status.HTTP_200_OK)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


```

- 通用类视图 Generic Class Base View

```
class GCourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class GCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
```

- DRF 视图集 viewset

```
路由：
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix='viewsets', viewset=views.CourseViewSet)
urlpatterns = [
	path('', include(router.urls))  ]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)
      
      
```

### 2.1  序列化

```
 序列化和反序列化
 1 序列化
   get请求中.把数据库查询到的queryset对象,传给序列化器的Instance变量,在调用序列化器的data方法时,序列化器内部再把
   queryset对象转为json对象,返回给前端
 2 反序列化
   请求体request.data的数据传给序列化器的data变量,在调用序列化器的save方法时,把请求体的data数据保存到数据库
   再调用序列化器的data方法.把数据库库保存的数据转为JSON数据传给instance,返回给前端

```





## 3.0 DRF token 认证

```
from rest_framework.authtoken import views

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),   #获取token的接口
    ]
  
 
# 在views中编写函数,当用户创建时自动生成token 
# 信号机制自动生成token
@receiver(post_save, sender=User)
def generate_token(sender, instance=None, created=False, **kwargs):
    """创建用户时自动生成token"""
    if created:
        Token.objects.create(user=instance)  
```

## 4.0  虚拟环境迁移

```
1 修改`pyvenv.cfg`文件里的`home`和`version`
   venv目录下的配置文件pyvenv.cfg
   home = C:\Python\Python38 改为当前电脑的地址
   
2 Scripts\activate`以及`Scripts\activate.bat两个文件中的
VIRTUAL_ENV=F:\study\code\student_xm\drf_xm\venv
改为当前电脑的地址

3 如果还报错,把venv\Lib\site-packages\下的pip的两个相关文件夹直接删除
再激活虚拟环境,重新安装pip:
python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple  
如果报错,执行:
python -m ensurepip
easy_install pip
后再重新执行一次pip安装

迁移方法2: 
  导出当前环境中的包  
    pip freeze > requirements.txt
  在目标机器上创建新环境并安装包
    pip install -r requirements.txt


4 跨域
1 安装依赖 pip install django-cors-headers
2 setting.py中
 记得修改允许访问的IP
ALLOWED_HOSTS = ['*'] # 允许全部IP访问项目
# setting.py 修改以下内容
INSTALLED_APPS = [
    'corsheaders', # 注册app corsheaders
    'app01',# 你的app
]
3 添加中间件 
MIDDLEWARE = [
     'corsheaders.middleware.CorsMiddleware',
]

4 # 在 setting.py 末尾添加以下设置
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True
# 允许跨域访问的白名单
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8081',
)

CORS_ALLOW_HEADERS = ('*')

国际化- LANGUAGE_CODE = 'zh-hans'        # 'en-us' 英语
       TIME_ZONE = 'Asia/Shanghai'


```

##  5.0 元类

```
创建类的方式2
Foo = type('Foo',(object),{"v1":123,"func":lambda self:999})


class  Foo(object,metaclass=type):  默认由type创建  
	def __init__(self);
		pass    # 2 初始化类数据
		
    def __new__(self):
    	paa  # 1 创建类,先于__init__方法执行
    	
    	
class  MyType(type)
	def __new__(cls,name,base,attrs)
	# 此处可以增加代码在类创建前进行修改类属性
	Foo = super().__new__(cls,name,base,attrs)
	return Foo
```





