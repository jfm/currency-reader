import time
import schedule
import threading


class CoinScheduler():

    def ethereum_schedule(self):
        print("ETH")

    def bitcoin_schedule(self):
        print("BTC")

    def scheduled_thread(self, method, seconds):
        thread = threading.Thread(target=method)
        thread.start()
        schedule.every(seconds).seconds.do(method)

    def start(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

