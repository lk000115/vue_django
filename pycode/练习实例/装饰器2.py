# 应用装饰器定义类方法
class Student(object):

    @property  # 装饰器
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()

s.score = 99
# print(s.score)

def outer(fn):
    def inner(*args,**kew):
        print("增加的功能1")
        fn(*args,**kew)
        print("增加的功能2")
    return inner

@outer
def fnn1(a):
    print(f"我是被装饰的函数---{a}")

@outer
def fnn2(a,b,x=3):
    print(f"我是被装饰的函数--{a}---{b}---{x}")

fnn1(1)
fnn2(2,3)

