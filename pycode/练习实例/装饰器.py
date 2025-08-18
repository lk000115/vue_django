# 装饰器也是闭包的一种

# 标准写法
def outer(func):
    def inner():
        print("增加的功能1")
        func()
        print("增加的功能2")
    return inner

def sleep():
    import random
    import time
    print("睡眠中。。。。。")
    time.sleep(random.randint(1,5))

fn = outer(sleep)
fn()


# 语法糖写法

def outer2(func):
    def inner():
        print("增加的功能代码1")
        func()
        print("增加的功能代码2")
    return inner

@outer2
def sleep2():
    import random
    import time
    print("睡眠中 2。。。。。")
    time.sleep(random.randint(1,5))

sleep2()


# 通用装饰器
def wrapper(fn):
    def inner(*args,**kwargs):
        print("增加的功能代码1")
        ret =  fn(*args,**kwargs)
        print("增加的功能代码2")
        return ret
    return inner

@wrapper
def fn(a,b):
    print(a+b)
    return "haha"

res  = fn(1, 2)  # 输出增加的功能代码1, 3, 增加的功能代码2

print(res)  # 输出 3


