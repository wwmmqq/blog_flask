# This is my blog powered by flask and markdown

## 使用了flask中的蓝图(blueprint)来设计。蓝图: 试用于大型的应用。
	blog = Blueprint('blog', __name__, url_prefix='/blog',template_folder='templates', static_folder='static')


## 使用的python包

	markdown解析包
	pygments代码高亮包
	mathjax相关修改