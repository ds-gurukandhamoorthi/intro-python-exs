import sys
import csv
import pandas as pd
import re
class Element:
    def __init__(self, element, number, symbol, weight):
        self._element = element
        self._number = number
        self._symbol = symbol
        self._weight = weight

    def __str__(self):
        return self._element + '(' + self._symbol + ', ' + str(self._number) +',' + str(self._weight) + ')' 


def molecular_weight_symb(symb, nmb, periodic_table):
    return periodic_table[symb]._weight * nmb

def molecular_weight(eq, periodic_table):
    eq_ = re.sub('([0-9]+)', ' \\1 ', eq)
    eq_ = [ s for s in re.split('\W+', eq_)  if s != '']
    symb, nmb = eq_
    nmb = int(nmb)
    return molecular_weight_symb(symb, nmb,periodic_table)
    

    

if __name__ == "__main__":
    h= Element('hydrog', 1, 'H', 3)
    print(h)
    filename = sys.argv[1]
    df = pd.read_csv(filename, index_col=False)
    # print(df)
    print(df.shape)
    # print(df.iloc[0,0:4])
    periodic_table = {}
    for i in range(0,df.shape[0]):
        el=df.loc[i,'Element']
        num=df.loc[i,'Number']
        sym=df.loc[i,'Symbol']
        wght=df.loc[i,'Weight']
        element = Element(el, num, sym, wght)
        periodic_table[sym] = element
        print(element)

    print(molecular_weight('H20', periodic_table))

