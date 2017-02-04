from flask import Flask, Blueprint, request

from lib.decorators import make_response
from database import db
from util import util

from bson.objectid import ObjectId

FOOD_API = Blueprint('FOOD_API', __name__)


@FOOD_API.route('/list/', methods=['GET'])
@make_response
def list_foods(res):
    res_data = []
    for food in db.food.find():
        food['_id'] = str(food['_id'])
        res_data.append(food)

    return res.send(res_data)


@FOOD_API.route('/add', methods=['POST'])
@make_response
def add_food(res):
    params = util.get_data(['name', 'ingredients', 'price', 'stock'], [], request.values)

    db.food.insert_one({
        'name': params['name'],
        'ingredients': params['ingredients'],
        'price': params['price'],
        'stock': params['stock'],
    })

    return res.send({
        'http_status_code': '[ 201, \'Created\' ]',
        'message': 'The food was successfully added.'
    })


@FOOD_API.route('/edit', methods=['PATCH'])
@make_response
def edit_food(res):
    params = util.get_data(['_id', 'name', 'ingredients', 'price', 'stock'], [], request.values)

    db.food.update_one(
        {'_id': ObjectId(params['_id'])},
        {
            '$set': {
                'name': params['name'],
                'ingredients': params['ingredients'],
                'price': params['price'],
                'stock': params['stock']
            }
        }
    )

    return res.send({
        'http_status_code': '[ 200, \'OK\' ]',
        'message': 'The food was successfully edited.'
    })


@FOOD_API.route('/delete', methods=['DELETE'])
@make_response
def delete_food(res):
    params = util.get_data(['_id'], [], request.values)

    db.food.remove(
        {'_id': ObjectId(params['_id'])},
        {'justOne': True}
    )

    return res.send({
        'http_status_code': '[ 200, \'OK\' ]',
        'message': 'The food was successfully deleted.'
    })
