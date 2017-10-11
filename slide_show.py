import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse
import os





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Slide show of images')
    parser.add_argument('files',nargs='+', help='list of image files')
    args = parser.parse_args()

    files = args.files

    for file_ in files:
        im2 = mpimg.imread(file_)
        plt.imshow(im2)
        plt.draw()
        plt.pause(1e-17)
        time.sleep(1)
    plt.show()

