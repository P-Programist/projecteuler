import math

def is_prime(num):
	if num < 2:
		yield False
	if num == 2:
		yield 2
	if num > 2 and num % 2 == 0:
		yield False
	for x in range (3, int(math.sqrt(num))+1, 2): # This condition works ONLY with first two strings!	 
		if num % x == 0:
			yield False
	yield True



def get_factors(number):
	factors = []

	for i in range(2, int(number / 2) + 1):
		if number % i == 0:
			if next(is_prime(i)):
				factors.append(i)
	yield factors




def collector(number, factors, limit=4):
	if len(factors) < limit:
		return False

	count = 1
	for f in factors:
		count *= f
		if count > number:
			return False
		elif count == number or count * 2 == number:
			return True

	return False



for i in range(134000, 140000):
	n0 = i
	n1 = i + 1
	n2 = i + 2
	n3 = i + 3

	a0 = next(get_factors(n0))
	a1 = next(get_factors(n1))
	a2 = next(get_factors(n2))
	a3 = next(get_factors(n3))

	results = (collector(n0, a0), collector(n1, a1), collector(n2, a2))

	if all(results):
		print(n0)
		break

