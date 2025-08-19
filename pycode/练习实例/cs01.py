
# 反射 --函数

# class F():
#     def get(self):
#         print("get---函数")

# obj = F()
# obj = getattr(obj,"get","NO")   # 获取对象obj中的get函数
# obj()

# 可以使用type定义类
# 类名 = type("类名",(父类,),{成员1,成员2})

# 以下函数就是把类的方法score变成一个变量或者说是属性,及调用时不需要()
# class Student(object):

#     @property  # 装饰器
#     def score(self):
#         return self._score


#     @score.setter
#     def score(self, value):
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value

# s = Student()
# s.score = 99    # 调用setter方法
# print(s.score)  # 调用getter方法

# 列表推导式或者生成式
lt = [i*2 for i in range(1,11)]  # 列表推导式
# print(lt)

st = lt.__iter__()  # 获取迭代器

while True:
    try:
        print(st.__next__())
    except StopIteration:
        break






