# 列表修改成字典,把索引为key,值为value
l = ["周星星","历山","赵六"]
d = {i:l[i] for i in range(len(l))}
print(d)

