# -*- coding: utf-8 -*-
__author__ = 'manman'

from flask import Flask

app = Flask(__name__)


@app.route('/')  # 修饰器
def index():  # 视图函数
    return '<h1>hello XiaoBiZai!</h1>'


# 添加一个动态路由
@app.route('/user/<name>')
def user(name):
    return '<h1>hello XiaoBiZai!</h1>' % name


if __name__ == '__main__':
    app.run(debug=True, port=8010)
