#################################################
# Lab2
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

def reverseNumber(n):
    n = abs(n)
    reverse = 0
    while (n > 0):
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10
    return reverse

def isPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True

def isEmirpsPrime(n):
    if n < 13:
        return False
    if n == reverseNumber(n):
        return False
    if isPrime(n):
        return isPrime(reverseNumber(n))

def isKaprekarNumber(n):
    if n < 1:
        return False
    square = n**2
    round = 0
    right_part = 0
    while square > 0:
        right_part += (square % 10) * (10**round)
        left_part = (n**2 - right_part) // (10**(round + 1))
        total = right_part + left_part
        if right_part != 0 and total == n:
            return True
        round += 1
        square //= 10
    return False

#################################################
# Problems
#################################################

def nthEmirpsPrime(n):
    found = 0
    guess = 0
    while found <= n:
        guess += 1
        if isEmirpsPrime(guess):
            found += 1
    return guess

def findZeroWithBisection(f, x0, x1, epsilon):
    return 42

def carrylessAdd(x1, x2):
    return 42

def nthKaprekarNumber(n):
    found = 0
    guess = 0
    while found <= n:
        guess += 1
        if isKaprekarNumber(guess):
            found += 1
    return guess

def integral(f, a, b, N):
    return 42

#################################################
# Test Functions
#################################################

def testNthEmirpsPrime():
    print('Testing nthEmirpsPrime()...', end='')
    assertEqual(nthEmirpsPrime(0), 13)
    assertEqual(nthEmirpsPrime(8), 107)
    assertEqual(nthEmirpsPrime(10), 149)
    assertEqual(nthEmirpsPrime(20), 701)
    print('Passed.')

def testFindZerosWithBisection():
    print('Testing findZerosWithBisection()...', end='')
    def f1(x): return x*x - 2 # root at x=sqrt(2)
    x = findZeroWithBisection(f1, 0, 2, 0.000000001)
    assertAlmostEqual(x, math.sqrt(2))
    def f2(x): return x**2 - (x + 1) # root at x=phi
    x = findZeroWithBisection(f2, 0, 2, 0.000000001)
    phi = (1 + 5**0.5)/2             # the actual value
    assertAlmostEqual(x, phi)
    def f3(x): return x**5 - 2**x # f(1)<0, f(2)>0
    x = findZeroWithBisection(f3, 1, 2, 0.000000001)
    assert(almostEqual(f3(x), 0))
    print('Passed.')

def testCarrylessAdd():
    print('Testing carrylessAdd()...', end='')
    assertEqual(carrylessAdd(785, 376), 51)
    assertEqual(carrylessAdd(12345678900, 38984034003), 40229602903)
    print('Passed.')

def testNthKaprekarNumber():
    print('Testing nthKaprekarNumber()...', end='')
    assertEqual(nthKaprekarNumber(0), 1)
    assertEqual(nthKaprekarNumber(1), 9)
    assertEqual(nthKaprekarNumber(2), 45)
    assertEqual(nthKaprekarNumber(3), 55)
    assertEqual(nthKaprekarNumber(4), 99)
    assertEqual(nthKaprekarNumber(5), 297)
    assertEqual(nthKaprekarNumber(6), 703)
    assertEqual(nthKaprekarNumber(7), 999)
    print('Passed.')

def f1(x): return 42
def i1(x): return 42*x 
def f2(x): return 2*x  + 1
def i2(x): return x**2 + x
def f3(x): return 9*x**2
def i3(x): return 3*x**3
def f4(x): return math.cos(x)
def i4(x): return math.sin(x)
def testIntegral():
    print('Testing integral()...', end='')
    epsilon = 10**-4
    assertAlmostEqual(integral(f1, -5, +5, 1), (i1(+5)-i1(-5)),
                      epsilon=epsilon)
    assertAlmostEqual(integral(f1, -5, +5, 10), (i1(+5)-i1(-5)),
                      epsilon=epsilon)
    assertAlmostEqual(integral(f2, 1, 2, 1), 4,
                      epsilon=epsilon)
    assertAlmostEqual(integral(f2, 1, 2, 250), (i2(2)-i2(1)),
                      epsilon=epsilon)
    assertAlmostEqual(integral(f3, 4, 5, 250), (i3(5)-i3(4)),
                      epsilon=epsilon)
    assertAlmostEqual(integral(f4, 1, 2, 250), (i4(2)-i4(1)),
                      epsilon=epsilon)
    print("Passed!")

#################################################
# Main
#################################################

def main():
    testAll(
        testNthEmirpsPrime,
        testFindZerosWithBisection,
        testCarrylessAdd,
        testNthKaprekarNumber,
        testIntegral,
    )

if __name__ == '__main__':
    main()
