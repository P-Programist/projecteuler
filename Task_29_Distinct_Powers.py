a = 2
end = 101
powers = set()
while a < end:
	for b in range(2,end):
		powers.add(a**b)
	a += 1

print(len(powers))
