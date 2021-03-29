limit = 100000

triangular_nums = [int(t*(t+1)/2) for t in range(1,limit)]
pentagonal_nums = [int(p*(3*p-1)/2) for p in range(1,limit)]
hexagonal_nums =  [int(h*(2*h-1)) for h in range(1,limit)]


for tph in triangular_nums:
	if tph in pentagonal_nums:
		if tph in hexagonal_nums:
			print(tph)

