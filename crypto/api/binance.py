from binance import Client


def getClient(api_key, api_sec):
    return Client(api_key, api_sec, {"timeout": 8})

def printAssetBalance(asset):
    name = asset['asset']
    balance = asset['free'].rjust(16)
    print(name + ":\t" + balance)

def printSymbol(symbol):
    name = symbol['symbol']
    price = symbol['price'].rjust(16) + " USD"
    print(name + ":\t" + price)



def account(api_key, api_sec):
    client = getClient(api_key,api_sec)
    printAssetBalance(client.get_asset_balance(asset='USDT'))
    printAssetBalance(client.get_asset_balance(asset='BTC'))
    printAssetBalance(client.get_asset_balance(asset='ETH'))
    print()


def prices(api_key, api_sec):
    client = getClient(api_key,api_sec)
    printSymbol(client.get_symbol_ticker(symbol="BTCUSDT"))
    printSymbol(client.get_symbol_ticker(symbol="ETHUSDT"))
    print()
