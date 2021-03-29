# COULD NOT COPE
# for horizontal_pairs in range(0,int(len(grid_list[0])-10),3):
# 		# grid_list[0][n:n+3] Key Moment
# 		# "end = '' " allows to apply integer convertation
# 		temp_line.append(grid_list[0][int(horizontal_pairs):int(horizontal_pairs+11)].split())
import math

grid = [

	[8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8],
	[49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0],
	[81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65],
	[52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91],
	[22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],
	[24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50],
	[32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],
	[67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21],
	[24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],
	[21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95],
	[78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92],
	[16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57],
	[86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58],
	[19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40],
	[4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66],
	[88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69],
	[4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36],
	[20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16],
	[20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54],
	[1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48]
																	]


length = 4

def horizontal_searching_algorithm(grid, length):
	result = 0

	for line in grid:
		for shift in range(0, len(line) - length):
			# Key moment is HERE, as it combines 4 elements out of line in itself
			block_of_four = line[shift : shift + length]
			temp = 1

			for i in block_of_four:
				temp *= i

			if temp > result:
				result = temp

	return result	


def vertical_searching_algorithm(grid, length):
	result = 0
	length_of_grid = len(grid)

	for place in range(0, length_of_grid):
		# We need to make range which checks ONLY one element in line, so the len of line "-"  something "=" 1
		for zero_index_of_each_line in range(0, length_of_grid - length+1):
			# This line takes only first(0) index of line
			substring = grid [zero_index_of_each_line:zero_index_of_each_line+length]
			temp = 1

			for first_indexes in substring:
				# Without including "place" as an index the algorithm will not move from left to the right
				temp *= first_indexes[place]

				if temp > result:
					result = temp

	return result


def diagonal_down_searching_algorithm(grid, length):
	result = 0
	size = len(grid)

	# This lines do not allow to exceed the range of len of line
	for row_index in range(0, size - length+1):
		for column_index in range(0, size - length+1):
			temp = 1

			for itter in range(0, length):
				# This slice allows us to move diagonaly (0:0, 1:1; 1:1, 2:2)
				block_of_four = grid[row_index+itter][column_index+itter]
				temp *= block_of_four

			if temp > result:
				result = temp

	return result


def diagonal_up_searching_algorithm(grid, length):
	result = 0
	size = len(grid)

	for row_index in range(0, size - length+1):
		for column_index in range(0, size - length+1):
			temp = 1
			for itter in range(0, length):
				block_of_four = grid[row_index-itter][column_index+itter]
				temp *= block_of_four
			if temp > result:
				result = temp

	return result


array_of_max = (
horizontal_searching_algorithm(grid, length),
vertical_searching_algorithm(grid, length),
diagonal_down_searching_algorithm(grid, length),
diagonal_up_searching_algorithm(grid, length)
				)

print(array_of_max)
	

# nums = """ 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48 """.split()

# nums_list = [int(x) for x in nums] 

# def get_nums(l:list): 
# 	result = [] 
# 	for x in l: 
# 		result.append(nums_list[x]) 
# 	return result 

# def pow_list(l:list): 
# 	result = 1 
# 	for x in l: 
# 		result *= x 
# 	return result 

# def max_line(): 
# 	m = 0 
# 	for x in range(20): 
# 		for y in range(20): 
# 			if x < 17: 
# 				p = pow_list(get_nums([0+x+y*20,1+x+y*20,2+x+y*20,3+x+y*20])) 
# 				m = p if p > m else m

# 			if y < 17: 
# 				p = pow_list(get_nums([0+x+y*20,20+x+y*20,40+x+y*20,60+x+y*20])) 
# 				m = p if p > m else m

# 			if x < 17 and y < 17: 
# 				p = pow_list(get_nums([0+x+y*20,21+x+y*20,42+x+y*20,63+x+y*20])) 
# 				m = p if p > m else m 

# 			if x < 17 and y > 2: 
# 				p = pow_list(get_nums([x+y*20,x-19+y*20,x-38+y*20,x-57+y*20])) 
# 				m = p if p > m else m 
# 	return m 

# print(max_line())