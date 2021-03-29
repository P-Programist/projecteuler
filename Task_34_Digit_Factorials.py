# We imported factorial method from math module for automatic summation
from math import factorial

def self_factorial(num):

	# We take every num as a string in order to split every number in it
	str_ver_num = str(num)
	sum_of_factorials = 0

	for index in range(len(str_ver_num)):
		
		# We add result of factorialization into variable to compare it with original one
		sum_of_factorials += factorial(int(str_ver_num[index]))
		if num > 2 and num == sum_of_factorials:
			return num


if __name__ == "__main__":
	result = [self_factorial(i) for i in range(3,100000) if self_factorial(i) != None]

	print(sum(result))