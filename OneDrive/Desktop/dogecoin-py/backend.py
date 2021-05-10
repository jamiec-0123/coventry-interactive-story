from binance.client import Client
client = Client('5iZ9J2bMtlfDnSH9zUXo3hVSEyEmX6jIqLbajbieCVCBLNJpSMXAvJti8CWOK2Vm', 'ThKjAJYqLFoqPuS6HWqk0RXwt9JAjmFDCWDgna1USqVQNq3jQupyKq0UuvwcWt4a')
def getValue():
    balance = client.get_asset_balance(asset='DOGE')
    myBalance = float(balance['free'])
    prices = client.get_all_tickers()
    for word in prices:
        if word['symbol'] == 'DOGEEUR':
            lastPrice = float(word['price'])
    return(myBalance*lastPrice)
