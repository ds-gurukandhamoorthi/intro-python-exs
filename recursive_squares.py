from htree import lower_corners, upper_corners
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import argparse

def corners_single(center, width):
    return lower_corners(*center, width) + upper_corners(*center, width)

def corners(list_centers, width):
    res = []
    for center in list_centers:
        res += corners_single(center, width)
    return res


def add_width(centers, width):
    lst = []
    for center in centers:
        lst += [(center,width)]
    return lst

SCALE=1/2.2
def squares_of_order(list_centers=[(0.5,0.5)], squares_and_side=[], line_length=1.0, order=1):
    new_centers = corners(list_centers,line_length)
    if order <= 1:
        return (new_centers, add_width(list_centers,line_length))
    new_squares = add_width(list_centers, line_length)
    return squares_of_order(new_centers,  new_squares, line_length * SCALE , order -1)

def squares(list_centers=[(0.5,0.5)], squares_and_side=[], line_length=1.0, order=1):
    res = []
    for i in reversed(range(1,order+1)):
        res += squares_of_order(list_centers, squares_and_side, line_length, i)[1]
    return res

def squares_(list_centers=[(0.5,0.5)], squares_and_side=[], line_length=1.0, order=1, bitstring='0101'):
    new_centers = corners(list_centers, line_length)
    if order < 1:
        return (new_centers, squares_and_side)
    new_squares = add_width(list_centers, line_length)
    if order == 1:
        return (new_centers, new_squares)
    lesser_squares = squares_(new_centers,  add_width(list_centers,line_length), line_length * SCALE , order -1, bit_string)[1]
    all_squares = put_together(lesser_squares, new_squares, bit_string)
    return (new_centers, all_squares)

def squares__(list_centers=[(0.5,0.5)], squares_and_side=[], line_length=1.0, order=1, bit_string='0101'):
    res = squares_(list_centers, squares_and_side, line_length, order, bit_string)[1]
    return res

def put_together(lesser_squares, squares, bit_string):
    res = []
    nb_bits = len(bit_string)
    n = len(lesser_squares) // nb_bits
    for i,bit in enumerate(bit_string):
        if bit == '1':
            res += lesser_squares[i*n : (i+1)*n]
    res += squares
    for i,bit in enumerate(bit_string):
        if bit == '0':
            res += lesser_squares[i*n : (i+1)*n]
    return res

    
    





def transform_square(square):
    "Given center and width, it returns left_corner and width"
    center, width = square
    x,y = center
    half = width / 2
    return (x-half, y-half), width

def as_patches(squares_and_side):
    lst_squares = []
    for square in squares_and_side:
        left_bottom_corner, width = transform_square(square)
        lst_squares += [patches.Rectangle(left_bottom_corner, width, width, facecolor='gray', edgecolor='black')]
    return lst_squares


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw recursive squares')
    parser.add_argument('order', type=int, help='order')
    parser.add_argument('--bit-string', help='bit string to change order ex: 0011')
    args = parser.parse_args()
    order = args.order
    if args.bit_string is not None:
        bit_string = args.bit_string
    else:
        bit_string = '0000'
   
    squares_and_side = squares__([(0.5,0.5)],[],0.5,order,bit_string)
    # print(len(squares_and_side))

    # res1 = squares([(0.5,0.5)],[],0.5,1)
    # print(res1[0])
    # print(res1[1])
    # squares_and_side1 = res1[1]
    
    fig, ax = plt.subplots()
    for ptch in as_patches(squares_and_side):
        ax.add_patch(ptch)
    fig.savefig('recsquares.png', dpi=90)
    plt.show()

    #FIXME : some squares are hidden in an unpredictable manner


