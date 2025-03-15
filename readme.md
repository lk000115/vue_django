# vue和python笔记

## 1. python笔记

### 1.1 知识要点

- vscode创建python虚拟环境

```python
1 在当前文件夹新建终端并输入以下命令：
python -m venv venv01    # 
2 在当前目录激活虚拟环境
.\venv01\scripts\activate
3 退出虚拟环境
 在虚拟环境提示符下执行 deactivate

```

- vscode 配置识别python虚拟环境

```python
在settings.json中添加
"python.venvPath": '虚拟环境的绝对路径'   #  如: 'd:\\venv'
```

-
- 导入iconfont字体库

  1 把icofont上选中的图片添加到购物车,再添加到自己的项目中
  2 到资源管理,我的项目中.把项目资源下载到本地
  3 把下载的图标文件解压复制到static文件中,
  4 在vue中的main.js文件中,导入 import '@/assets/font/iconfont.css'
  5  挑选相应图标并获取类名，应用于页面：<i class="iconfont icon-xxx"></i>
- linux命令

```
  useradd   es     -M -s /sbin/nologin   创建用户
  ps -ef | grep  nginx   显示nginx的进程  
```

## stable diffusion  AI绘画

模型：基础底模  基础算法1.5   基础算法XL   基础算法F.1


1 正向提示词

基本结构： 人物+场景+环境+氛围
high quality 高品质

masterpiece 杰出

best quality 最好品质

photography 摄影作品

ultra highres 超高分辨率

RAW photo 原始照片

extreme detail 极致的细节

2 反向提示词

worst quality

bad quality

low quality

normal quality

lowres

normal quality

ng_deepnegative_v1_75t,(badhandv4:1.2),EasyNegative,(worst quality:2),

一 文生图
1 迭代步数 建议20-30,就像一块模糊的玻璃,擦拭的次数越多,越清晰
2 提示词引导系数 7-10,引导系数越大,AI发挥的空间就越大
二 图生图
1 重绘幅度:建议0.5-0.75 此值越大,AI重绘的想象空间就越大,和原图越不像,越小和原图越像
2
