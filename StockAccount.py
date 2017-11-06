import re
import sys
from yahoo_finance import Share
from collections import Counter

class StockAccount:
    def __init__(self, filename):
        with open(filename, 'r') as account_data:
            self._holder = next(account_data)
            self._cash_on_hand = float(next(account_data))
            self._nb_shares = int(next(account_data))
            self._shares = Counter()
            for line in account_data:
                tem = re.split('[ ]+', line)
                nb = int(tem[-2])
                symb = tem[-1]
                nb = int(nb)
                self._shares[symb] = nb

    def buy(self, symb, n):
        self._shares[symb] += n
        if self._shares[symb] == 0:
            del self._shares[symb]
        self._nb_shares = len(self._shares)

    def sell(self, symb, n):
        self._shares[symb] -= n
        if self._shares[symb] == 0:
            del self._shares[symb]
        self._nb_shares = len(self._shares)

    def total_value(self):
        tot = 0
        for symb in self._shares:
            nb = self._shares[symb]
            shr = Share(symb)
            tot += float(shr.get_price()) * nb
        return tot

    def write(self, filename):
        with open(filename, 'w') as account_data:
            account_data.write(str(self))

    def write_report(self):
        print('holder:', self._holder)
        print('cash at disposal:', self._cash_on_hand)
        total = 0
        for symb in self._shares:
            nb = self._shares[symb]
            shr = Share(symb)
            price = float(shr.get_price()) * nb
            print (symb, nb, price) 
            total += price
        print('Total', total)



    def __str__(self):
        res = self._holder
        res += '\n'+ str(self._cash_on_hand)
        res += '\n'+ str(self._nb_shares)
        res += '\n'
        for symb in self._shares:
            nb = self._shares[symb]
            res += str(nb).rjust(4) + ' '+ symb + '\n'
        return res



if __name__ == "__main__":
    filename = sys.argv[1]
    s = StockAccount(filename)
    s.buy('UG', 50)
    # print(s)
    s.sell('UG', 50)
    # s.buy('UG', 50)
    print(s)
    print(s.total_value())
    # s.write('tes.txt')
    s.write_report()
