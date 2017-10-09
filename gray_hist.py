import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw histogram of a grayscale image')
    parser.add_argument('filename',  help='name of the grayscale image file')
    args = parser.parse_args()
    filename = args.filename
    im = mpimg.imread(filename)
    a = np.hstack(im)
    plt.hist(a,bins='auto')
    plt.show()
