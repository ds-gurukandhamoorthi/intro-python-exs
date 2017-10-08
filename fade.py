from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import argparse
import os
from functools import partial

def morph(from_pixel, to_pixel, weight):
    def mul(tup, c):
        return tuple( x * c for x in tup)
    assert weight >= 0
    assert weight <= 1
    return tuple( f*(1-weight) + t*weight  for f,t in zip(from_pixel, to_pixel))

def morph_array(from_array, to_array, weight):
    assert from_array.shape == to_array.shape
    dims = from_array.shape
    res_array = np.zeros(from_array.shape)
    for row_i in range(dims[0]):
        for pix_i in range(dims[1]):
            coord = (row_i, pix_i)
            # print(from_array[coord], to_array[coord])
            res_array[coord] = morph(from_array[coord], to_array[coord], weight)
            # print("res_array[coord]", res_array[coord])
    return res_array

def morph_images_weight(fromfile, tofile, outfile, weight):
    src = mpimg.imread(fromfile)
    trgt = mpimg.imread(tofile)
    morphed = morph_array(src, trgt, weight)
    mpimg.imsave(outfile, morphed)

def morph_images(fromfile, tofile, output_prefix, n):
    for i in range(0, n+1):
        out_file=output_prefix+'_morph'+str(i)+'_'+str(n)+ '.png'
        morph_images_weight(fromfile, tofile, out_file, i/n)









if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert image to grayscale')
    parser.add_argument('source',  help='name of the image file')
    parser.add_argument('target', help='name of the image file')
    parser.add_argument('nb_steps',type=int, help='number of steps to transform source into target')
    parser.add_argument('--output',  help='output file name', action='store_true')
    args = parser.parse_args()
    source = args.source
    target = args.target
    nb_steps = args.nb_steps
    if args.output is False:
        frm, ext = os.path.splitext(source)
        to, ext = os.path.splitext(target)
        output_prefix = frm+'_'+to
    else:
        outputfile = args.output
    morph_images(source, target, output_prefix, nb_steps)

