#COULD NOT COPE

triangle = [
                            [75],
                          [95, 64],
                        [17, 47, 82],
                      [18, 35, 87, 10],
                    [20, 4, 82, 47, 65],
                   [19, 1, 23, 75, 3, 34],
                 [88, 2, 77, 73, 7, 63, 67],
			   [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
          [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
      [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [92, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
  [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
 [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]



i = 0
f_b_n = max(triangle[1])
f_b_n_i = triangle[1].index(f_b_n)
cur_big_ind = f_b_n_i
max_sum = max(triangle[0])

while i <= len(triangle)-2:

	n_b_i = max(triangle[i+1][cur_big_ind], triangle[i+1][cur_big_ind+1])
	cur_big_ind = triangle[i+1].index(n_b_i)
	max_sum += n_b_i
	i += 1

print(max_sum)


def greatest_path(index, rows):
	if len(rows) == 1:
		return max(rows[0][index], rows[0][index])
	print(greatest_path(index, rows[1:]), greatest_path(index + 1, rows[1:]) + rows[0][index])
	return max(greatest_path(index, rows[1:]), greatest_path(index + 1, rows[1:])) + rows[0][index]

print(greatest_path(0,triangle))