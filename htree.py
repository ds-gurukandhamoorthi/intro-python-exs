import matplotlib.pyplot as plt
import matplotlib.collections

def htree_lines( x,y, line_length, order):
    points = []
    half = line_length /2
    points += [[(x-half, y), (x+half, y)]]
    points += [[(x-half, y-half), (x-half, y+half)]]
    points += [[(x+half, y-half), (x+half, y+half)]]
    return points

if __name__ == "__main__":
    plt.axis('equal')
    h = htree_lines(1,1,2,1)
    lc = matplotlib.collections.LineCollection(h)
    fig, ax = plt.subplots()
    ax.add_collection(lc)

    # for line in h:
    #     for frm, to in line:
    #         lc = 
    #         print(0)
    #         # plt.plot(frm, to, 'k')
    plt.plot((0,0), (1,1))
    plt.show()
    print(h)
