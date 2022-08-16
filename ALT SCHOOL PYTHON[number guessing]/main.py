import random

print('Hello Welcome to Dolapo Guessing game')
print('Guess number from the range of 1 - 16')
score = 10
print('Your score: ', score)
while True:
    user_guess = input('Guess the number: ')
    user_guess = int(user_guess)
    guessed_num = 'Guessed number: ', random.randrange(1, 16)

    if(user_guess != guessed_num):
        print(guessed_num)
        score -= 1
        print('Your score: ', score)
    elif(user_guess == guessed_num):
        print(guessed_num)
        score += 1
        print('Your score: ', score)
    if(user_guess >= 17):
        print('User dont use number above the range')
