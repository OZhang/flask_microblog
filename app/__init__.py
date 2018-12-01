#!/usr/bin/python
# -*- coding:utf8 -*-
#默认文件是ASCII格式，需要更改文件编码，操作是在文件首行加上
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#将routes的导入放在底部可以避免由于这两个文件之间的相互引用而导致的错误

from app import routes, models
