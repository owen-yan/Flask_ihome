# -*- coding:utf-8 -*-
import redis


class Config(object):
    """配置工程信息"""

    DEBUG = True
    # 密匙
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"

    # 数据库的配置信息,真实的开发不会写127 这个ip地址会写真实的ip地址
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis数据库配置：实际开发中会使用redis数据库的真是ip
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # 配置session参数
    # 指定 session 保存到 redis 中
    SESSION_TYPE = "redis"
    # 让 cookie 中的 session_id 被加密签名处理
    SESSION_USE_SIGNER = True
    # 指定使用redis的位置
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # session 的有效期，单位是秒
    PERMANENT_SESSION_LIFETIME = 3600*24


class Development(Config):
    """开发模式下的配置"""
    pass


class Production(Config):
    """生产环境下的配置"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome_Protection"
    PERMANENT_SESSION_LIFETIME = 60*60*24  # 有效时间一天


class UnitTest(Config):
    """测试环境下的配置"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome_UnitTest"


# 准备工程钥匙用的原材料
configs = {
    'dev': Development,
    'pro': Production,
    'test': UnitTest,
}