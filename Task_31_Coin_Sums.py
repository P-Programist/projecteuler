def coin_sum(pence):
	# We create a list of values that we are going to iterate through
	coins = [1,2,5,10,20,50,100,200]

	# Here we create a dictionary which will include every satisfied value
	ways = {n:1 for n in range(pence+1)}

	# We do not need to count 1 as the rest of values will be either satisfy or filled up by ones
	for coin in coins[1:]:
		for x in range(coin,pence+1):
			ways[x] += ways[x-coin]

	return ways[pence]

print(coin_sum(200))
