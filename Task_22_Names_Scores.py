# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

import os

alpha_list = ['A','B','C',
			'D','E','F',
			'G','H','I',
			'J','K','L',
			'M','N','O',
			'P','Q','R',
			'S','T','U',
			'V','W','X',
			'Y','Z']

count = 0
result = 0
file = open('p022_names.txt', 'r')

for lenght_of_list in range(5163):
	with open('p022_names.txt', 'r', encoding = 'UTF-8',) as names:
		for name in list(names):
			for letter in name.split('","')[lenght_of_list][:][:]:
				if letter in alpha_list:
					# print(letter, ' - ', alpha_list.index(letter)+1)
					count += (alpha_list.index(letter)+1)
			result += (lenght_of_list+1) * count
		# print(count)
		# print(lenght_of_list+1)
		# print(result)
	
	count = 0
			
file.close()
print(result)