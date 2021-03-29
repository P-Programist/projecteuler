# import math

# def difference(number, sum_of_squares = 0, sum_of_sum = 0):
# 	for squares in range(1,number + 1):
# 		sum_of_squares += (squares ** 2)
# 	for sum_ in range(1, number + 1):
# 		sum_of_sum += sum_
# 	result = (sum_of_sum ** 2) - sum_of_squares
# 	print('										The difference between square of sum ' + str(sum_of_sum ** 2) + ' and sum of squares ' + str(sum_of_squares) + ' = ' + str(result))
# difference(100)

# One string solution:
# print(sum([i for i in range(101)])**2-sum([i**2 for i in range(101)]))