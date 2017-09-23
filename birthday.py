import argparse
import sys
import random

DAYS_PER_YEAR=365

def random_birthday():
    return random.randrange(0,DAYS_PER_YEAR)

def birthdayExperiment():
    peopleWithBirthday = [False] * DAYS_PER_YEAR
    nb_persons = 0
    while True:
        nb_persons += 1
        person = random_birthday()
        if peopleWithBirthday[person]:
            return nb_persons
        peopleWithBirthday[person] = True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Estimate chance of two people having same birthday')
    parser.add_argument('nb_trials', type=int, help='number of times the experiment should be run')
    args = parser.parse_args()
    nb_trials = args.nb_trials
    nb_persons = 0
    for i in range(nb_trials):
        nb_persons += birthdayExperiment()
    print(nb_persons/nb_trials)

