"""
Command Line Interface for CRY

"""
import os
import fire

from pyfiglet import Figlet

import crypto.api.binance as api


BINANCE_API_KEY = os.path.expanduser(os.getenv('BINANCE_API_KEY','NONE'))
BINANCE_API_SEC = os.path.expanduser(os.getenv('BINANCE_API_SEC','NONE'))

def _printLarge(msg):
    figlet = Figlet(font='cyberlarge')
    print(figlet.renderText(msg))


def account():
    """
    show balances of the wallet
    """
    _printLarge("Account")
    api.account(BINANCE_API_KEY, BINANCE_API_SEC)

def prices():
    """
    show prices
    """
    _printLarge("Prices")
    api.prices(BINANCE_API_KEY, BINANCE_API_SEC)


def _main():
    fire.Fire()

if __name__ == '__main__':
    _main()
