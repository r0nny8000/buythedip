"""
Command Line Interface for CRY

"""
import os
import click
from pyfiglet import Figlet

import crypto.api.binance as api


BINANCE_API_KEY = os.path.expanduser(os.getenv('BINANCE_API_KEY','NONE'))
BINANCE_API_SEC = os.path.expanduser(os.getenv('BINANCE_API_SEC','NONE'))

@click.group()
def cli():
    pass

def printHeadline(msg):
    figlet = Figlet(font='cyberlarge')
    print(figlet.renderText(msg))

@cli.command()
def account():
    """
    Show the current balances of the wallet.
    """
    printHeadline("Account")
    api.account(BINANCE_API_KEY, BINANCE_API_SEC)

@cli.command()
def prices():
    """
    Show the prices of Cryptos.
    """
    printHeadline("Prices")
    api.prices(BINANCE_API_KEY, BINANCE_API_SEC)

@cli.command()
@click.argument('amount')
@click.argument('from_symbol')
@click.argument('to_symbol')
def exchange(amount, from_symbol, to_symbol):
    """
    Exchange an <amount> of crypto from <symbol> to <symbol>.
    """
    printHeadline("Exchange")
    api.exchange(BINANCE_API_KEY, BINANCE_API_SEC, amount, from_symbol, to_symbol)


if __name__ == '__main__':
    cli()    
