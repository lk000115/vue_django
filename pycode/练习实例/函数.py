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
fn3(1,2,3)

# 关键字参数
def fn4(name, age, **kw):
    print(f"'name:', {name}, 'age:', {age}, 'other:',关键字参数 = {kw} " )

fn4("zhansan",18,a=2,b=4)