class Ethereum():
    def __init__(self, coingecko):
        self.coingecko = coingecko

    def fetch_price(self):
        print("Fetching ETH price")
        price = self.coingecko.get_price(ids='ethereum', vs_currencies='dkk,usd')
        print(price)
