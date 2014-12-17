__author__ = 'eugene'

from numpy import sqrt

def euler():
    natural_number = 1
    triangle_number = 1

    divisor_count= 1
    div_count_table = [[1,1]] # Lookup table of values and their corresponding # of divisors
    prime_array = [] # Array of primes that will be filled as the triangle number increases
    while divisor_count <= 500:
        natural_number = natural_number + 1
        triangle_number = triangle_number + natural_number

        divisor_count = number_of_divisors(triangle_number)
        if divisor_count > 100:
            print [triangle_number, divisor_count]

def number_of_divisors(num):
    divisor_count = 1
    last_divisor = 1.0
    num = float(num)
    for denom in range(2,int(num)+1):
        denom = float(denom)

        if num%denom == 0:
            if sqrt(num) == denom:
                divisor_count = divisor_count * 2 + 1
                return divisor_count
            elif denom > sqrt(num):
                divisor_count = divisor_count * 2
                return divisor_count
            else:
                divisor_count = divisor_count + 1
                last_divisor = denom

euler()