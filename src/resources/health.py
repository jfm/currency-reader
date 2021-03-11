import falcon
import json


class Health(object):
    def on_get(self, request, response):
        health_response = {
                    "health": "OK"
                }
        response.status = falcon.HTTP_200
        response.body = json.dumps(health_response)
