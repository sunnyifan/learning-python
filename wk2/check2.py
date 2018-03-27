#################################################
# Check2
#################################################

from cs112_f16_wk2 import assertEqual, assertAlmostEqual, lintAll, testAll
import math

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Problems
#################################################

def digitCount(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def hasConsecutiveDigits(n):
    n = abs(n)
    if 0 <= n < 10:
        return False
    digit = n % 10
    n //= 10
    while n > 0:
        if n % 10 == digit:
            return True
        digit = n % 10
        n //= 10
    return False

def gcd(x, y):
    return 42

def nthPrime(n):
    return 42

def nthAdditivePrime(n):
    return 42

def nthPerfectNumber(n):
    return 42

#################################################
# Test Functions
#################################################

def testDigitCount():
    print('Testing digitCount()... ', end='')
    assertEqual(digitCount(3), 1)
    assertEqual(digitCount(33), 2)
    assertEqual(digitCount(3030), 4)
    assertEqual(digitCount(30300), 5)
    assertEqual(digitCount(-3030), 4)
    assertEqual(digitCount(0), 1)
    print('Passed.')

def testHasConsecutiveDigits():
    print('Testing hasConsecutiveDigits()... ', end='')
    assertEqual(hasConsecutiveDigits(0), False)
    assertEqual(hasConsecutiveDigits(123456789), False)
    assertEqual(hasConsecutiveDigits(1212), False)
    assertEqual(hasConsecutiveDigits(1212111212), True)
    assertEqual(hasConsecutiveDigits(33), True)
    assertEqual(hasConsecutiveDigits(330), True)
    assertEqual(hasConsecutiveDigits(3003), True)
    assertEqual(hasConsecutiveDigits(-1212111212), True)
    print('Passed.')

def testGcd():
    print('Testing gcd()... ', end='')
    assertEqual(gcd(3, 3), 3)
    assertEqual(gcd(3**6, 3**6), 3**6)
    assertEqual(gcd(3**6, 2**6), 1)
    assertEqual (gcd(2*3*4*5,3*5), 15)
    x = 1568160 # 2**5 * 3**4 * 5**1 *        11**2
    y = 3143448 # 2**3 * 3**6 *        7**2 * 11**1
    g =    7128 # 2**3 * 3**4 *               11**1
    assertEqual(gcd(x, y), g)
    print('Passed.')

def testNthPrime():
    print('Testing nthPrime()... ', end='')
    assertEqual(nthPrime(0), 2)
    assertEqual(nthPrime(1), 3)
    assertEqual(nthPrime(2), 5)
    assertEqual(nthPrime(3), 7)
    assertEqual(nthPrime(10), 31)
    assertEqual(nthPrime(20), 73)
    assertEqual(nthPrime(30), 127)
    print('Passed.')

def testNthAdditivePrime():
    print('Testing nthAdditivePrime()... ', end='')
    assertEqual(nthAdditivePrime(0), 2)
    assertEqual(nthAdditivePrime(1), 3)
    assertEqual(nthAdditivePrime(5), 23)
    assertEqual(nthAdditivePrime(10), 61)
    assertEqual(nthAdditivePrime(15), 113)
    print('Passed.')

def testNthPerfectNumber():
    print('Testing nthPerfectNumber()... ', end='')
    assertEqual(nthPerfectNumber(0), 6)
    assertEqual(nthPerfectNumber(1), 28)
    assertEqual(nthPerfectNumber(2), 496)  
    assertEqual(nthPerfectNumber(3), 8128) # this can be slow 
    print('Passed.')

#################################################
# Main
#################################################

def main():
    lintAll() # check style rules
    testAll(
        testDigitCount,
        testHasConsecutiveDigits,
        testGcd,
        testNthPrime,
        testNthAdditivePrime,
        testNthPerfectNumber,
    )

if __name__ == '__main__':
    main()
