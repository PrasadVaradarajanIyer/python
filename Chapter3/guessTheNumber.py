#This is a guess the number game

import random
secretNumber=random.randint(1, 20)
print('I am thinking of a number between 1 to 20.')

for guessesTaken in range(1,7):
	print('Guess my number')
	guess=int(input())
	
	if guess < secretNumber:
		print('The number guessed is lower than my number')
	elif guess > secretNumber:
		print('The number guessed is greater than my number')
	else:
		break	#This the condition when guess matches!


if guess == secretNumber:
	print ('Good Job you got my number in ' +str(guessesTaken) + ' guesses!')
else:
	print ('Nope, The number I was thinking of was ' + str(secretNumber))
