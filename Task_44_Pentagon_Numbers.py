pentagon_nums = [int(num*(3*num - 1)/2) for num in range(1,10000)]

for a in pentagon_nums:
	for b in pentagon_nums:
		if a > b:
			continue
		if a+b in pentagon_nums:
			if b-a in pentagon_nums:
				print(str(a),str(b), str(a+b),str(b-a))


