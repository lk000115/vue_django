## 项目笔记

- 项目依赖导出   **pip freeze>requirements.txt** 命令将项目的库依赖导出
- Pyinstaller -F setup.py 打包exe
- Pyinstaller -F -w payslip.py 不带控制台的打包
- Pyinstaller -F -i xx.ico setup.py 打包指定exe图标

### django

- 右键新建python package目录apps,用于存放APP.
- 在models.py中创建或者修改模型；
- 运行`python manage.py makemigrations`为我们的修改动作创建迁移记录文件；
- 运行`python manage.py migrate`，将操作同步到数据库
- 国际化  
  - LANGUAGE_CODE = 'zh-hans'        # 'en-us' 英语
    TIME_ZONE = 'Asia/Shanghai'
- 

