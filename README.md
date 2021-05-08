# 图书馆管理系统(python3，PyQt5，MySQL)

> ## 实现以下功能:
- 用户注册、登录、修改密码、用户管理

- 存储图书信息、采购和淘汰情况、租借情况 

- 实现图书采购、淘汰、租借功能。 

- 实现图书信息、采购和淘汰、库存、和租借情况查询 

- 实现图书的采购、库存、淘汰、租借情况等统计

## 1.配置项目

1. `LibraryManage.sql`为数据库文件

2. 打开`db.py`进行对数据配置

   ```python
   host = "127.0.0.1"
   user = "root"
   password = "******" # 数据库密码
   database = "***"  # 数据库名字
   ```

   

## 2.运行项目

1. 安装依赖包

   `pip install -r requirements.txt`

2. 运行`MainWindow.py`启动项目

## 3.打包项目

1. `pyinstaller -F -w --clean --icon=./images/MainWindow_1.ico MainWindow.py`生成可执行`exe`文件

2. 生成的文件位于项目文件夹`dist`下。