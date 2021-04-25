# AxureHub 产品原型Web文件托管服务
> 基于 Python 3.x 和 Django 3.0.5

在线教程：[Django 文档](https://docs.djangoproject.com/zh-hans/3.1/)

## 本地运行

1. 将代码clone到本地
2. 安装Django，已安装可忽略
```
pip install -r requirements.txt
```
3. 启动
```
python manage.py runserver --insecure
```
4. 访问：htttp://127.0.0.1:8000




## Docker运行

1. 构建镜像
```
docker build -t axurehub .
```

2. 启动容器
```
docker run -d -p 8000:8000 --name axurehub  axurehub
```
3. 宿主机访问：htttp://127.0.0.1:8000

> 托管文件在www文件加下，可将此文件映射到宿主机，可做备份使用。
> ```
> docker run -d -p 8000:8000 -v /Users/admin/Downloads/axurehub:/usr/src/app/www --name axurehub  axurehub
> ```

**/usr/src/app/media**: 存放上传的压缩包
**/usr/src/app/www**: 存放解压后的web文件
**/usr/src/app/data**: 存放数据库文件

建议将以上目录都映射到宿主机。




## 数据操作

1. 清空数据库
    - 删除数据库文件：db.sqlite3
    - 删除项目的migrations模块中的所有文件，除了__init__.py 文件
    - 运行命令
    ```
    python manage.py makemigrations
    python manage.py migrate    
    ```
    - 重启应用/容器

2. 创建管理员

```
# 创建超级管理员
python manage.py createsuperuser

# 修改管理员密码
python manage.py changepassword ${username}
```

#  makemigrations 不生效问题

连接数据库：
sudo sqlite3 db.sqlite3 
或者
python manage.py dbshell 

进到数据库中，执行：
delete from django_migrations where app='your_appname';

再次执行变更：
python manage.py makemigrations
python manage.py migrate 



