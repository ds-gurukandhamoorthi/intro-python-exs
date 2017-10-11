import argparse
from yahoo_finance import Share





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get stock quote')
    parser.add_argument('syms', nargs='+', help='stock''symbol')
    args = parser.parse_args()
    syms = args.syms
    for sym in syms:
        share = Share(sym)
        print(sym.rjust(8), ':', end='')
        print(share.get_price())



