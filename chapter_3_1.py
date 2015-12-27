# -*- coding: utf-8 -*-
__author__ = 'manman'

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hard to guess string'


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', current_time=datetime.utcnow(), name=name, form=form)


@app.route('/user/<name>')
def user(name):
    book_dict = {'flask': 20, 'python': 30}
    print book_dict['flask']
    person = Person('i am a good boy.  ')
    return render_template('user.html', name=name, users=['xiaofu', 'xiaozhu'], books=book_dict, index=1, person=person)


@app.route('/user_bak/<name>')
def user_bak(name):
    return render_template('user_bak.html', name=name)


@app.route('/animal/<name>')
def animal(name):
    dog_color = {'white': 12, 'black': 16}
    print dog_color['white']
    person = Dog('HE is xiao bai tu.')
    return render_template('animal.html', name=name, animals=['dog', 'cat'], dogs=dog_color, index=0, person=person)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', name='xiaoqigui'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


class Dog(object):
    """
    person
    """

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Person(object):
    """
    person
    """

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


if __name__ == '__main__':
    app.run()
