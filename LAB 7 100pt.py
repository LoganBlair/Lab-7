guessesTaken = 0
import random
rand = random.randint(0,50)
print('Well, '  ', I am thinking of a number between 0 and 50.')
while guessesTaken < 50:
    print('Take a guess.') 
    guess = raw_input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess < rand:
        print('Your guess is too low.') 
    if guess > rand:
        print('Your guess is too high.')
    if guess == rand:
        print 'You got it!'
