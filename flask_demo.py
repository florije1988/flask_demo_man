# -*- coding: utf-8 -*-
__author__ = 'manman'
from flask import Flask  # 初始化

app = Flask(__name__)  # name是所需变量值


@app.route('/')  # 路由和视图函数
def hello_world():
    return '<h1>hello world!</h1>'


if __name__ == '__main__':  # 启动服务器
    app.run(debug=True, host='0.0.0.0')
