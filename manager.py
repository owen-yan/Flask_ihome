# -*- coding:utf-8 -*-
# 程序入口
import redis
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand



class Config(object):
    """配置工程信息"""
    DEBUG = True

    # 数据库的配置信息,真实的开发不会写127 这个ip地址会写真实的ip地址
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis数据库配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379


app = Flask(__name__)

# 加载配置参数
app.config.from_object(Config)

# 链接mysql数据库
db = SQLAlchemy(app)

redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 创建脚本管理器
manager = Manager(app)

# 迁移时，app和db建立关联
Migrate(app, db)

# 将数据库迁移的脚本，命令添加到脚本管理器对象中
manager.add_command('db',MigrateCommand)


@app.route('/')
def index():

    redis_store.set('name', 'owen')
    return 'index'


if __name__ == '__main__':
    manager.run( )