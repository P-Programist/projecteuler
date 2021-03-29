import math
from formulas import primes_finder

def truncatable_primes(num):
	
	str_version_of_num = str(num)
	while len(str_version_of_num):

		if not primes_finder(int(str_version_of_num)):
			return False

		str_version_of_num = str_version_of_num[1:]


	str_version_of_num = str(num)
	while len(str_version_of_num):

		if not primes_finder(int(str_version_of_num)):
			return False

		str_version_of_num = str_version_of_num[:-1]

	return num

if __name__ == "__main__":

	truncatable_primes_list = []
	digit = 11

	while len(truncatable_primes_list) < 11:

		if truncatable_primes(digit):
			truncatable_primes_list.append(digit)
		digit += 2

	print(truncatable_primes_list)
	print(sum(truncatable_primes_list))

