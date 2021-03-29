
template = [str(n) for n in range(1,10)]

def pandigital(num):
	temp = ''
	for i in range(1,10):
		temp += str(num*i)
		if len(temp) > 8:
			break
	return temp

def max_pandigital(list_of_pandig = []):

	for i in range(2,9328):
		number = list(pandigital(i))
		int_number = int(str(number).strip('[\'\']').replace('\', \'', ''))
		
		number.sort()
		if number == template:
			# print(i)
			list_of_pandig.append(int_number)
	return(max(list_of_pandig))


if __name__ == "__main__":
	print(max_pandigital())