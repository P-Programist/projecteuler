# import sys
# import math

# def find_palindrome(palindrome_list = set(), biggest_palindrome = set(), result = ''):
# 	for is_palindrome in range(10000, 998002):
# 		is_palindrome = str(is_palindrome)
# 		if is_palindrome[:3] == is_palindrome[:2:-1]:
# 			palindrome_list.add(is_palindrome)
			
# 	for factor in range(100, 1000):
# 		for palindrome in palindrome_list: 
# 			if int(palindrome) % factor == 0:
# 				result = int(palindrome) / int(factor)

# 				if len(str(int(result))) == 3:
# 					biggest_palindrome.add(palindrome)

# 	print(max(biggest_palindrome))

# find_palindrome()