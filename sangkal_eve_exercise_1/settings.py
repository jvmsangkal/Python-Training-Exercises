from domains.questions import questions
from domains.test_papers import test_papers
from domains.users import users

DOMAIN = {
    'questions': questions,
    'test_papers': test_papers,
    'users': users
}

# DB Config
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB_NAME = 'eve'

# Global config
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

SORTING = False
HATEOAS = False
PAGINATION_LIMIT = 10
