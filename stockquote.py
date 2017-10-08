import argparse
from yahoo_finance import Share





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get stock quote')
    parser.add_argument('sym',  help='stock''symbol')
    args = parser.parse_args()
    sym = args.sym
    share = Share(sym)
    print(share.get_price())



