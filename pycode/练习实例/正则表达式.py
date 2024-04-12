import re
str = "我的电话号码是10086,另外一个10050"
# print(re.match(r'^\d{3}', '010 12345'))
s = ''' 
   <div class="asddsd" id="1">您好</div>
   <div class="asd" id="2">我好</div>
   <div class="asdd" id="3">大家好</div>
   '''
s1 = "      带空格字符串"

# 正则(?P<id>.*)表示分组.把.*匹配的字符放入分组变量id中
lst = re.finditer(r'<div class=".*?" id="(?P<id>.*?)">(?P<st>.*?)</div>' , s)
for it in lst:
    # print(it.group("id"),it.group("st"))
    dt = it.groupdict()
    print(dt)

#  .*?F非贪婪的匹配字符F前的任意字符
lst2 = re.findall(r".*?F", "ggFggSDFg")
print(lst2)

# strip()函数去除空格
print(s1.strip())

# 预加载正则,re.S表示匹配
obj = re.compile(r"\d+",re.S)
res = obj.finditer(str)
# for i in res:
#     print(i.group())





