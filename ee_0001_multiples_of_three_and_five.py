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


def sumMultiplesOfXOrY(t,x,y):
    """
    returns sum of all multiples of x or y of total t
    time: O(n) linear
    space: O(1) constant
    """
    sum = 0
    for i in range(t+1):
        if i % x == 0 or i % y == 0:
            sum = sum + i
    return sum


def sumDivisibleBy(t,x):
    """
    returns sum of all multiples of number x of total t
    time: O(1) constant
    space: O(1) constant

    Simulates an incrementor
    to the rounded nearest integer
    of total t divided by multiple x
    * x
    """
    p = t // x
    return ((p*(p+1)) // 2) * x







def main():
    """Find the sum of all the multiples of 3 or 5 below the inputted value."""
    input_target = int(input('target:'))

    result = sumMultiplesOfXOrY(input_target,3,5)
    print(result)

    # sum the multiples of 3 and the multiples of 5 under 1000
    # while removing any duplicate multiples
    result2 = sumDivisibleBy(input_target,3) + sumDivisibleBy(input_target,5) - sumDivisibleBy(input_target,15)
    print(result2)

if __name__ == "__main__":
    main()
