questions = {
    'schema': {
        'question': {
            'type': 'string',
            'required': True,
            'maxlength': 200
        },
        'choices': {
            'type': 'list',
            'minlength': 4,
            'schema': {
                'type': 'dict',
                'schema': {
                    'choice': {
                        'type': 'string',
                        'required': True
                    },
                    'correct': {
                        'type': 'boolean'
                    }
                }
            }
        },
        'points': {
            'type': 'integer',
            'min': 0
        }
    },
    'soft_delete': True,
    'item_methods': ['GET', 'PATCH', 'DELETE']
}
