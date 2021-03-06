from kafka import KafkaProducer
import os
import falcon
import json


class HelloWorldResource(object):

    def __init__(self):
        self.producer = KafkaProducer(
                value_serializer=lambda v: json.dumps(v).encode("utf-8"), 
                bootstrap_servers=os.getenv['KAFKA_BOOTSTRAP_SERVERS', 'localhost:1324']
                )

    def on_get(self, request, response):
        self.producer.send('testQueue', {"data": "Hello World"})

        response.status = falcon.HTTP_200
        response.body = 'Message Sent'


app = falcon.API()
hello = HelloWorldResource()
app.add_route('/', hello)
