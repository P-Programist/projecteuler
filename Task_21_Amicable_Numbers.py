import math

lenght = 10000
sum_of_amicables = 0

def amicable_numbers(num):
	temp1 = 0
	temp2 = 0
	
	for check_point in range(1,int(num/2)+1):
		if num % check_point == 0:
			temp1 += check_point

	for check_point_2 in range(1,int(temp1/2)+1):
		if temp1 % check_point_2 == 0:
			temp2 += check_point_2

	if num == temp2:
		if temp1 != temp2:
			return temp2



for i in range(lenght+1):
	if amicable_numbers(i) != None:
		# print (amicable_numbers(i))
		sum_of_amicables += amicable_numbers(i)

print(sum_of_amicables)