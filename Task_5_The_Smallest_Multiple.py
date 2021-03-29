# COULD NOT COPE 

import math 

def lcm(n): 
    ans = 1    
    for i in range(1, n + 1):
    	ans = (ans * i) / math.gcd(int(ans), i)
      
    return int(ans)

n = 20
print(lcm(n))

# Max Number for this interpreter is 218