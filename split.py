import csv
import pandas as pd
import os
import argparse

def split_csv_into_files(filename, n=None):
    with open(filename) as csvfile:
        prefix=os.path.splitext(filename)[0]
        df = pd.read_csv(csvfile)
        if n is None:
            n = df.shape[1]
        for i in range(n):
            column = df.ix[:,i:i+1]
            column.to_csv(prefix+str(i+1)+'.csv', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split csv columns into separate files')
    parser.add_argument('csvfile',  help='name of the csv file')
    parser.add_argument('n', type=int, help='number of columns')
    args = parser.parse_args()
    csvfile = args.csvfile
    n = args.n
    split_csv_into_files(csvfile,n)
