import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import argparse
import os
from functools import partial
from distance import euclideanDist



def zoom(img_array, x_factor, y_factor, scale_factor):
    MAX_RADIUS = 50
    orig_shp = img_array.shape
    height, width = orig_shp[0:2]
    res = np.zeros([height, width, 3])
    center = (height-int(height * y_factor), int(width * x_factor))
    for i, row in enumerate(res):
        for j, pixel in enumerate(row):
            dist = euclideanDist((i,j), center) 
            if dist < MAX_RADIUS:
                orig_point = center[0]+(i - center[0])* (1-scale_factor), center[1]+(j-center[1])*(1-scale_factor)
                res[i,j] = img_array[orig_point]
            else:
                res[i,j] = img_array[i,j]
    return res





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert image to grayscale')
    parser.add_argument('filename',  help='name of the image file')
    parser.add_argument('--output',  help='output file name', action='store_true')
    args = parser.parse_args()
    filename = args.filename
    if args.output is False:
        fn, ext = os.path.splitext(filename)
        outputfile = fn+'_scaled.png'
    else:
        outputfile = args.output


    im2 = mpimg.imread(filename)
    zoomed = zoom(im2, 0.66,0.9, 0.4)




    # print(im2)
    # gray = np.dot(im2[...,:3], WEIGHTED_RGB)
    plt.imshow(zoomed)
    plt.show()
    mpimg.imsave(outputfile, scaled)

