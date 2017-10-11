import pandas as pd
import matplotlib.pyplot as plt
if __name__ == "__main__":
    filename = '../djia.csv'
    df = pd.read_csv(filename)
    plt.plot(df['Close'])
    plt.show()
