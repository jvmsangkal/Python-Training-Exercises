from lib.error_handler import FailedRequest
from urllib.parse import quote

import uuid

def clean_string(string, delimiter=' '):
    return delimiter.join(string.split())

def generate_UUID():
    return str(uuid.uuid4())

def get_data(reqd, optional, body):
    ret = {}

    i = len(reqd) - 1
    while i >= 0:
        temp = reqd[i]

        if not temp in body or type(body[temp]) == object:
            raise FailedRequest(
                'Missing required parameter: ' + str(temp), 400)

        ret[temp] = body[temp]

        if isinstance(ret[temp], str):
            ret[temp] = clean_string(ret[temp])

            if ret[temp] == '':
                raise FailedRequest(
                    'Missing required parameter: ' + str(temp), 400)

        i -= 1

    i = len(optional) - 1
    while i >= 0:
        temp = optional[i]

        if not temp in body or type(body[temp]) == object:
            ret[temp] = None

        else:
            ret[temp] = body[temp]

        if isinstance(ret[temp], str):
            ret[temp] = clean_string(ret[temp])

            if ret[temp] == '':
                ret[temp] = None

        i -= 1

    return ret

def encode_params(params):
    params_encoded = []

    for key in params.keys():
        params_encoded.append(quote(key, safe='~()*!.\'')
                              + '=' + quote(params.get(key), safe='~()*!.\''))

    return '&'.join(params_encoded)
