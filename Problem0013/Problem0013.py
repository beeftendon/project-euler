__author__ = 'eugene'

def euler():

    # Open the supplementary file. Convert each line to an integer
    f = open('Problem0013supp')

    numbers = []
    for line in f:
        numbers += [int(line[:11])] # Remove the newline character and convert to integer, only grab the first 11 digits of each number because that's all you need

    print sum(numbers)

euler()