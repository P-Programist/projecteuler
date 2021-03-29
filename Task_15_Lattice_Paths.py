# COULD NOT COPE
import math 

def lattice_paths(size):
	result = math.factorial(2 * size) / (math.factorial(size) ** 2)
	return int(result)

# print(lattice_paths(20))

def pathes(start_point_x, start_point_y, end_point_x, end_point_y):

	if start_point_x == end_point_x and start_point_y == end_point_y:
		return 1

	if start_point_x == end_point_x:
		return pathes(start_point_x, start_point_y + 1, end_point_x, end_point_y)

	if start_point_y == end_point_y:
		return pathes(start_point_x + 1, start_point_y, end_point_x, end_point_y)

	return pathes(start_point_x + 1, start_point_y, end_point_x, end_point_y) + pathes(start_point_x, start_point_y + 1, end_point_x, end_point_y)

print (pathes(0,0,20,20))	