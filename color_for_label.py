import matplotlib.image as mpimg
import numpy as np
import argparse
from colorutils import are_compatible, as_matplotlib_color, rand_color
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from geomutils import sub_coords

#matr colors are defined in 0-1, but colors are defined in 0-255 range
def compatible_colors(matr, colors):
    res = set(colors)
    for color in colors:
        color_ = as_matplotlib_color(color)
        for row in matr:
            for pxl in row:
                if not are_compatible(pxl, color_):
                    res.discard(color)
    return list(res)


def filter_compatible_for_label(filename, rectangle, colors):
    im = mpimg.imread(filename)
    # brdrless = im[uc_r:lc_r+1,lc_c:uc_c+1]
    (r1,c1), (r2,c2) = rectangle
    matr = im[r1:r2+1, c1:c2+1]
    return compatible_colors(matr, colors)
    
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Remove white border from an image')
    parser.add_argument('filename',  help='name of the image')
    args = parser.parse_args()
    filename = args.filename
    colors = [rand_color() for i in range(1000)]
    rectangle = ((40,40),(45,50))
    width, height = sub_coords(rectangle[1],rectangle[0])
    acceptable = filter_compatible_for_label(filename,rectangle, colors)
    print("acceptable", acceptable)
    if len(acceptable) > 0:
        color = as_matplotlib_color(acceptable[0])
        fig, ax = plt.subplots()
        im = mpimg.imread(filename)
        rect = patches.Rectangle(rectangle[0],width, height, facecolor='none', edgecolor=color, hatch='x')
        ax.imshow(im)
        ax.add_patch(rect)
        plt.show()


