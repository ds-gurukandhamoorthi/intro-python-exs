import random

def guess():
    chosen = random.randrange(1,101)
    n = -1
    steps = 0
    while n != chosen:
        n = int(input("Guess the number : "))
        steps += 1
        if n < chosen:
            print("you have guessed low")
        elif n > chosen:
            print("you have guessed high")
        else:
            print("you have won in ", steps, " steps")

if __name__ == "__main__":
    guess()

