class Bitcoin():
    def __init__(self, coingecko):
        self.coingecko = coingecko

    def fetch_price(self):
        print("Fetching BTC price")
        price = self.coingecko.get_price(ids='bitcoin', vs_currencies='dkk,usd')
        print(price)
