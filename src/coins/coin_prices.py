from kafka.kafka import CoinProducer
from prometheus_client import Gauge


class CoinPrices():
    def __init__(self, coingecko, ids, currencies):
        self.coingecko = coingecko
        self.coin_producer = CoinProducer()
        self.ids = ids
        self.currencies = currencies
        self.gauges = self.initialize_gauges(ids)


    def fetch_prices(self):
        ids_string = ','.join(self.ids)
        currencies_string = ','.join(self.currencies)
        price = self.coingecko.get_price(ids=ids_string, vs_currencies=currencies_string)
        self.publish_prices(price)
        self.gauge_prices(price)


    def initialize_gauges(self, ids):
        gauges = {}
        for id in ids:
            gauges[id] = Gauge(id, '', ['currency'])

        return gauges

    def gauge_prices(self, prices):
        for coin, price in prices.items():
            for currency, value in price.items():
                self.gauges[coin].labels(currency).set(value)

    def publish_prices(self, prices):
        for coin in prices:
            print(coin)
            self.coin_producer.send(coin)

