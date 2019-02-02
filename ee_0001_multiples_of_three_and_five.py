#! usr/bin/env python

# author    : Luke Demarest
# title     : Multiples of Three and Five
# license   : GPLv3
# date      : 2019-02-01

# exercise  : 0001

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def sumMultiplesOf3Or5(t):
    sum = 0
    for i in range(t):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
    return sum


def sumDivisibleBy(t,n):
    p = t // n
    return n*(p*(p+1))//2







def main():
    """invoke the main processes of the program"""

    result = sumMultiplesOf3Or5(1000)
    print(result)

    result2 = sumDivisibleBy(999,3) + sumDivisibleBy(999,5) - sumDivisibleBy(999,15)
    print(result2)

if __name__ == "__main__":
    main()
