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
  