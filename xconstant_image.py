import argparse
import numpy as np
import matplotlib.image as mpimg

def canvas_create(color, filename,width = 256, height=256):
    color_ = tuple(c / 255 for c in color)
    canvas = np.full([height, width, 3], color_)
    mpimg.imsave(filename, canvas)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a canvas for the given R G B coordinates')
    parser.add_argument('r', type=int, help='red')
    parser.add_argument('g', type=int, help='green')
    parser.add_argument('b', type=int, help='blue')
    args = parser.parse_args()
    color = (args.r, args.g, args.b)
    canvas_create(color, 'canvas.png')



