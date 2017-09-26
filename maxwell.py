import scipy.stats
from randomutils import maxwell
import matplotlib.pyplot as plt


if __name__ == "__main__":
    NB_TRIALS = 10000
    values = [maxwell(10) for i in range(NB_TRIALS)]
    plt.hist(values)
    # plt.show()

    plt.hist(scipy.stats.maxwell.rvs(size=NB_TRIALS,scale=10))
    plt.show()
