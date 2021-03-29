# Importing "permutatitions" function to find all ways of permutation
from itertools import permutations 

# Create a list with all possible permutations
pandit_list = tuple( permutations (i for i in range(10) ) )
# Provide a list with necessary divider.
divs_list = (2,3,5,7,11,13,17)


count = 0
# Just clean a tuple from commas and brakets to get clean digits without symbols
for itter in range(len(pandit_list)):
	pan_num = int(str(pandit_list[itter]).strip('()').replace(', ', ''))
	# Optimize range of finding by removing all EVEN numbers
	if pan_num % 2 != 0:
		digit = str(pan_num)

		# Split a number onto 3 digits in a row to see a property of substring
		num_list = [digit[three:three+3] for three in range(1, len(digit)-2)]

		# Devide each element of split-number to divider from "divs_list".
		res = sum([int(i) % j for i, j in zip(num_list, divs_list)] )
		if res == 0:
			count += int(digit)

print(count)





		

	
	


