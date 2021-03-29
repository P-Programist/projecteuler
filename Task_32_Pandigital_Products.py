
def pandigital_products(num):

	# We create a list with a range of numbers which we should compare
	range_of_numbers = ['1','2','3','4','5','6','7','8','9']
	filter_for_repeated = set()

	for x in range(num):
		for y in range(200):
			product = x * y

			# We put multiple/multiplier/product in one string for the following convertation
			string_ver = x,y,product

			# We delete commas,breakets,spaces from each string in order to insert in the list
			int_ver = list(str(string_ver).replace(', ', '').strip('()'))

			# We sort every list for comparison it with original one
			int_ver.sort()

			# If sorted list has exactly one number in itself it will be counted as satisfied case
			if int_ver == range_of_numbers:
				filter_for_repeated.add(product)
	return sum(filter_for_repeated)#, filter_for_repeated

if __name__ == "__main__":	
	print(pandigital_products(2000))