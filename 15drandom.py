import random
number = random.randint(1, 100)
attempts = 0  # count no of attempts to guess the number
guess = 0
attempts = 0
while attempts<3:
    guess = int(input('Guess a number between 1 and 100: '))
    attempts += 1
    if guess == number:
        print('Congratulations! You used', attempts, 'attempts!')
        break
    elif guess < number:
        print('Go higher!')
    else:
        print('Go lower!')
else:
    print('The number is ',number)