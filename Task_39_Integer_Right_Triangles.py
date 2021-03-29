import math

# The function which finds pythagorean_triples
def pythagorean_triples(num):
	count = 0
	if num % 2 == 0:
		for a in range (1, num+1):
			for b in range (1, num+1):
				if a > b:
					continue
				if a + b + (a**2 + b**2)**0.5 == num:
					# print(a,b,int((a**2 + b**2)**0.5))
					count += 1
		return count

	# In case if number is ODD we apply second property of triples
	if num % 2 != 0:
		triple2 = math.floor((num**2)/2)
		triple3 = math.ceil((num**2)/2)
		# print(int(num), triple2, triple3)
		count += 1
		return count


# A loop which goes through 1000 number to find a number which has the most number of triples in this range
num_of_triplets = 0

for number in range(1001):
	if pythagorean_triples(number) > num_of_triplets:
		num_of_triplets = pythagorean_triples(number)
		print("Number: " + str(number), num_of_triplets)

