# -*- coding:utf-8 -*-

from ihome.api_1_0 import api


@api.route('/', methods=['GET', 'POST'])
def index():
    # redis_store.set('name', 'owen')
    # session['name'] = 'owen'

    return 'index'