#!/usr/bin/python
# -*- coding:utf8 -*-
from flask import render_template, flash, redirect,url_for
from app import app
from app.forms import LoginForm

#＠app.route行是装饰器
#装饰器的常见模式是使用它们将函数注册为某些事件的回调函数

@app.route('/')
@app.route('/index')
def index():
    #return "Hello, World!"
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    #render_template()函数调用Flask框架原生依赖的Jinja2模板引擎
    #return render_template('index.html', title='Home',user=user)
    #return render_template('index.html', user=user)
    return render_template('index.html', title='Home',user=user, posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)