import random
designated_number = random.randint(0,100)
number=int(input('Enter a number between 0 and 100: '))
while designated_number != number :
	if number > designated_number:
		print('Too large!')
	else:
		print('Too small!')
	number=input('Please enter another number.')
	number=int(number)
print(f'Congratulation! The number is {designated_number}!')