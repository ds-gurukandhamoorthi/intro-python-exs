import matplotlib.pyplot as plt
import matplotlib.collections
from geomutils import midpoint
import sys


def other_corners(bottom_left, top_right):
    x0, y0 = bottom_left
    x1, y1 = top_right
    return (x0,y1), (x1,y0)

def vertical_split(bottom_left, top_right):
    top_left, bottom_right = other_corners(bottom_left, top_right)
    return [midpoint(bottom_left, bottom_right), midpoint(top_left, top_right)]

def horizontal_split(bottom_left, top_right):
    top_left, bottom_right = other_corners(bottom_left, top_right)
    return [midpoint(bottom_left, top_left), midpoint(bottom_right, top_right)]

def box_lines(bottom_left, top_right):
    lines = []
    top_left, bottom_right = other_corners(bottom_left, top_right)
    lines += [[bottom_left, top_left]]
    lines += [[top_left, top_right]]
    lines += [[bottom_left, bottom_right]]
    lines += [[top_right, bottom_right]]
    return lines




def paper_cut(list_boxes, lines=[], n=0): 
    if n == 0:
        return (list_boxes, lines)
    new_lines = lines
    new_boxes = []
    for bottom_left, top_right in list_boxes:
        if n % 2 == 0:
            mid_line =  vertical_split(bottom_left, top_right)
            new_lines += [mid_line]
        else:
            mid_line = horizontal_split(bottom_left, top_right)
            new_lines += [mid_line]
        new_bl, new_tr = mid_line
        new_boxes += [[bottom_left, new_tr]]
        new_boxes += [[new_bl, top_right]]
    return paper_cut(new_boxes, new_lines, n-1)


if __name__ == "__main__":
    n = int(sys.argv[1])
    lines = paper_cut([[(0,0), (1189,841)]],[], n)[1]
    lines += box_lines((0,0), (1189,841))
    lc = matplotlib.collections.LineCollection(lines)
    fig, ax = plt.subplots(1,1)
    ax.add_collection(lc,autolim=True)
    ax.set_xlim([0,1189+1])
    ax.set_ylim([-1,841+1])
    ax.set_title('Paper sizes A' + str(n) + ':'+ str(2**n) + ' pieces')
    ax.set_axis_off()
    plt.show()
