#uwsgi
	pip install uwsgi
	sudo uwsgi config.ini

		[uwsgi]
		# uwsgi 启动时所使用的地址与端口
		socket = 182.254.131.130:8001 
		# 指向网站目录
		chdir = /home/ubuntu/work/myblog

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

	## 第二种方法

		[uwsgi.ini]
		socket = 127.0.0.1:5000 #注： 指定某个固定端口
		processes = 4   #注：跑几个进程，这里用4个进程
		threads = 2	
		master = true
		pythonpath = /data/web_app/testpro
		module = test
		callable = app
		memory-report = true

		pythonpath：表示项目目录
		module：表示项目启动模块，如上例为test.py，这里就为test
		callable：表示Flask项目的实例名称，上例代码中app = Flask(__name__)，所以这里为app
		socket：表示和Nginx通信的地址和端口，和Nginx配置里的uwsgi_pass一致。
		processes：表示开启多少个子进程处理请求。
		threads：每个进程的线程数。



# Nginx
	## 第一种方法
	$: sudo apt-get install nginx
	$: sudo service nginx restart

	[/etc/nginx/sites-available/default]替换
	server {
	   listen  80;
	   server_name 182.254.131.130; #公网地址
	 
	   location / {
	   include      uwsgi_params;
	   uwsgi_pass	127.0.0.1:5000;
	   \#指向uwsgi 所应用的内部地址,所有请求将转发给uwsgi处理 
	   \#注:这里的端口8000和uwsgi的里配的是同一个端口.因为nginx和uwsgi需要通过这个端口进行交互
	   }
	 }


	## 第二种方法 通过sock通讯
	/etc/nginx/sites-available/default
	sudo service nginx restart

	server {
	    listen      80;
	    server_name localhost;
	    charset     utf-8;

	    location / {
	    	include uwsgi_params;
	    	uwsgi_pass unix:/home/ubuntu/work/myblog/uwsgi.sock;
	     }
	}

# Create an Upstart Script

#  1. command & ： 后台运行，你关掉终端会停止运行
   2. nohup command & ： 后台运行，你关掉终端也会继续运行

   3. ps -ef | grep uwsgi
   4. sudo killall uwsgi

   
#https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-14-04
$: sudo start myblog
#sudo nano /etc/init/myblog.conf

description "uWSGI server instance configured to serve flask_dev"

start on runlevel [2345]
stop on runlevel [!2345]

setuid ubuntu
setgid www-data

env PATH=/home/ubuntu/work/flask_dev/venv/bin
chdir /home/ubuntu/work/flask_dev
exec uwsgi --ini uwsgi.ini
