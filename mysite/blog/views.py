# -*- coding: utf-8 -*-

from . import blog
from flask import render_template, url_for, request, redirect
from .. import flatpages
import json

blog.secret_key = '\xda\xb8\xc8d\xe9Ml]\xa3\x86*\x12}\xc3\xad\xe2\xe0\xe0\x83K]\xadGD'


@blog.route('/')
def index():
    return "Hello World!"

@blog.route('/home')
def home():
	articles = (p for p in flatpages if 'date' in p.meta)
	return render_template('article.html', pages=articles)

@blog.route('/resume')
def resume():
	return render_template('resume.html')


@blog.app_errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404

@blog.route('/pagelist')
def pagelist():
	articles = (p for p in flatpages if 'date' in p.meta)
	return render_template('pagelist.html', pages=articles)

@blog.route('/pagelist/<path:path>/')
def page(path):
    page = flatpages.get_or_404(path)
    return render_template('onepage.html', page=page)
