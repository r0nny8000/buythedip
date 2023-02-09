"""
cli

"""
import fire

import crypto.api.binance as api

def wallet():
    """
    show balances of the wallet
    """
    api.test()


def _main():
    fire.Fire()

if __name__ == '__main__':
    _main()
