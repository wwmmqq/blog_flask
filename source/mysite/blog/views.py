# -*- coding: utf-8 -*-

from . import blog
from flask import render_template, url_for, request, redirect
from .. import flatpages
import json


@blog.route('/')
def index():
    return render_template('home.html')

@blog.route('/home')
def home():
    return render_template('home.html')

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

@blog.route('/tags')
def contact():
	return render_template('tags.html')

@blog.app_errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404
