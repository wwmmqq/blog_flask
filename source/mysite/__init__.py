# -*- coding: utf-8 -*-
'''mysite __init__
''' 

from flask import Flask

from flask_flatpages import FlatPages

from flask_mail import Mail

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

Email = Mail(app)

app.config['FLATPAGES_EXTENSION'] = '.md'
flatpages = FlatPages()
flatpages.init_app(app)

# 注册蓝图
# 后import blog 是因为防止循环导入。 
#blog中引用了flatpage, 如果放在前面则flatpage还未创建从而引发错误
from .blog import blog
#from .api import api
app.register_blueprint(blog)
#app.register_blueprint(api)
