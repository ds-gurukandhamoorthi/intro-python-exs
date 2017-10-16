import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import argparse
import os
from functools import partial
from scale import scale



def zoom(img_array, x_factor, y_factor, scale_factor):
    orig_shp = img_array.shape
    height, width = orig_shp
    res = np.zeros([height, width, 3])
    for i, row in enumerate(res):
        for j, pixel in enumerate(row):
            res[i,j] = img_array[scl((i,j))]
    return res





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert image to grayscale')
    parser.add_argument('filename',  help='name of the image file')
    parser.add_argument('width', type=int, help='width of the image')
    parser.add_argument('height', type=int, help='height of the image')
    parser.add_argument('--output',  help='output file name', action='store_true')
    args = parser.parse_args()
    filename = args.filename
    width = args.width
    height = args.height
    if args.output is False:
        fn, ext = os.path.splitext(filename)
        outputfile = fn+'_scaled.png'
    else:
        outputfile = args.output


    im2 = mpimg.imread(filename)
    scaled = scale(im2, (height, width))




    # print(im2)
    # gray = np.dot(im2[...,:3], WEIGHTED_RGB)
    plt.imshow(scaled)
    plt.show()
    mpimg.imsave(outputfile, scaled)

