"""
Middleware to serialize the response
"""
import json


class Serializer(object):

    def process_response(self, req, resp, *args):
        if 'result' not in resp.context:
            return
        resp.body = json.dumps(resp.context['result'])
