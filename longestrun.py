from rle import rle
from ioutils import read_ints

if __name__ == "__main__":
    array = read_ints()
    length_and_run = rle(array)
    run, leng = max(length_and_run)
    print(run , 'consecutive', leng,'s')
