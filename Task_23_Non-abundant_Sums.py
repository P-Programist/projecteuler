# COULD NOT COPE
import math


def perfect_num(is_perfect):
    temp = 0
    for divisor in range(1,is_perfect):
        if is_perfect % divisor == 0: 
            temp += divisor
    return temp
        
sum_of_abundant = set()
set_of_non_abundant_sums = set()

# for i in range(1,28124):
    
#     if perfect_num(i) > i:
#         sum_of_abundant.add(i*2)

# for i2 in range(1,28124): 
#     set_of_non_abundant_sums.add(i2)


# set_of_non_abundant_sums.difference_update(sum_of_abundant)
# print(sum(set_of_non_abundant_sums))




# This Function will show You wheather a number is perfect number.
def perfect_number(if_perfect):
    return sum(i for i in range(1,if_perfect) if if_perfect % i == 0)

def abundant_vs_deficient (num):
        # Abundant number
    if perfect_number(num) > num:
        return True
        # Deficient number
#     if perfect_number(num) < num:
#         return num

result = 0
abundant_set = []
limit = 28124

for num in range(limit):
    if abundant_vs_deficient(num) == True:
        abundant_set.append(num) 

def looking_for_abundant(num):
    for c in (i for i in abundant_set if i < num):
        for o in (i for i in abundant_set if i < num):
            if c + o == num:
                return True
    return False

if __name__ == "__main__":
    resulted_set = set(n for n in range(1,limit) if not looking_for_abundant(n))
    print(sum(resulted_set))

