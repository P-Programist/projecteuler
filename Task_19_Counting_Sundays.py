import datetime

def counting_Sundays():
	init_date = datetime.date(1899,12,31)
	final_date = datetime.date(2000,12,31)

	sundays = 0
	i = 0
	while i < 36890:
		i += 1
		result = (init_date + datetime.timedelta(days = i))
		init_date + datetime.timedelta(days = i)
		if i % 7 == 0:
			if i > 364:
				if str(result).endswith('01'):
					# print(result, 'Sunday')
					sundays += 1
	return sundays

print(counting_Sundays())