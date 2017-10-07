from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import argparse
import os

WEIGHTED_RGB = [0.299, 0.587, 0.114]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert image to grayscale')
    parser.add_argument('filename',  help='name of the image file')
    parser.add_argument('--output',  help='output file name', action='store_true')
    args = parser.parse_args()
    filename = args.filename
    if args.output is False:
        fn, ext = os.path.splitext(filename)
        outputfile = fn+'_gray.png'
    else:
        outputfile = args.output



    #method1
    # im = Image.open('mandrill.png')
    # res = im.convert("LA")
    # # res.show()
    # res.save('tes.png',"PNG")

    #method2
    im2 = mpimg.imread(filename)
    # print(im2)
    gray = np.dot(im2[...,:3], WEIGHTED_RGB)
    plt.imshow(gray, cmap='gray')
    plt.show()
    mpimg.imsave(outputfile, gray, cmap='gray')

