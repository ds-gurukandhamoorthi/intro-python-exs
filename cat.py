import argparse
import sys

def cat(files, outfile=None):
    if outfile is None:
        out = sys.stdout
    else:
        out = open(outfile,'w')
    for inpfile in files:
        try:
            with open(inpfile) as inp:
                for line in inp:
                    out.write(line)
        except(FileNotFoundError):
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='cat files')
    parser.add_argument('files',nargs='+',  help='files to concatenate')
    args = parser.parse_args()
    files = args.files
    print(files) 
    cat(files)
