# COULD NOT COPE 
import logging
import time
import num2words

today_date = time.strftime('%H' ':' '%M' ':' '%S ' '%Y' '-' '%m' '-' '%d' )

# print(dir(logging))
logging.basicConfig(filename = "C:\\Users\geekg\OneDrive\Рабочий стол\Python Projects\Euler_project\\Number_letter_counts.log", 
	level = logging.DEBUG,
	filemode = 'w')
logging_process = logging.getLogger()
logging_process.info('# Log created at ' + str(today_date))

# logging_process.warning('Hey! Check the syntax, something went wrong!')

# one_to_ten = [
# 'one',
# 'two',
# 'three',
# 'four',
# 'five',
# 'six',
# 'seven',
# 'eight',
# 'nine',
# 'ten'
# ]

# ten_to_nineteen = [
# 'eleven',
# 'twelve',
# 'thirteen',
# 'fourteen',
# 'fifteen',
# 'sixteen',
# 'seventeen',
# 'eighteen',
# 'nineteen'
# ]

# twenty_to_hundred = [
# 'twenty',
# 'thirty',
# 'forty',
# 'fifty',
# 'sixty',
# 'seventy',
# 'eighty',
# 'ninety',
# 'hundredand'
# ]

# thousand = 'thousand'

# def counting_stars():
# 	temp = 11

# 	for units in range(len(one_to_ten)):
# 		# print(one_to_ten[units], len(one_to_ten[units]))
# 		temp += len(one_to_ten[units])
# 	# print()

# 	for units_of_ten in range(len(ten_to_nineteen)):
# 		# print(ten_to_nineteen[units_of_ten], len(ten_to_nineteen[units_of_ten]))
# 		temp += len(ten_to_nineteen[units_of_ten])
# 	# print()

# 	for decades in range(len(twenty_to_hundred)-1):
# 		# print(twenty_to_hundred[decades], len(twenty_to_hundred[decades]))
# 		temp += len(twenty_to_hundred[decades])

# 		for units in range(len(one_to_ten)-1):
# 			# print(twenty_to_hundred[decades],one_to_ten[units], len(twenty_to_hundred[decades]+one_to_ten[units]))
# 			temp += len(twenty_to_hundred[decades]+one_to_ten[units])

# 		if decades == 7:
# 			for units_1 in range(len(one_to_ten)-1):
# 				# print(one_to_ten[units_1], twenty_to_hundred[-1], len(one_to_ten[units_1] + twenty_to_hundred[-1]))
# 				temp += len(one_to_ten[units_1] + twenty_to_hundred[-1])

# 				for units in range(len(one_to_ten)-1):
# 					# print(one_to_ten[units_1], twenty_to_hundred[-1], one_to_ten[units], len(one_to_ten[units_1] + twenty_to_hundred[-1] + one_to_ten[units]))
# 					temp += len(one_to_ten[units_1] + twenty_to_hundred[-1] + one_to_ten[units])

# 				for units_of_ten in range(len(ten_to_nineteen)):
# 					# print(one_to_ten[units_1], twenty_to_hundred[-1],ten_to_nineteen[units_of_ten], len(one_to_ten[units_1] + twenty_to_hundred[-1] + ten_to_nineteen[units_of_ten]))
# 					temp += len(one_to_ten[units_1] + twenty_to_hundred[-1] + ten_to_nineteen[units_of_ten])

# 				for decades in range(len(twenty_to_hundred)-1):
# 					# print(one_to_ten[units_1], twenty_to_hundred[-1], twenty_to_hundred[decades], len(one_to_ten[units_1] + twenty_to_hundred[-1] + twenty_to_hundred[decades]))
# 					temp += len(one_to_ten[units_1] + twenty_to_hundred[-1] + twenty_to_hundred[decades])

# 					for units in range(len(one_to_ten)-1):
# 						# print(one_to_ten[units_1], twenty_to_hundred[-1],twenty_to_hundred[decades], one_to_ten[units], len(one_to_ten[units_1] + twenty_to_hundred[-1] + twenty_to_hundred[decades] + one_to_ten[units]))
# 						temp += len(one_to_ten[units_1] + twenty_to_hundred[-1] + twenty_to_hundred[decades] + one_to_ten[units])
# 	return temp

# print(counting_stars())


def counting_letters(number):

	return sum(1 for l in num2words.num2words(number) if l.isalpha())

print(sum(counting_letters(i) for i in range(1,1001)))

