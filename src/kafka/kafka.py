from kafka import KafkaProducer
import json
import os


class CoinProducer(object):

    def __init__(self):
        self.producer = KafkaProducer(
                value_serializer=lambda v: json.dumps(v).encode("utf-8"),
                bootstrap_servers=os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:1324')
                )

    def send(self, data):
        self.producer.send('coin_update', data)
