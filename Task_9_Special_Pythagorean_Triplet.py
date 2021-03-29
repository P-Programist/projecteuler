# COULD NOT COPE
import math

def pythagorean_triples(num):

	# sum_of_triples = int(input('Type the a number and let\'s see if there are triples for it: \n' ))
	if num % 2 == 0:
		for a in range (1, num+1):
			for b in range (1, num+1):
				if a > b:
					continue
				if a + b + (a**2 + b**2)**0.5 == num:
					return (a,b,int((a**2 + b**2)**0.5), a*b*int((a**2 + b**2)**0.5))
		else: return False

	if num % 2 != 0:
		triple2 = math.floor((num**2)/2)
		triple3 = math.ceil((num**2)/2)
		return(int(num), triple2, triple3)


print(pythagorean_triples(int(input('Type a number and let\'s see if there are triples for it: \n' ))))
