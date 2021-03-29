import math
import time

def is_prime(num):
	if num < 2:
		return False
	if num == 2:
		return 2
	if num > 2 and num % 2 == 0:
		return False
	for x in range (3, int(math.sqrt(num))+1, 2): # This condition works ONLY with first two strings!	 
		if num % x == 0:
			return False
	return True

limit = 1000000

primes = [i for i in range(2, limit+1) if is_prime(i)]

at_max = int(math.sqrt(limit))
shift_range = int(math.sqrt(limit)) - int(math.sqrt(int(math.sqrt(limit))))

max_primes = 0
max_prime = 0


for q in range(shift_range):
	for p in range(at_max):
		numbers = primes[p: p + q]
		if sum(numbers) >= limit:
			break
		elif sum(numbers) in primes and len(numbers) > max_primes:
			max_primes = len(numbers)
			max_prime = sum(numbers)

print(max_prime)