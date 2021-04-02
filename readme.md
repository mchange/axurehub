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

3. 修改业务线

修改文件“hub > models.py > BU_OPTION”

```
BU_OPTION = (
    ('0', '业务线1'),
    ('1', '业务线2'),
    ('2', '业务线3'),
    ('3', '业务线4'),
    ('4', '业务线5'),
    ('5', '业务线6'),
)
```
然后执行命令：
```
python manage.py makemigrations
python manage.py migrate   
```
