import math

# The function below check whether a number is prime...
def primes_finder(lim, cache = {}):
	if lim in cache:
		return cache[lim]
	else:

		if lim == 2:
			return lim
		if lim < 2:
			return False
		if lim > 2 and lim % 2 == 0:
			return False
		for x in range (3, int(math.sqrt(lim))+1, 2): # This conditions works ONLY with first two strings!	 
			if lim % x == 0:
				return False

		cache[lim] = lim
		return lim