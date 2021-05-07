from prometheus_client import generate_latest
import falcon
import json


class Metrics(object):
    def on_get(self, request, response):
        metrics_response = generate_latest()
        response.status = falcon.HTTP_200
        response.content_type = 'text/plain'
        response.body = metrics_response
