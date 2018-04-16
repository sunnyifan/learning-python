#################################################
# Hw2
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

def nthKaprekarNumber(n):
    found = 0
    guess = 0
    while found <= n:
        guess += 1
        if isKaprekarNumber(guess):
            found += 1
    return guess

def digitCount(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def carrylessAdd(x1, x2):
    min_count = min(digitCount(x1), digitCount(x2))
    max_x = max(x1, x2)
    carryless_sum = 0
    round = 0
    while round < min_count:
        digit_sum = (x1 % 10 + x2 % 10) % 10
        carryless_sum += digit_sum * (10**round)
        x1 //= 10
        x2 //= 10
        round += 1
    return (max_x - (max_x % (10**round)) + carryless_sum)

#################################################
# Problems
#################################################

def sumOfSquaresOfDigits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit**2
        n //= 10
    return total

def isHappyNumber(n):
    if n < 1:
        return False
    while sumOfSquaresOfDigits(n) > 4:
        n = sumOfSquaresOfDigits(n)
    return sumOfSquaresOfDigits(n) == 1

def nthHappyNumber(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if isHappyNumber(guess):
            found += 1
    return guess

def nthHappyPrime(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if isHappyNumber(guess) and isPrime(guess):
            found += 1
    return guess

''' 
# This does work but the style is far from desired
def nearestKaprekarNumber(n):
    if n <= 5:
        return 1
    if isKaprekarNumber(n):
        return n
    guess = 1
    minDistance = n**2
    for factor in range(1, roundHalfUp(n**0.5) // 2 + 1):
        distance = abs(n - nthKaprekarNumber(factor))
        if minDistance > distance:
            minDistance = distance
            guess = nthKaprekarNumber(factor)
    return guess
'''

def nearestKaprekarNumber(n):
    if n <= 5:
        return 1
    if isKaprekarNumber(n):
        return n
    trail = 0
    guess = 1
    while guess < n:
        trail += 1
        guess = nthKaprekarNumber(trail)
    if (guess - n) < (n - nthKaprekarNumber(trail - 1)) :
        return guess
    return nthKaprekarNumber(trail - 1)

def carrylessMultiply(x1, x2):
    carrylessSum = 0
    carrylessMultiply = 0
    digitUnit = 1
    while x1 > 0:
        digit = x1 % 10
        while digit > 0:
            carrylessSum = carrylessAdd(x2, carrylessSum)
            digit -= 1
        carrylessMultiply = carrylessAdd((carrylessSum * digitUnit), carrylessMultiply)
        x1 //= 10
        digitUnit *= 10
    return carrylessMultiply

def nthSmithNumber(n):
    return 42

###### BONUS #######

def nthWeaklyPrime(n):
    return 42

def play112(game):
    return 42

#################################################
# Test Functions
#################################################

def testSumOfSquaresOfDigits():
    print("Testing sumOfSquaresOfDigits()...", end="")
    assertEqual(sumOfSquaresOfDigits(5), 25)   # 5**2 = 25
    assertEqual(sumOfSquaresOfDigits(12), 5)   # 1**2 + 2**2 = 1+4 = 5
    assertEqual(sumOfSquaresOfDigits(234), 29) # 2**2 + 3**2 + 4**2 = 4 + 9 + 16 = 29
    print("Passed all tests!")

def testIsHappyNumber():
    print("Testing isHappyNumber()...", end="")
    assertEqual(isHappyNumber(-7), False)
    assertEqual(isHappyNumber(1), True)
    assertEqual(isHappyNumber(2), False)
    assertEqual(isHappyNumber(97), True)
    assertEqual(isHappyNumber(98), False)
    assertEqual(isHappyNumber(404), True)
    assertEqual(isHappyNumber(405), False)
    print("Passed all tests!")

def testNthHappyNumber():
    print("Testing nthHappyNumber()...", end="")
    assertEqual(nthHappyNumber(0), 1)
    assertEqual(nthHappyNumber(1), 7)
    assertEqual(nthHappyNumber(2), 10)
    assertEqual(nthHappyNumber(3), 13)
    assertEqual(nthHappyNumber(4), 19)
    assertEqual(nthHappyNumber(5), 23)
    assertEqual(nthHappyNumber(6), 28)
    assertEqual(nthHappyNumber(7), 31)
    print("Passed all tests!")

def testIsHappyPrime():
    print("Testing isHappyPrime()...", end="")
    assertEqual(isHappyPrime(1), False)
    assertEqual(isHappyPrime(2), False)
    assertEqual(isHappyPrime(3), False)
    assertEqual(isHappyPrime(7), True)
    assertEqual(isHappyPrime(10), False)
    assertEqual(isHappyNumber(13), True)
    print("Passed all tests!")

def testNthHappyPrime():
    print("Testing nthHappyPrime...", end="")
    assertEqual(nthHappyPrime(0), 7)
    assertEqual(nthHappyPrime(1), 13)
    assertEqual(nthHappyPrime(2), 19)
    assertEqual(nthHappyPrime(3), 23)
    assertEqual(nthHappyPrime(4), 31)
    assertEqual(nthHappyPrime(10), 167)
    assertEqual(nthHappyPrime(20), 397)
    print("Passed all tests!")

def testNearestKaprekarNumber():
    print("Testing nearestKaprekarNumber()...", end="")
    assertEqual(nearestKaprekarNumber(1), 1)
    assertEqual(nearestKaprekarNumber(0), 1)
    assertEqual(nearestKaprekarNumber(-1), 1)
    assertEqual(nearestKaprekarNumber(-2), 1)
    assertEqual(nearestKaprekarNumber(-12345), 1)
    assertEqual(nearestKaprekarNumber(1.234), 1)
    assertEqual(nearestKaprekarNumber(4.99999999), 1)
    assertEqual(nearestKaprekarNumber(5), 1)
    assertEqual(nearestKaprekarNumber(5.00000001), 9)
    assertEqual(nearestKaprekarNumber(27), 9)
    assertEqual(nearestKaprekarNumber(28), 45)
    assertEqual(nearestKaprekarNumber(45), 45)
    assertEqual(nearestKaprekarNumber(50), 45)
    assertEqual(nearestKaprekarNumber(51), 55)
    assertEqual(nearestKaprekarNumber(1611), 999)
    assertEqual(nearestKaprekarNumber(1612), 2223)
    assertEqual(nearestKaprekarNumber(2475.4), 2223)
    assertEqual(nearestKaprekarNumber(2475.5), 2223)
    assertEqual(nearestKaprekarNumber(2475.51), 2728)
    assertEqual(nearestKaprekarNumber(2475.6), 2728)
    #kaps = [1, 9, 45, 55, 99, 297, 703, 999, 2223, 2728]
    #bigKaps = [994708, 999999]
    # assertEqual(nearestKaprekarNumber(995123), 994708)
    # assertEqual(nearestKaprekarNumber(9376543), 9372385)
    # assertEqual(nearestKaprekarNumber(13641234), 13641364)
    print("Passed!")

def testCarrylessMultiply():
    print("Testing carrylessMultiply()...", end="")
    assertEqual(carrylessMultiply(643, 59), 417)
    assertEqual(carrylessMultiply(6412, 387), 807234)
    print("Passed!")

def testNthSmithNumber():
    print('Testing nthSmithNumber()... ', end='')
    assertEqual(nthSmithNumber(0), 4)
    assertEqual(nthSmithNumber(1), 22)
    assertEqual(nthSmithNumber(2), 27)
    assertEqual(nthSmithNumber(3), 58)
    assertEqual(nthSmithNumber(4), 85)
    assertEqual(nthSmithNumber(5), 94)
    assertEqual(nthSmithNumber(6), 121)
    print('Passed.')

def testNthWeaklyPrime():
    print("Testing carrylessMultiply()...", end="")
    #assertEqual(nthWeaklyPrime(0), 294001)
    assertEqual(nthWeaklyPrime(1), 505447)
    #assertEqual(nthWeaklyPrime(2), 584141)
    print("Passed!")

def testPlay112():
    print("Testing play112()...", end="")
    assertEqual(play112( 5 ), "88888: Unfinished!")
    assertEqual(play112( 521 ), "81888: Unfinished!")
    assertEqual(play112( 52112 ), "21888: Unfinished!")
    assertEqual(play112( 5211231 ), "21188: Unfinished!")
    assertEqual(play112( 521123142 ), "21128: Player 2 wins!")
    assertEqual(play112( 521123151 ), "21181: Unfinished!")
    assertEqual(play112( 52112315142 ), "21121: Player 1 wins!")
    assertEqual(play112( 523 ), "88888: Player 1: move must be 1 or 2!")
    assertEqual(play112( 51223 ), "28888: Player 2: move must be 1 or 2!")
    assertEqual(play112( 51211 ), "28888: Player 2: occupied!")
    assertEqual(play112( 5122221 ), "22888: Player 1: occupied!")
    assertEqual(play112( 51261 ), "28888: Player 2: offboard!")
    assertEqual(play112( 51122324152 ), "12212: Tie!")
    print("Passed!")

#################################################
# Main
#################################################

def main():
    testAll(
        testSumOfSquaresOfDigits,
        testIsHappyNumber,
        testNthHappyNumber,
        testNthHappyPrime,
        testNearestKaprekarNumber,
        testCarrylessMultiply,
        testNthSmithNumber,
        # bonus: (uncomment these to test them....)
        # testNthWeaklyPrime,
        # testPlay112,
    )

if __name__ == '__main__':
    main()
