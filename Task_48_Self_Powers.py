def self_power(n):
    result = 0
    for i in range(1, n + 1):
        result += i ** i
    return result

print(self_power(1000))