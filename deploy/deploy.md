#uwsgi
	pip install uwsgi

		[uwsgi]

		# uwsgi 启动时所使用的地址与端口
		socket = 127.0.0.1:8001 

		# 指向网站目录
		chdir = /home/www/ 

		# python 启动程序文件
		wsgi-file = manage.py 

		# python 程序内用以启动的 application 变量名
		callable = app // app 是 manage.py 程序文件内的一个变量
						//这个变量的类型是Flask的 application类

		# 处理器数
		processes = 4

		# 线程数
		threads = 2

		#状态检测地址
		stats = 127.0.0.1:9191
	uwsgi config.ini
	//此时已经正常启动 uwsgi 并将 Flask 项目载入其中了
	//ctrl+c 关闭程序。但这只是命令启动形式，要使其随同服务器启动并作
	//为后台服务运行才是运营环境的实际所需要。因此接下来我们需要安装另一个工具来引导 uwsgi

	sudo apt-get install supervisor
	//supervisor可以同时启动多个应用，最重要的是
	//当某个应用Crash的时候，他可以自动重启该应用，保证可用性。

# Supervisor 的全局的配置文件位置在：
	/etc/supervisor/supervisor.conf
	正常情况下我们并不需要去对其作出任何的改动，只需要添加一个新的 *.conf 文件放在
	/etc/supervisor/conf.d/

	[my_flask_supervisor.conf]
	[program:my_flask]
	# 启动命令入口
	command=/home/www/my_flask/venv/bin/uwsgi /home/www/my_flask/config.ini

	# 命令程序所在目录
	directory=/home/www/my_flask
	#运行命令的用户名
	user=root
	autostart=true
	autorestart=true
	#日志地址
	stdout_logfile=/home/www/my_flask/logs/uwsgi_supervisor.log

	sudo service supervisor start
	sudo service supervisor stop

# Nginx
	$: sudo apt-get install nginx

	[/ext/nginx/sites-available/default]替换
	server {
	   listen  80;
	   server_name XXX.XXX.XXX; #公网地址
	 
	   location / {
	   include      uwsgi_params;
	   uwsgi_pass   127.0.0.1:8001;  # 指向uwsgi 所应用的内部地址,所有请求将转发给uwsgi处理
	   uwsgi_param UWSGI_PYHOME /home/www/my_flask/venv; # 指向虚拟环境目录
	   uwsgi_param UWSGI_CHDIR  /home/www/my_flask; # 指向网站根目录
	   uwsgi_param UWSGI_SCRIPT manage:app; # 指定启动程序
	   }
	 }

	$: sudo service nginx restart