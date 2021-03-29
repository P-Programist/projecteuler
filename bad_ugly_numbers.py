import math
def isdisprime(factor):
    if factor == 2:
        return True

    if factor > 2 and factor % 2 == 0:
        return False

    for is_factor in range(3, int(math.sqrt(factor)), 2):
        if factor % is_factor == 0:
            return False
    return True

str_ = '1'
const = 10

num_of_test = int(input())

for test in range(num_of_test):
    input_ = int(input())

    if input_ == 1:
        print(-1)

    elif input_ == 2:
        print(23)

    else:
        for num in range(int(str(input_)*3), const ** input_):
            if isdisprime(num):
                print(num)
                break



