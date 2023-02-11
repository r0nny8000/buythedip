from binance import Client
from binance import exceptions 


def getClient(api_key, api_sec):
    return Client(api_key, api_sec, {"timeout": 8})


def printAssetBalance(asset):
    name = asset['asset']
    balance = asset['free'].rjust(16)
    print(name + "\t" + balance)


def printSymbol(symbol):
    print(symbol['symbol'] + ":\t" + str(float(symbol['price'])).rjust(16) + " USDT")


def account(api_key, api_sec):
    client = getClient(api_key,api_sec)
    printAssetBalance(client.get_asset_balance(asset='USDT'))
    printAssetBalance(client.get_asset_balance(asset='BTC'))
    printAssetBalance(client.get_asset_balance(asset='ETH'))
    printAssetBalance(client.get_asset_balance(asset='SOL'))
    

def exchange(api_key, api_sec, from_quantity, from_symbol, to_symbol):
    client = getClient(api_key,api_sec)
    symbol = to_symbol + from_symbol

    print("Balance before exchange:\n")
    account(api_key, api_sec)
    print()

    try:
        price = client.get_symbol_ticker(symbol=symbol)
        print("Exchange:\n")
        print(from_quantity + " " + from_symbol + " to " + to_symbol + " at a rate of " + str(float(price['price'])) + " " + from_symbol)

        to_quantity = round(float(from_quantity) / float(price['price']), 4)
        print(str(to_quantity) + " " + to_symbol + " calculated")

        order = client.order_market_buy(symbol=symbol, quantity=to_quantity)
        print(str(float(order['executedQty'])) + " " + to_symbol + " received")

    except exceptions.BinanceAPIException as exception:
        print(exception)

    print()
    print("Balance after exchange:\n")
    account(api_key, api_sec)


def prices(api_key, api_sec):
    client = getClient(api_key,api_sec)
    printSymbol(client.get_symbol_ticker(symbol="BTCUSDT"))
    printSymbol(client.get_symbol_ticker(symbol="ETHUSDT"))
    print()
