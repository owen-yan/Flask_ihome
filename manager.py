# -*- coding:utf-8 -*-
# 程序入口

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from ihome import app, db



# class Config(object):
#     """配置工程信息"""
#     SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
#
#     DEBUG = True
#
#     # 数据库的配置信息,真实的开发不会写127 这个ip地址会写真实的ip地址
#     SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#
#     # redis数据库配置
#     REDIS_HOST = "127.0.0.1"
#     REDIS_PORT = 6379
#
#     # flask_session的配置信息
#     SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
#     SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
#     SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用 redis 的实例
#     SESSION_USE_SIGNER = True
#     PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，单位是秒


# app = Flask(__name__)
#
# # 加载配置参数
# app.config.from_object(Config)
#
# # 链接mysql数据库
# db = SQLAlchemy(app)
#
# # redis 数据库
# redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
#
# # 创建脚本管理器
# manager = Manager(app)
#
# # 迁移时，app和db建立关联
# Migrate(app, db)
#
# # 将数据库迁移的脚本，命令添加到脚本管理器对象中
# manager.add_command('db', MigrateCommand)
#
# # csrf 需要保护的方法有post，put， patch， delete
# CSRFProtect(app)
#
# # 将session数据写入数据库
# Session(app)

# 创建脚本管理器
manager = Manager(app)

# 迁移时，app和db建立关联
Migrate(app, db)

# 将数据库迁移的脚本，命令添加到脚本管理器对象中
manager.add_command('db', MigrateCommand)


@app.route('/', methods=['GET', 'POST'])
def index():
    # redis_store.set('name', 'owen')
    # session['name'] = 'owen'

    return 'index'


if __name__ == '__main__':
    manager.run( )