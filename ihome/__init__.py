# -*- coding:utf-8 -*-

import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import configs


# 创建连接到mysql数据库的对象
db = SQLAlchemy()


def get_app(config_name):
    """"使用工厂设计模式，更具传入不同的config_name,找到不同的配置"""

    app = Flask(__name__)

    # 配置
    # app.config.from_object(Config)
    app.config.from_object(configs[config_name])

    # 创建链接到mysql数据库的对象
    db.init_app(app)


    # 全局可用的redis
    redis_store = redis.StrictRedis(host=configs[config_name].REDIS_HOST, port=configs[config_name].REDIS_PORT)

    # 开启 csrf 保护
    CSRFProtect(app)

    # 开启Session
    Session(app)

    return app
#
# # 注意点，注册蓝图时哪里使用哪里导入，避免某些变量导入时不存在
# from ihome.api_1_0 import api
# # 注册pai蓝图
# app.register_blueprint(api)



