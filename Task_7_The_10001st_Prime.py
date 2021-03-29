# COULD NOT COPE

# import time
import math

def list_of_primes(lim):
	if lim == 2:
		return True

	if lim > 2 and lim % 2 == 0:
		return False

	for x in range (3, int(math.sqrt(lim))+1, 2): # This conditions works ONLY with first two strings!	 
		if lim % x == 0:
			return False
			
	return True


# print(list_of_primes(13))
# set_of_primes = set()
# i = 2
# limit = 10001

# while len(set_of_primes) < limit: # This condition controls how much, primes will be shown!
# 	if list_of_primes(i):
# 		set_of_primes.add(i)
# 	i += 1

# print(max(set_of_primes))
# ALL PRIMES GREATER THAN 3 CAN BE WRITTEN IN THE FORM  6k + or - 1
# ANY NUMBER (10, 33, 51, ...) CAN HAVE ONLY ONE PRIMEFACTOR GREATER THAN sqrt(n).