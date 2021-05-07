class Cardano():
    def __init__(self, coingecko):
        self.coingecko = coingecko

    def fetch_price(self):
        print("Fetching ADA price")
        price = self.coingecko.get_price(ids='cardano', vs_currencies='dkk,usd')
        print(price)
