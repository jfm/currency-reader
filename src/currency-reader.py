from resources.health import Health
from schedulers.coin_schedule import CoinScheduler
from coins.coin_eth import Ethereum
from coins.coin_btc import Bitcoin
import falcon

ethereum = Ethereum()
bitcoin = Bitcoin()
coin_scheduler = CoinScheduler()
coin_scheduler.scheduled_thread(ethereum.fetch_price, 5)
coin_scheduler.scheduled_thread(bitcoin.fetch_price, 13)


app = falcon.API()
health_resource = Health()
app.add_route('/health', health_resource)

coin_scheduler.start()
