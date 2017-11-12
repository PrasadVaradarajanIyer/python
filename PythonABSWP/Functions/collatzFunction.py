def collatz(inputNumber):
		if (inputNumber%2)==0:
			inputNumber=inputNumber/2
			return inputNumber
		elif (inputNumber%2)==1:
			inputNumber= 3*inputNumber+1
			return inputNumber
		else:
		 	print('Enter a valid whole number')

print('Enter a number greater than 1')
try:
	number=int(input())
	while number!=1:
		number=(collatz(number))
		print(number)
except NameError:
	print('Enter only numbers')
