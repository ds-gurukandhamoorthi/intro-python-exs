import argparse
from gauss import pdf
import matplotlib.pyplot as plt

def plot_gaussian_same_mean(mean=0):
    for i in range(1,10):
        plt.plot([pdf(x, mean, i) for x in range(-100,101)])
    plt.show()

def plot_gaussian_same_std(std=1):
    for i in range(1,20,2):
        plt.plot([pdf(x, i, std) for x in range(-100,101)])
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Effect of chaning means or std-deviation on the Gaussian distribution curve')
    group=parser.add_mutually_exclusive_group()
    group.add_argument('--mean', type=int, help='vary stds', default=0)
    group.add_argument('--std', type=int, help='vary means', default=1)
    args = parser.parse_args()
    mean = args.mean
    std = args.std
    if mean:
        plot_gaussian_same_mean(mean)
    else:
        plot_gaussian_same_std(std)



