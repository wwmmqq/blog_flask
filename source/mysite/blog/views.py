# -*- coding: utf-8 -*-

from . import blog 
from flask import render_template, url_for, request, redirect
from .. import flatpages, Email
from flask_mail import Message
from wtforms import Form, TextAreaField, StringField,SubmitField, validators

import sys, urllib, urllib2, json


class EmailForm(Form):
	#email = TextField("Email Addres",[validators.Required()])
	email = StringField('Email Addres', validators.Required())
	message = TextAreaField("Message",[validators.Required()])
	#StringField类表示一个type="text"属性的<input>标签
	submit = SubmitField("Send",[validators.Required()])
	#SubmitField类表示一个type="submit"属性的<input>标签

@blog.route('/')
def index():
    return render_template('home.html')

@blog.route('/home', methods=['GET'])
def home():
	ip = request.remote_addr
	with open('iplog.txt', 'a') as f:
		f.write("{}\n".format(ip))
	return render_template('home.html')


@blog.route('/sendemail', methods=['POST'])
def sendemail():
	email_form = EmailForm(request.form)
	if request.method == 'POST':
		if email_form.validate() == False:
		      print 'All fields are required.'
		      #flash('Thanks for registering')
		      return render_template('email.html', form=email_form)
		else:
			msg = Message('Hello',
					sender=sender_mail,
					recipients=[].append(app.config['MAIL_ADDR']))
			msg.body = """
			      From: <%s>
			      %s
			      """ % (email_form.email.data, email_form.message.data)
			mail.send(msg)
			return render_template('home.html', email_form)


#https://pythonhosted.org/Flask-FlatPages/
@blog.route('/scribbles')
def scribbles():
	articles = (p for p in flatpages if 'date' in p.meta)
	latest = sorted(articles, reverse=True,
	                    key=lambda p: p.meta['time'])
	return render_template('scribbles.html', pages=latest)

@blog.route('/scribbles/<path:path>/')
def ascribble(path):
    page = flatpages.get_or_404(path)
    return render_template('page.html', page=page)

@blog.route('/resume')
def resume():
	return render_template('resume.html')

@blog.route('/tags', methods=['GET'])
def contact():
	ip = request.remote_addr#'219.228.146.21'
	#url = 'http://apis.baidu.com/apistore/iplookupservice/iplookup?ip='+ip
	#req = urllib2.Request(url)
	#req.add_header("apikey", "3872039f1e4d7873e17cc50963c94541")
	#resp = urllib2.urlopen(req)
	#content = resp.read()
	#info = json.loads(content)
	#print content
	#location =  info['retData']['country'] + info['retData']['province'] + info['retData']['city'] + info['retData']['district'] +info['retData']['carrier']
	return render_template('tags.html',yourip=ip)

@blog.app_errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404
