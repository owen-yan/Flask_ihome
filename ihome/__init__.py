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

# 注意点，注册蓝图时哪里使用哪里导入，避免某些变量导入时不存在
from ihome.api_1_0 import api
# 注册pai蓝图
app.register_blueprint(api)