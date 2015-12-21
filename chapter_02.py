# -*- coding: utf-8 -*-
__author__ = 'manman'
from flask import Flask
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/', methods=['GET'])
def index():
    return 'index'

# ...

if __name__ == '__main__':
    manager.run()
