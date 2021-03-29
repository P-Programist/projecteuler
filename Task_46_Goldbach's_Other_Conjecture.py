import math

# The function below defines whether the number is a prime
def is_prime(num):
	if num < 2:
		yield False
	if num == 2:
		yield 2
	if num > 2 and num % 2 == 0:
		yield False
	for x in range (3, int(math.sqrt(num))+1, 2): # This conditions works ONLY with first two strings!	 
		if num % x == 0:
			yield False
	yield True


'''
The function below, defines if the formula 
(prime + 2 * "var: ** 2) 
is applied to a number which will be considered as Golbach's Conjecture'''

def is_goldbach(num):
	for x_range in range(3, num+1, 2):
		for mult in range(1,int(math.sqrt(num))):
			if next(is_prime(x_range )):
				conject_num = x_range + 2 * mult ** 2
				if conject_num == num:
					return conject_num
	return False

for i in range(33,5778,4):
	if not next(is_prime(i)):
		if not is_goldbach(i):
			print(i)
