import random

print("Number Guessing Game")
num = random.randint(1,9)
chances= 0
    
while chances < 5:
    guess= int(input(f'Guess a number between 1 and 9:'))
    if guess < num:
        print("Sorry, guess again. Too low.")
    elif guess > num:
        print("Sorry, guess again. Too high.")
    else:
        print("Yay! Congratulations, you guessed the right number", num)

    chances += 1

if not chances< 5:
    print("YOU LOST!! The number is", num)




