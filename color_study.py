import matplotlib.pyplot as plt
import matplotlib.patches as patches
from geomutils import add_coords
from colorutils import as_matplotlib_color, rand_color
from albers_squares import albers_square



if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax.set_xlim(0,16)
    ax.set_ylim(0,16)
    for i in range(16):
        for j in range(16):
            c1 = (255-j*16,255-j*16,255)
            c2 = (i*16,i*16,i*16)
            for ptch in albers_square(c1,c2,(i,j), 1):
                ax.add_patch(ptch)
    plt.show()
