import math
import collections

def circular_primes(num):

	# The function below checks whether a number is prime
	def list_of_primes(lim):
		if lim > 2 and lim % 2 == 0:
			return False
		for x in range (3, int(math.sqrt(lim))+1, 2): # This conditions works ONLY with first two strings!	 
			if lim % x == 0:
				return False
		return True

	'''These 3 lines below take a number from the parameter and convert it into a "string" /
	/ and then create an object-version of this list for the following rotation'''
	list_ver = [i for i in str(num)]
	list_ver_obj = collections.deque(list_ver)
	rotated_numbers = []

	''' The loop below rotates the object version of string and append it to the list. 
	P.S. Before that it clears the object version from: "Commas, Breakets and Quotation Marks" '''
	for charp in range(len(list_ver)):
		list_ver_obj.rotate()
		result = int(str(list_ver_obj).strip('deque([\'\'\'])').replace('\', \'', ''))
		rotated_numbers.append(result)

	# The loop below checks if all values in list are True or not and return only those numbers that list had all True outputs
	for is_circular in rotated_numbers:
		if not list_of_primes(int(is_circular)):
			return False
	return num
	
# Here the code generates numbers from 3 to 1000000 with step of 2 to save time and resources
if __name__ == "__main__":
	numbers = [circular_primes(num) for num in range(3,1000000,2) if circular_primes(num)]
	numbers.insert(0,2)
	print(numbers)
	print(len(numbers))