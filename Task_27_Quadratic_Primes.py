#COULD NOT COPE
import math 

def is_prime(num, memoization = {2:2}):
	if num in memoization:
		return memoization[num]

	if num == 2:
		return True
	if num % 2 == 0:
		return False

	for divisor in range(3, int(math.sqrt(num)) ,2):
		if num % divisor == 0:
			memoization[num] = False
			return False
	memoization[num] = num
	return memoization[num]


def quadratic_primes(a, b):
	n = 0
	result = abs(n**2 + a*n + b)
	check_for_prime_properties = is_prime(result)

	while check_for_prime_properties:
		yield check_for_prime_properties
		n += 1
		result = abs(n**2 + a*n + b)
		check_for_prime_properties = is_prime(result)


if __name__ == "__main__":
	longest_prime_combination = (1,41,len([i for i in quadratic_primes(1,41)]))
	for a in range(-999, 1000):
		if is_prime(abs(a)) == False:
			continue
		for b in range(-1000, 1001):
			if is_prime(abs(b)) == False:	
				continue
			prime_list = [i for i in quadratic_primes(a,b)]
			if len(prime_list) > longest_prime_combination[2]:
				longest_prime_combination = (a,b,len(prime_list))

	# print (longest_prime_combination)
	print(longest_prime_combination[0] * longest_prime_combination[1])

