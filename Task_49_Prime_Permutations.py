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


def is_permutations(a, b, c):
	a_s = list(str(a))
	b_s = list(str(b))
	c_s = list(str(c))

	a_s.sort()
	b_s.sort()
	c_s.sort()

	n1 = ''.join(a_s)
	n2 = ''.join(b_s)
	n3 = ''.join(c_s)

	if n1 == n2 == n3:
		return True


primes = (
	i for i in range(1000, 10000) 
	if next(is_prime(i)) 
	and next(is_prime(i + 3330)) 
	and next(is_prime(i + 3330 * 2))
	and is_permutations(i, i + 3330, i + 3330 * 2)
)

next(primes)

result = ''
number = next(primes)

for n in range(3):
	result += str(number + n * 3330)

print(result)