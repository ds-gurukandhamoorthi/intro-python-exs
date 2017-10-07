from sys import stdin
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Prints lines containing the given string')
    parser.add_argument('text',  help='the text that must be contained in the lines')
    args = parser.parse_args()
    text = args.text
    for line in stdin:
        if text in line:
            print(line,end='')


