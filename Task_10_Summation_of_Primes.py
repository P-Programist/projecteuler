#Find the sum of all the primes below two million.
import math

temp_set = set()

print(2)

def summation_of_primes(prime):
	if prime > 2:
		for n in range(3,int(math.sqrt(prime)+1),2):
			if prime % n == 0:
				return False
		else: 
			if prime % 2 != 0:
				temp_set.add(prime)
				return prime


for n in range(2000):
	if summation_of_primes(n):
		print(summation_of_primes(n))

print(sum(temp_set)+2)



