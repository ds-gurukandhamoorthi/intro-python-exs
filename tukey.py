import matplotlib.pyplot as plt
from ioutils import read_floats

if __name__ == "__main__":
    array = read_floats()
    plt.boxplot(array)
    plt.show()
    
