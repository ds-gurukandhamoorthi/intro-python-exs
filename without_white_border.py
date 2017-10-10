import matplotlib.image as mpimg
import numpy as np
import argparse
import os

def bounding_box(image_array):
    "returns the lower left corner and upper right corner of the bounding of all non-white pixels"
    #FIXME: the definition of WHITE is different sometimes it is 1.0 at other times it is not
    shp = image_array.shape
    print("shp", shp)
    sum_colors = np.sum(image_array, 2)
    WHITE = 1.0
    height, width = shp[0:2]
    uc_r , uc_c = 0,0
    lc_r , lc_c = 0,0
    for i in range(height):
        if np.all(sum_colors[i] == WHITE*3):
            uc_r = i
        else:
            uc_r += 1
            break
    for i in reversed(range(height)):
        if np.all(sum_colors[i] == WHITE*3):
            lc_r = i
        else:
            lc_r -= 1
            break
    for i in range(width):
        if np.all(sum_colors[:,i] == WHITE*3):
            lc_c = i
        else:
            lc_c += 1
            break
    for i in range(width-1, -1,-1):
        if np.all(sum_colors[:,i] == WHITE*3):
            uc_c = i
        else:
            uc_c -= 1
            break
    return ((lc_r,lc_c),(uc_r,uc_c))

def border_less(filename):
    prefix = os.path.splitext(filename)[0]
    im = mpimg.imread(filename)
    ((lc_r,lc_c),(uc_r,uc_c)) = bounding_box(im)
    print(bounding_box(im))
    if lc_r <= uc_r or uc_c <= lc_c:
        print('no borders: so no conversions made')
        return
    brdrless = im[uc_r:lc_r+1,lc_c:uc_c+1]
    # mpimg.imsave(prefix + '_woborder.png', im)
    mpimg.imsave(prefix + '_woborder.png', brdrless)
    
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Remove white border from an image')
    parser.add_argument('filename',  help='name of the image')
    args = parser.parse_args()
    filename = args.filename
    border_less(filename)
