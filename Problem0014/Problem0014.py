__author__ = 'eugene'


def euler():
    num = 999999 # start with the largest number under 1 million
    max_terms = 0
    max_terms_num = 0

    while num > 0:
        if num % 10000 == 0:
            print num
        terms = collatz(num)
        if terms > max_terms:
            max_terms = terms
            max_terms_num = num

        num -= 1

    print max_terms_num


def collatz(num):
    terms = 1
    while num > 1:
        if num % 2 == 0:
            # evens
            num /= 2
            terms += 1
        else:
            # odds
            num = 3 * num + 1
            terms += 1

    return terms + 1

euler()