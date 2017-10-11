import csv
import pandas as pd
import os
import argparse

def unsplit_csv_into_files(filenames, sep=' '):
    files = [open(file_) for file_ in filenames]
    for row in zip(*files):
        print(sep.join([c.strip() for c in row]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Join mutliple csv columns from many files')
    parser.add_argument('columnfiles', nargs='+', help='name of the files containing each separate column')
    args = parser.parse_args()
    columnfiles = args.columnfiles
    unsplit_csv_into_files(columnfiles,'::')
