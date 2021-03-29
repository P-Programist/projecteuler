import math

def if_prime(num):
	if num < 2:
		return False
	if num == 2:
		return num
	if num > 2 and num % 2 == 0:
		return False
	for x in range (3, int(math.sqrt(num))+1, 2): # This conditions works ONLY with first two strings!	 
		if num % x == 0:
			return False
	return num


def if_pandigital_and_prime(num):
	if num % 2 == 0:
		return False

	if if_prime(num):
		len_of_num_for_temp = [d for d in range(1,len(str(num))+1)]
		template = int(str(len_of_num_for_temp).strip("[]").replace(", ", ""))

		num_in_list = [s for s in str(num)]
		num_in_list.sort()
		str_ver_of_num = int(str(num_in_list).strip("[\'\']").replace("\', '", ""))
		
		if str_ver_of_num == template:
			return num

		else:
			return False

	else:
		return False

count = 0
for i in range(3,987654322,2):
	if if_pandigital_and_prime(i) > count:
		count = if_pandigital_and_prime(i)
		print(count)