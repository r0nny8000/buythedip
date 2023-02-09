from binance import Client


def printAssetBalance(asset):
    name = asset['asset']
    balance = asset['free'].rjust(16)
    print(name + ":\t" + balance)



def account(api_key, api_sec):
    client = Client(api_key, api_sec, {"timeout": 8})
    
    

    printAssetBalance(client.get_asset_balance(asset='USDT'))
    printAssetBalance(client.get_asset_balance(asset='BTC'))
    printAssetBalance(client.get_asset_balance(asset='ETH'))


    print()