__author__ = 'eugene'

from numpy import sqrt


triangle_table = []  # list of triangle numbers that have been evaluated so far
divisor_table = [] # list of lists of divisors corresponding to triangle_table
prime_list = [2] # list of prime numbers that have been calculated so far
last_checked_for_prime = 2 # last number that was checked if was prime, kept here to shorten later checks

def euler():
    natural_number = 1
    triangle_number = 1

    divisor_count = 1
    while divisor_count <= 500:
        natural_number += 1
        triangle_number += natural_number

        divisors = find_prime_factors(triangle_number)
        divisors.sort()
        divisor_table = divisor_table + [divisors]
        divisor_count = len(divisors)
        if len(divisors) > 100:
            print [triangle_number, divisors]


def find_prime_factors(num):
    ### Takes number for which prime factors are to be found
    ### Returns list of powers of each prime number that correspond to the global prime_list

    num = float(num) # Cast as float to make calculating square root more precise
    prime_powers = []
    prime_iter = prime_list[0]
    prime_num = prime_iter.next()
    divided_num = num # Number will be divided by the prime factor each time it is tallied
    while prime_num <= sqrt(num):
        power = 0  # Number of times the prime factor divides into the number
        while divided_num % prime_num == 0:
            power += 1
            divided_num /= prime_num

        if power > 0:
            power += 1  # Add one more because that's how the prime factorialization rule works

        prime_powers += [power]

        try:
            prime_num = prime_iter.next()
        except StopIteration:
            break



euler()