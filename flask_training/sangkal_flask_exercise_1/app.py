from flask import Flask
from blueprints.food.api import FOOD_API
from lib.error_handler import mod_err

app = Flask(__name__)

# Error and exception handling
app.register_blueprint(mod_err)

app.register_blueprint(FOOD_API, url_prefix='/food')


if __name__ == '__main__':
    app.run(debug=True)
