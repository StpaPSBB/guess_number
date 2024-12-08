from random import randint


number = randint(1, 100)

while True:
    guess = int(input("Guess a number: "))
    if guess == number:
        print('You Guessed!')
        break
    elif guess > number:
        print('Too much!')
    elif guess < number:
        print('Too low!')
