import sys
import pandas as pd
from ipaddress import IPv4Address


def get_country(ip_knowledge, ip):
    ip = IPv4Address(ip)
    for (begin, end), country in ip_knowledge.items():
        begin, end = IPv4Address(begin), IPv4Address(end)
        if begin <= ip <= end:
            return country


def build_ip_knowledge(csvfile):
    ip_knowlege = {}
    df = pd.read_csv(csvfile, index_col=False)
    for i in range(0, df.shape[0]):
        begin_ip = df.loc[i, 'beginning IP Address']
        end_ip = df.loc[i, 'ending IP Address']
        country = df.loc[i, 'Country Name']
        # print(begin_ip, end_ip, country)
        ip_knowlege[(begin_ip, end_ip)] = country
    return ip_knowlege

def main():
    ip_knowl = build_ip_knowledge('../ip-by-country.csv')
    ip_address = sys.argv[1]
    print(get_country(ip_knowl, ip_address))

if __name__ == "__main__":
    main()
