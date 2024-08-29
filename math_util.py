import math
import random


# 1. Calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# 2. Generate a list of prime numbers up to a given limit
def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


# 3. Find the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# 4. Calculate the area of a circle given its radius
def circle_area(radius):
    return math.pi * radius ** 2


# 5. Generate a random number between a given range
def random_number(min_val, max_val):
    return random.randint(min_val, max_val)


# 6. Calculate the sum of digits of a number
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))


# 7. Convert degrees to radians
def degrees_to_radians(degrees):
    return math.radians(degrees)


# 8. Check if a number is a perfect square
def is_perfect_square(n):
    return int(math.sqrt(n)) ** 2 == n


# 9. Calculate the nth Fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# 10. Calculate the standard deviation of a list of numbers
def standard_deviation(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)
