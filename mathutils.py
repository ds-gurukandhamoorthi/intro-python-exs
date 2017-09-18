import math

def avg(array):
    return sum(array)/len(array)

def variance(array):
    m = avg(array)
    totalSquared = 0
    for val in array:
        totalSquared += (val - m) **2
    return totalSquared / len(array)

def std_dev(array):
    return math.sqrt(variance(array))

def geom_mean(array):
    n = len(array)
    logtotal = 0
    for val in array:
        logtotal += math.log(val) #to avoid overflow
    return math.exp(logtotal/n)

def harm_mean(array):
    n = len(array)
    total = 0
    for val in array:
        total += 1/val
    return n/total



if __name__ == "__main__":
    print(std_dev([1,2,4,4,5]))
    print(harm_mean([1,4,4]))
    print(geom_mean([1,4,4]))
    print(geom_mean([25,9]))
    print(geom_mean([4,25,10]))
