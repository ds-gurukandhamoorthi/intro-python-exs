from percolation import experiment
from Data import Data
if __name__ == "__main__":
    MAX = 25
    PROB = 0.5
    nb_exp = 10
    dt = Data(MAX)
    for i in range(2,MAX):
        res = experiment(i, i, PROB, nb_exp)
        dt += (i, res/nb_exp)
    dt.plot()


        

