users = {
    'schema': {
        'full_name': {
            'type': 'string',
            'required': True,
            'maxlength': 50
        },
        'username': {
            'type': 'string',
            'required': True,
            'regex': '[A-Za-z0-9]+',
            'unique': True
        },
        'password': {
            'type': 'string',
            'required': True,
            'minlength': 8
        }
    }
}
