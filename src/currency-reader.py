from pycoingecko import CoinGeckoAPI
from resources.health import Health
from resources.metrics import Metrics
from schedulers.coin_schedule import CoinScheduler
from coins.coin_prices import CoinPrices
import falcon
import os


coingecko = CoinGeckoAPI()
prices = CoinPrices(coingecko, ['bitcoin','ethereum','cardano'], ['dkk', 'usd'])
coin_scheduler = CoinScheduler()

coin_scheduler.scheduled_thread(prices.fetch_prices, 60)

app = falcon.API()
health_resource = Health()
metrics_resource = Metrics()
app.add_route('/health', health_resource)
app.add_route('/metrics', metrics_resource)

coin_scheduler.start()
