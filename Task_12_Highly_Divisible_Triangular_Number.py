# COULD NOT COPE
import math
def triangular_number(i = 0):
	starting_point = 0

	while True:
		i += 1
		starting_point += i
		count = 1

		for divisors in range(1,int(starting_point/2)+1):
			if starting_point % divisors == 0:
				count += 1
		if count > 500:
			return starting_point	

print(triangular_number())