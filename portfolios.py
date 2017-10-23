from StockAccount import StockAccount

def read_portfolios(lst_files):
    stock_accounts = [None] * len(lst_files)
    for i, filename in enumerate(lst_files):
        stock_accounts[i] = StockAccount(filename)
    return stock_accounts

def max_values(lst_portfolios):
    max_v = None
    res = None
    for pf in lst_portfolios:
        pf_value = pf.total_value()
        if max_v is None or pf_value > max_v:
            res = pf
            max_v = pf_value
    return res

def min_values(lst_portfolios):
    min_v = None
    res = None
    for pf in lst_portfolios:
        pf_value = pf.total_value()
        if min_v is None or pf_value < min_v:
            res = pf
            min_v = pf_value
    return res




if __name__ == "__main__":
    pfs = read_portfolios(['tur.pf', 'ano.pf', 'three.pf'])
    print('maximum value for')
    pf_max = max_values(pfs)
    print(pf_max)
    print('minimum value for')
    pf_min = min_values(pfs)
    print(pf_min)


