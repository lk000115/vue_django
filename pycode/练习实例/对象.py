class  Master():
    def __init__(self):
        self.kongfu = "我是父类master的属性"
        self.__money = 2000

    def __str__(self):
        return '这是一台洗衣机'

    def maker_cake(self):
        print(f'运用{self.kongfu}技术')

class Prentice(Master):
    pass

xia = Prentice()

print(xia.maker_cake())
