
def fifth_powers(p):

# This piece of shit works in the following way:
		# 1. We created approximately number of variables which will count all possible outcomes
		# 2. In case with 5-th power we need 6 variables
		# 3. We put each loop inside previous in order to power every number

	for a in range(0,10):
		for b in range(0,10):
			for c in range(0,10):
				for d in range(0,10):
					for e in range(0,10):
						for f in range(0,10):

							# The line below creates string version of number to compare it with generated
							string_ver = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
							num_rep = int(string_ver)

							# The line below sums all powered number
							sum_of_fifth = (a**p + b**p + c**p + d**p+e**p+f**p)

							# In case if string and generated sum of powers are equal it returns that number
							if sum_of_fifth == num_rep:
								yield sum_of_fifth

if __name__ == "__main__":
	sums = [i for i in fifth_powers(5) if i > 1]
	# print(sums)
	print(sum(sums))


