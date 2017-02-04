test_papers = {
    'schema': {
        'name': {
            'type': 'string'
        },
        'passing_rate': {
            'type': 'float',
            'min': 0,
            'max': 1
        },
        'question_ids': {
            'type': 'list',
            'schema': {
                'type': 'string',
                'data_relation': {
                    'resource': 'questions',
                    'field': '_id',
                    'embeddable': True
                }
            }
        }
    },
    'soft_delete': True,
    'item_methods': ['GET', 'PATCH', 'DELETE']
}
