from flask import Flask
from blueprints.user.api import USER_API
from blueprints.movie.api import MOVIE_API

app = Flask(__name__)

app.register_blueprint(USER_API, url_prefix='/user')
app.register_blueprint(MOVIE_API, url_prefix='/movie')

if __name__ == '__main__':
    app.run(debug=True)
