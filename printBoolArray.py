import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matrixutils import dimen

def get_shapes_for(matr, true_color='white', false_color='black'):
    lst_squares = []
    n = len(matr)
    for i, row in enumerate(matr):
        for j, cell in enumerate(row):
            (x,y) = j, n -i -1
            color = true_color if cell == True else false_color
            lst_squares += [patches.Rectangle((x,y), 1, 1, facecolor=color)]
    return lst_squares

def get_shapes_for_ragged(matr, true_color='green', false_color='red'):
    lst_squares = []
    n = len(matr)
    for i, row in enumerate(matr):
        for j, cell in enumerate(row):
            (x,y) = j, n -i -1
            color = true_color if cell == True else false_color
            lst_squares += [patches.Rectangle((x,y), 1, 1, facecolor=color)]
    return lst_squares

def show_ragged_matr(matr, true_color='green', false_color = 'red'):
    sqrs = get_shapes_for_ragged(matr, true_color, false_color)
    nr = dimen(matr)[0]
    nc = max((len(row) for row in matr))
    fig, ax = plt.subplots()
    ax.set_xlim(0,nc)
    ax.set_ylim(0,nr)
    for ptch in sqrs:
        ax.add_patch(ptch)
    plt.show()

def showMatrix(matr, true_color='white', false_color='black'):
    sqrs = get_shapes_for(matr, true_color, false_color)
    nr, nc = dimen(matr)
    fig, ax = plt.subplots()
    ax.set_xlim(0,nc)
    ax.set_ylim(0,nr)
    for ptch in sqrs:
        ax.add_patch(ptch)
    plt.show()
    



def printMatrix(matr, trueSymbol='*', falseSymbol=' '):
    for i in range(len(matr)):
        print(i+1,end='')
    print('')
    i=0
    for row in matr:
        for v in row:
            toprint = trueSymbol if v else falseSymbol
            print(toprint, end='')
        print(i+1)
        i+=1

a = [[True, True, True, True],
        [False, False, True, True],
        [True, False, True, False],
        [False, False, False, False]]

ragged = [[True],
        [False,True],
       [True,False,True] ]
if __name__ == "__main__":
    printMatrix(a)
    showMatrix(a)
    show_ragged_matr(ragged)
