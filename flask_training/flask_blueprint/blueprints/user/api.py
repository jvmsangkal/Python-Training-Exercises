from flask import Flask, Blueprint, render_template

USER_API = Blueprint('USER_API', __name__)

@USER_API.route('/list/')
def get_users():
    users = ['Gigi', 'Jack', 'Jose']
    return render_template('user/list.html', users=users)

@USER_API.route('/add/')
def add_users():
    return render_template('user/add.html')

@USER_API.route('/view/')
def view_users():
    return render_template('user/view.html')
