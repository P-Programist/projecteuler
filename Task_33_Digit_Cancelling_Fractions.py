product = 1
for numerator in range(10,51):
	for denominator in range(50,101):
		if numerator % 10 == 0 and denominator % 10 == 0:
			continue
		else:
			str_num = str(numerator)
			str_den = str(denominator)
			initial_result = float(numerator/denominator)
			if int(str_den[1]) != 0:
				end_result = int(str_num[0])/int(str_den[1])

			if initial_result == end_result and str_num[0] != str_num[1] and str_num[1] == str_den[0]:
				print(str(numerator) + '/' + str(denominator) + '   ' + str(end_result))
				product *= end_result

print(int(product*10000))
