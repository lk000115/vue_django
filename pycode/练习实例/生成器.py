# 列表修改成字典,索引为key,值为value
list = ["周星星","历山","赵六"]
d = {i:list[i] for i in range(len(list))}
print(d)

