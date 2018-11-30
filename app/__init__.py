#!/usr/bin/python
# -*- coding:utf8 -*-
#默认文件是ASCII格式，需要更改文件编码，操作是在文件首行加上
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
#将routes的导入放在底部可以避免由于这两个文件之间的相互引用而导致的错误

from app import routes