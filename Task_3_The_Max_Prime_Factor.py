import math
#Task : 3 (Find the largest prime factor of number) Version_1(Improved)

def isdisprime(factor, factors_set = [], n = 0):
    for is_factor in range(2, int(math.sqrt(factor))):
        if factor % is_factor == 0: 
        	factors_set.append(is_factor)

    for i in factors_set:
        for n in range(3, max(factors_set)):
            if max(factors_set) % n == 0:
                factors_set.remove(max(factors_set))

    print(max(factors_set))
isdisprime(600851475143)

#Task : 3.1 (Find the largest prime factor of number:My_first_recursion)

# def my_first_recursion(number,number1):
#     if number > 0:
#         print('number = ',number)
#         number -= 1
#         if number1 > 0:
#             print('number1 = ',number1)
#             number1 -= 1
#         my_first_recursion(number, number1)
#     return number, number1
#
# my_first_recursion(3, 3)


#Task : 3 (Find the largest prime factor of number)Version_2

# def maxPrimeFactors (n):
#     maxPrime = -1
#
#     while n % 2 == 0:
#         maxPrime = 2
#         n >>= 1     # equivalent to n /= 2
#
#     # n must be odd at this point,
#     # thus skip the even numbers and
#     # iterate only for odd integers
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         while n % i == 0:
#             maxPrime = i
#             n = n / i
#
#     # This condition is to handle the
#     # case when n is a prime number
#     # greater than 2
#     if n > 2:
#         maxPrime = n
#
#     return int(maxPrime)
#
# print(maxPrimeFactors(60085147514323131241232))


#Task : 3 (Find the largest prime factor of number:There was used recursion method!)Version_3

# def prime_factorize(x,li=[]):
#     for i in range(3,int(math.sqrt(x))):
#         if not x%i:
#             li.append(i)
#             break
#     else:                      #This else belongs to for
#         li.append(x)
#         print (int(max(li)))
#         return li
#     prime_factorize(x/i,li)

# prime_factorize(60085147514323412341)