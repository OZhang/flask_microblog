#!/usr/bin/python
# -*- coding:utf8 -*-

from flask_wtf import FlaskForm
#Flask-WTF插件本身不提供字段类型，因此我直接从WTForms包中导入了四个表示表单字段的类
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')