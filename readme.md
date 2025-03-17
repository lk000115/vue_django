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

ai辅助代码插件  marscode  ai

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


## ComfyUI共享WebUI模型

在使用Stable Diffusion的WebUI和ComfyUI时，可能会遇到模型存储空间的问题。如果在WebUI中已经下载了很多模型，
可以通过共享这些模型来避免重复下载，从而节省存储空间。以下是如何在ComfyUI中共享WebUI模型的步骤：

修改配置文件

首先，找到ComfyUI的根目录，并找到名为extra_model_paths.yaml.example的文件。将该文件重命名为extra_model_paths.yaml

*** 将文件名从 extra_model_paths.yaml.example 改为 extra_model_paths.yaml
*** 修改后的文件内容如下：
a111:
base_path: path/to/stable-diffusion-webui/
checkpoints: models/Stable-diffusion
configs: models/Stable-diffusion
vae: models/VAE
loras: |
models/Lora
models/LyCORISss
upscale_models: |
models/ESRGAN
models/RealESRGAN
models/SwinIR
embeddings: embeddings
hypernetworks: models/hypernetworks
controlnet: models/ControlNet
1 设置模型路径

打开刚刚修改的extra_model_paths.yaml文件，找到base_path字段，将其值修改为你本地的Stable Diffusion WebUI安装路径。
例如，如果你的WebUI安装在D:/stable-diffusion-webui，则修改为：

base_path: D:/stable-diffusion-webui
检查ControlNet文件夹

如果你的ControlNet文件夹不在WebUI的models文件夹下，还需要进行以下操作
2 回到WebUI根目录，找到extensions文件夹。

进入sd-webui-controlnet文件夹，找到其中的models文件夹。

复制该文件夹的路径。

回到extra_model_paths.yaml文件中，找到controlnet字段，将复制的路径粘贴到这里。

controlnet: D:/stable-diffusion-webui/extensions/sd-webui-controlnet/models
重启ComfyUI

保存并关闭extra_model_paths.yaml文件，然后重新启动ComfyUI。此时，你应该可以在ComfyUI中看到从WebUI共享过来的所有模型

3通过以上步骤，你可以轻松地在ComfyUI中共享WebUI的模型，从而节省存储空间并提高效率

##  comfyui提示词翻译插件安装

进入comfyui插件目录 /ComfyUI/custom_nodes/
执行 git clone https://github.com/juehackr/comfyui_fk_server.git
重启 ComfyUI

baidu翻译api密钥,
https://api.fanyi.baidu.com/manage/developer

20250317002305921    HIpC_oaYUR1WoNCSxbcU