
def spiral_printing(size):
	side = 3
	i = 1
	yield (i)
	while i < size**2:
		for step in range(0,4):
			i += side - 1
			yield (i)
		side += 2

if __name__ == "__main__":
	temp = [i for i in spiral_printing(1001)]
	print(sum(temp))
































