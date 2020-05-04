### 安装

```shell
python -m pip install Django
```



### 创建新文件

```shell
django-admin startproject HelloWorld
```



### 启动

```shell
python manage.py runserver

python manage.py runserver 0.0.0.0:8000  
```



### 配置

```
# settings.py 文件代码：
...TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+"/templates",],       # 修改位置
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
...


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'templates/static'),
]
```



### html 加载 css 文件

在`urls.py`文件添加：

```python
from django.views import static
from django.conf import settings

urlpatterns = [
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static') 
]
```



### 设置 django 外网访问

开启 django 时，使用0.0.0.0:xxxx，作为 ip 和端口，例如：

```shell
python manage.py runserver 0.0.0.0:9000
```

然后在 settings 里修改 `ALLOWED_HOSTS= []`，改为`ALLOWED_HOSTS= ['*',]`，注意不要漏掉“，”。其他机器就可以通过这台机器的ip和端口号访问django了。