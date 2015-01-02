from math import sqrt

def count_factors(num):
    factors = 0
    for i in range(1,int(sqrt(num))+1):
        if num % i == 0:
            factors += 1

    if sqrt(num) == int(sqrt(num)):
        factors = 2*factors - 1
    else:
        factors = 2*factors

    return factors

def euler():
    triangle_num = 1
    natural_num = 2
    factors = 0
    while factors < 500:
        triangle_num += natural_num
        print(triangle_num)
        natural_num += 1
        factors = count_factors(triangle_num)

    print factors

euler()