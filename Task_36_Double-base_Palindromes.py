# We define a function with input of range to search palindromes
def palindromes(num):

	# The list below will accumulate all values that satisfy our conditions
	temp = []
	for bins in range(1,num+1):
		
		# We convert binary representation of a number to the string format and slice it after "0b" symbols
		str_format_of_bin_format = str(bin(bins))[2:]
		if str(bins) == str(bins)[::-1]:
			if str_format_of_bin_format == str_format_of_bin_format[::-1]:
				# print(str_format_of_bin_format, bins)
				temp.append(bins)

	return(sum(temp))

print(palindromes(1000000))