import argparse
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from geomutils import add_coords
import random

def as_matplotlib_color(color):
    return tuple([c /255 for c in color])

def albers_square(c1,c2, coord, width):
    c1, c2 = as_matplotlib_color(c1), as_matplotlib_color(c2)
    res = []
    res += [patches.Rectangle(coord, width,width, facecolor=c1)]
    ratio = 0.5
    lc = add_coords(coord, (width*ratio/2, width*ratio/2))
    res += [patches.Rectangle(lc, width*ratio,width*ratio, facecolor=c2)]
    return res

def rand_color():
    return (random.randrange(255),random.randrange(255),random.randrange(255))

def luminance(rgb):
    c = as_matplotlib_color(rgb)
    r, g, b = c
    return 0.299*r+0.587*g+0.114*b



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw albers squares given two colors')
    group=parser.add_mutually_exclusive_group()
    group.add_argument('--colors', type=int, nargs=9,  help='two color''s r g b components ex: 9 90 166 100 100 100')
    group.add_argument('--random', help='random colors', action='store_true')
    args = parser.parse_args()
    fig, ax = plt.subplots()
    ax.set_xlim(0,2.5)
    ax.set_ylim(0,4)
    if args.random==False:
        c = args.colors
        c1 = tuple(c[0:3])
        c2 = tuple(c[3:6])
        c3 = tuple(c[6:9])
        print(c1, c2, c3)
    else:
        c1 = rand_color()
        c2 = rand_color()
        c3 = rand_color()
        print(c1, c2, c3)
    for ptch in albers_square(c1,c2,(0,0), 1):
        ax.add_patch(ptch)
    for ptch in albers_square(c2,c3,(0,1.5), 1):
        ax.add_patch(ptch)
    for ptch in albers_square(c3,c1,(0,3), 1):
        ax.add_patch(ptch)
    for ptch in albers_square(c2,c1,(1.5,0), 1):
        ax.add_patch(ptch)
    for ptch in albers_square(c3,c2,(1.5,1.5), 1):
        ax.add_patch(ptch)
    for ptch in albers_square(c1,c3,(1.5,3), 1):
        ax.add_patch(ptch)
    plt.show()
