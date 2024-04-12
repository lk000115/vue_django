def outer(logo):

    # 内部函数访问外部函数变量
    def inner(msg):
        print(f"外部参数: {logo}---内部参数: {msg}")

    return inner

fn =  outer("传入的外部参数")
# fn("aa")

def outer2(num1=0):

    def inner(num2):
        # 加上关键字nonlocal后，内部函数就可以改变外部函数变量的值
        nonlocal  num1
        num1 += num2
        print(f"计算结果 = {num1}")

    return inner

fn2 = outer2()

fn2(2)
fn2(6)