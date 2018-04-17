# -*- coding:utf-8 -*-

import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import Config

app = Flask(__name__)
# 配置
app.config.from_object(Config)
# 数据库
db = SQLAlchemy(app)
# 全局可用的redis
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启 csrf 保护
CSRFProtect(app)
# 开启Session
Session(app)