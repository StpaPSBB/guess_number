from random import randint


number = randint(1, 100)
print(f"Game 'Guess number in range from 1 to 100'")

while True:
    #Asking user to guess a number
    guess = int(input("Guess a number: "))

    if guess == number:
        print('You Guessed!') #print the winning message
        break
    elif guess > number:
        print('Too much!') #print a hint
    elif guess < number:
        print('Too low!') #print a hint
