DOMAIN = {
    'products': {
        'schema': {
            'name': {
                'type': 'string'
            },
            'description': {
                'type': 'string'
            },
            'price': {
                'type': 'integer'
            }
        }
    }
}

MONGO_HOST = 'localhost'
MONGO_PORT = 27017

MONGO_DB_NAME = 'eve'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
