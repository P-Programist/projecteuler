# Created an empty var for concatination
string = ''

# Add every number to the string variable
for i in range(0,1000001):
	string += str(i)



result = int(string[1]) # Initial value the first index of a string

# Multiply every number under the index on result variable
for p in range(1,7):
	index = pow(10,p)
	result *= int(string[index])

print(result)

