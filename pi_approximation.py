"""Approximating p using random numbers"""

from time import time
from random import randint
from math import sqrt, pi, gcd
import matplotlib.pyplot as plt

TRIALS = 35000000
LIMIT = 1000000000000000

T1 = time()

RAND_NUMS = [1 for trial in range(1, TRIALS + 1) if gcd(randint(1, LIMIT), randint(1, LIMIT)) == 1]
X = [sqrt(6 / (num / TRIALS)) for num in range(1, len(RAND_NUMS) + 1)]
Y = [i for i in range(1, len(RAND_NUMS)+1)]

PI_APPROXIMATION = sqrt(6 / (sum(RAND_NUMS) / TRIALS))

T2 = time()

plt.title("P-approximation " + str(PI_APPROXIMATION) + "\n" + "Time: " \
        + str(T2 - T1) + "\n" + "Error: " + str((1-PI_APPROXIMATION/pi)*100))
        
plt.plot(Y, X)
plt.hlines(pi, 0, len(RAND_NUMS))
plt.ylabel('Approximation')
plt.xlabel('TRIALS')
plt.show()
