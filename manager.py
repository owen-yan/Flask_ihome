# -*- coding:utf-8 -*-
# 程序入口

from werkzeug.routing import BaseConverter
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from ihome import get_app, db


# 使用工厂设计模式创建app，并传入配置模式
app = get_app('dev')

# 关联app
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