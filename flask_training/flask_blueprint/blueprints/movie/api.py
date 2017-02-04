from flask import Flask, Blueprint, render_template

MOVIE_API = Blueprint('MOVIE_API', __name__)

@MOVIE_API.route('/list/')
def get_movies():
    movies = ['Gigi', 'Jack', 'Jose']
    return render_template('movie/list.html', movies=movies)

@MOVIE_API.route('/add/')
def add_movies():
    return render_template('movie/add.html')

@MOVIE_API.route('/view/')
def view_movies():
    return render_template('movie/view.html')
