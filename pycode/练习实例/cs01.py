print("fffff")
print("fffff")

# 反射 --函数

class F():
    def get(self):
        print("get---函数")

obj = F()
obj = getattr(obj,"get","NO")   # 获取对象obj中的get函数

obj()














