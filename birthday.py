import sys
import random

DAYS_PER_YEAR

def birthdayExperiment():
    peopleWithBirthday = [False] * DAYS_PER_YEAR
    nb_persons = 0
    while True:
        nb_persons += 1
        person = random.randrange(0,365)
        if peopleWithBirthday[person]:
            return nb_persons
        peopleWithBirthday[person] = True


if __name__ == "__main__":
    nb_trials = int(sys.argv[1])
    nb_persons = 0
    for i in range(nb_trials):
        nb_persons += birthdayExperiment()


    print(nb_persons/nb_trials)

