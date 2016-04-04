title: Flask deploy
date: Saturday, April 2, 2016
time: 2016_04_02
summary: Flask 部署相关
tag: flask, python

Hello, *World*!

Lorem ipsum dolor sit amet, …

# python web app

## 框架选择： Flask + nginx + SAE

## Flask 
		Flask is based on Werkzeug and Jinja2
		Werkzeug 是一个 WSGI 套件。 
		WSGI 是 Web 应用与多种服务器之间的标准Python 接口，即用于开发，也用于部署。 
		Jinja2 是用于渲染 模板的。

## python base
	__init__.py 文件会在导入时被执行。 

## Flask base
	
	virtualenv	 venv_name
	source venv_name/bin/activate

	在模板内部你也可以访问 request 、session 和 g对象，以及 get_flashed_messages() 函数。

## problem list
	1.	ImportError: No module named flask.ext.script
		solve: pip install Flask-Script 

## MarkDown (use flask-flatpages)

	pip install flask-flatpages


## 部署 Flask + Nginx + uWSGI 
	Nginx是一个提供静态文件访问的web服务，然而，它不能直接执行托管Python应用程序，而uWSGI解决了这个问题。