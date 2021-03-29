#Task : 2 (Find the sum of even Fibonacci integers below 4 000 000): Version_1

# a = 0
# b = 1
# c = 0
# while (a+b) < 4000000:
#     a += b
#     b += a
#     if a % 2 == 0:
#         c += a
#     if b % 2 == 0:
#         c += b
# print(c)

#Task : 2 (Find the sum of even Fibonacci integers below 4 000 000) Version_2

# a = 0
# b = 1
# d = 0
# while d < 4000000:
#     c = a + b
#     a = b
#     b = c
#     if c % 2 == 0:
#         d += c
# print(d)

#Task : 2 (Find the sum of even Fibonacci integers below 4 000 000) Version_3(The Perfect Ones!)

# def fibto(lim):
# 	a, b = 1, 1
# 	while b < lim:
# 		yield b
# 		a, b = b, a+b
# print(sum(n for n in fibto(4000000) if n%2==0))

# a,b,x = 0,1,0
# while b < 4000000:
#     a,b = b,a + b
#     if a % 2 == 0: x += a; print(x)