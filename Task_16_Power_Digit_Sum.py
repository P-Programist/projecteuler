import logging
import time

today_date = time.strftime('%H' ':' '%M' ':' '%S ' '%Y' '-' '%m' '-' '%d' )

# print(dir(logging))
logging.basicConfig(filename = 'C:\\Users\geekg\OneDrive\Рабочий стол\Python Projects\Euler_project\Execution_logs.log', 
	level = logging.DEBUG)
logging_process = logging.getLogger()
logging_process.info('# Log created at ' + str(today_date))


def power_of_two(pwd):
	result = 2 ** pwd
	return result

def summation(result, temp = 0):
	for i in str(result):
		temp += int(i)
	return temp

print(summation(power_of_two(1000)))

