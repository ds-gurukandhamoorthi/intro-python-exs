from diceSimulation import die
from bernoulli import count_integers
import matplotlib.pyplot as plt
from randomutils import oneOf

def sum_die(nb_trials):
    sums = [die() + die() for i in range(nb_trials)]
    return sums

def sicherman_die():
    die1 = (1,3,4,5,6,8)
    die2 = (1,2,2,3,3,4)
    return (oneOf(die1),oneOf(die2))

def sum_sicherman_die(nb_trials):
    sums = [sum(sicherman_die()) for i in range(nb_trials)]
    return sums


if __name__ == "__main__":
    plt.hist(sum_die(10000), alpha=0.7)
    plt.hist(sum_die(10000), alpha=0.7)
    plt.show()
