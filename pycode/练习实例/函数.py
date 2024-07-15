# 位置参数
def fn1(x,y):
    print(f"位置参数---{x}----{y}")
fn1(2,3)

# 默认参数n
def fn2(x,n=2):
    print(f"默认参数: n = {n}")
fn2(3)

# 可变参数
def fn3(*args):
    print(f"可变参数是一个元祖:  =  {args}")
x = (6,7,8)    
fn3(1,2,3)
fn3(*x)
# 关键字参数
def fn4(name, age, **kw):
    print("以下是关键字参数-----")
    print(f"'name:', {name}, 'age:', {age}, 'other:',关键字参数 = {kw} " )
    print(type(kw))
x={"a":2, "b":8}
# 调用方式1
fn4("调用方式1--- ",18,**x)
# 调用方式2
fn4("调用方式2--- ",18,a=22,b=88)