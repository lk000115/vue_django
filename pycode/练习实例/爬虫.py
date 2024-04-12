from urllib.request  import urlopen
# 安装第三方模块requests
import requests
url = 'https://www.sogou.com/web?query=周杰伦'

dic = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
}

resp = requests.get(url,headers=dic)

print(resp.text)


# url = "http://www.baidu.com"
# resp = urlopen(url)
# with open("mybaidu.html",mode="w") as f:
#     f.write(resp.read().decode("utf-8"))

