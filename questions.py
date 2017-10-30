import random
MAX = 100

number = random.randrange(MAX)
guess = None
steps = 0
while guess is None or guess != number:
    steps += 1
    guess = int(input('Enter your guess: '))
    if guess > number:
        print('the number to guess is smaller')
    elif guess < number:
        print('the number to guess is higher')
print('you have found the number in ' , steps, ' steps')
