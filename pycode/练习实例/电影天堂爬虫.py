import requests
import re
url = "https://www.dy2018.com"
resp = requests.get(url,verify=False)
resp.encoding = 'gb2312'
# print(resp.text)

obj = re.compile(r'2024必看热片.*?<ul>(?P<ul>.*?)</ul>',re.S)
obj2 = re.compile(r"<a href='(?P<herf>.*?)'",re.S)

res = obj.finditer(resp.text)
print('------------------')
for it in res:
    ul = it.group("ul")
    # print(ul)
    res2 = obj2.finditer(ul)
    for it2 in res2:
        print(it2.group('herf'))