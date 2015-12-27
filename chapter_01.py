# -*- coding: utf-8 -*-
__author__ = 'manman'

from flask import Flask, request

app = Flask(__name__)


@app.route('/')  # 修饰器
def index():  # 视图函数
    # return '<h1>hello XiaoBiZai!</h1>'
    user_agent = request.headers.get('User-Agent')
    return 'Your browser is %s' % user_agent


# 添加一个动态路由
@app.route('/user/<int:id>', methods=['POST'])
def user(id):
    print type(id)
    return '<h1>hello %s</h1>' % id


@app.before_request
def before_request():
    print 'before_request'


@app.after_request
def after_request():
    print 'after_request'


@app.teardown_request
def teardown_request():
    """

    :return:
    """
    print ''


if __name__ == '__main__':
    app.run(debug=True, port=8010)
