import sys
import random
def rumor_experiment(n):
    people = list(range(n))
    heard = [False] * (n)
    rumorAbout = random.randrange(n)
    rumourSayer = random_element(people,[rumorAbout])
    heard[rumourSayer] = True
    prev = -1
    while True:
        rumourReceiver = random_element(people, [rumorAbout, rumourSayer, prev])
        if heard[rumourReceiver]:
            return heard.count(True)
        heard[rumourReceiver] = True
        prev = rumourSayer
        rumourSayer = rumourReceiver


def random_element(array, avoidThese):
    if len(avoidThese)>=len(array):
        print("Error in randomElement(): Too many elements to avoid")
        return
    while True:
        elem = random.sample(array,1)[0]
        if elem not in avoidThese:
            return elem


if __name__ == "__main__":
    n = int(sys.argv[1])
    nbTrials = int(sys.argv[2])
    success = 0
    persons_hearing_rumour = 0
    for i in range(nbTrials):
        res = rumor_experiment(n)
        persons_hearing_rumour += res
        if res == n-1:
            success += 1

    print(success/nbTrials, persons_hearing_rumour/nbTrials)


        
