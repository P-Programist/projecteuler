# COULD NOT COPE

limit = 1000000
temp = 0

def memoize(f):
	cache = {}

	def memoizer(itter):
		if itter not in cache:
			cache[itter] = f(itter)
		return cache[itter]
	return memoizer
	
@memoize

def collatz_sequence(n):
	if n == 1:
		return True

	if n % 2 == 0:
		n /= 2
		# print(str(int(n)) + ' here we have print')
		return 1 + collatz_sequence(n)
	else:
		n = 3*n + 1
		# print(str(int(n)) + ' here we have print')
		return 1 + collatz_sequence(n)


for itter in range(2,limit+1):
	storage = collatz_sequence(itter)-1
	if storage > temp:
		temp = storage
		print('Number -> ' + str(itter) + ' has ' + str(temp) + ' divisors!')



