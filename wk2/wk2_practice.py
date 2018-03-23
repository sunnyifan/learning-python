#################################################
# Week2 Practice
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
    
def countDigitOccurrence(n, d):
    count = 0
    while n >= 1:
        if n % 10 == d:
            count += 1
        n //= 10
    return count
    
def isPowerfulNumber(n):
    if (n < 1):
        return False
    if (n == 1):
        return True
    maxFactor = roundHalfUp(n**0.5)
    for factor in range(1, maxFactor+1):
        if n % (factor**3) != 0:
            continue
        a = n // (factor**3)
        if roundHalfUp(a**0.5) ** 2 == a:
            return True
    return False

''' 
def digitsCount(n):
    n = abs(n)
    count = 0
    while n >= 1:
        count += 1
        n //= 10
    return count
'''

def reverseNumber(n):
    n = abs(n)
    reverse = 0
    while (n > 0):
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10
    return reverse

def isPalindromic(n):
    return n == reverseNumber(n)

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

def isLeftTruncatablePrime(n):
    digit = 0
    decimal = 0
    component = 0
    while n > 0:
        digit = n % 10
        component += digit * (10**decimal)
        if isPrime(component):
            decimal += 1
            n //= 10
        else:
            return False
    return True

#################################################
# Tue Lecture
#################################################

def mostFrequentDigit(n):
    n = abs(n)
    # initialization
    d = 0
    max_count = 0
    max_digit = 0
    # looping d from 0 to 9
    for d in range(0, 9):
        count = countDigitOccurrence(n, d)
        # compare and rewrite max_count and max_digit
        if count > max_count:
            max_count = count
            max_digit = d
    return max_digit

def nthPowerfulNumber(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (isPowerfulNumber(guess)):
            found += 1
    return guess

#################################################
# Wed Recitation
#################################################

def longestDigitRun(n):
    n = abs(n)                  # better than if...then n = -n
        
    consecutive_count = 0       # when setting variable names, concise+readable
    max_consecutive_count = 0
    digit_to_right = n % 10
    longest_digit = n % 10
    
    while n >= 1:
        if n % 10 == digit_to_right:
            consecutive_count += 1
            if consecutive_count > max_consecutive_count:
                max_consecutive_count = consecutive_count
                longest_digit = digit_to_right
            if consecutive_count == max_consecutive_count:
                max_consecutive_count = consecutive_count
                longest_digit = min(digit_to_right, longest_digit)
        else:
            consecutive_count = 1
        digit_to_right = n % 10
        n //= 10
    return longest_digit

''' # draft showing way to debug #
def longestIncreasingRun(n):
    n = abs(n)
    if n < 10:  # trivial case
        return n

#     print("DEBUG: n = ", n)
    length = 0
    original_n = n
    digit_to_right = n % 10
    increasing_run = n % 10
    max_increasing_run = n % 10
#    print("DEBUG: digit_to_right = ", digit_to_right)
#    print("DEBUG: increasing_run = ", increasing_run)
#    print("DEBUG: max_increasing_run = ", max_increasing_run)

    while n >= 10:
#        print("DEBUG: current n = ", n)
#        print("DEBUG: Current digit_to_right", digit_to_right)
        if n % 10 > digit_to_right:
            increasing_run = original_n % (10**length)
            if increasing_run > max_increasing_run:
                max_increasing_run = increasing_run
            original_n = (n - increasing_run) / (10**length)
            digit_to_right = n % 10
            length = 1
        else:
            length += 1
            digit_to_right = n % 10
            n //= 10
    return max_increasing_run

'''

def longestIncreasingRunAttmp(n):
    n = abs(n)
    
    copy_n = n      # represents the original n, used to print out current_run
    run_length = 1  # counting digits in the increasing run
    current_run = 0 # represents increasing runs being counted
    longest_run = 0 # reprensents the longest run out of all
    digit_to_right = n % 10  # initialzed as the unit digit of n ('rightest')
                             # represents the digit to the right of the number
                             # being verified
 
    if n < 10:  # trivial case to eliminate numbers with only 1 digit
        return n

    n //= 10        # since unit digit is already set to be initial dtr
    while n >= 1:   # it can be dropped before the loop
        if n % 10 < digit_to_right:
            run_length += 1
            current_run = copy_n % (10**run_length)
            if current_run > longest_run:
                longest_run = current_run
        else:
            copy_n //= (10**run_length)
            run_length = 1
        digit_to_right = n % 10
        n //= 10    
    return longest_run

def longestIncreasingRun(n):    # simplier, w/o copy_n
    n = abs(n)
 
    if n < 10:  # trivial case to eliminate numbers with only 1 digit
        return n

    run_length = 1  # counting digits in the increasing run
    current_run = n % 10
    longest_run = n % 10
    digit_to_right = n % 10

    n //= 10        # since unit digit is already set to be initial dtr it can be dropped before the loop

    while n >= 1:
        if n % 10 < digit_to_right:
            current_run += (n % 10) * (10**run_length)  # key change
            run_length += 1
            if current_run > longest_run:
                longest_run = current_run
        else:
            run_length = 1
            current_run = n % 10
        digit_to_right = n % 10
        n //= 10    
    return longest_run

   
def nthPalindromicPrime(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if isPalindromic(guess) and isPrime(guess):
            found += 1
    return guess

def nthLeftTruncatablePrime(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if isLeftTruncatablePrime(guess):
            found += 1
    return guess

def nthCarolPrime(n):
    factor = 0
    found = 0
    guess = 0
    while (found <= n):
        factor += 1
        guess = (2**factor - 1)**2 - 2
        if isPrime(guess):
            found += 1
    return guess


#################################################
# Extra Practice
#################################################

def pi(n):
    return 42

def h(n):
    return 42

def estimatedPi(n):
    return 42

def estimatedPiError(n):
    return 42

def hasOnlyOddDigits(n):
    return 42

def isRotation(x, y):
    return 42

def nthCircularPrime(n):
    return 42

#################################################
# Test Functions
#################################################

def testMostFrequentDigit():
    print('Testing mostFrequentDigit()... ', end='')
    assertEqual(mostFrequentDigit(0), 0)
    assertEqual(mostFrequentDigit(1223), 2)
    assertEqual(mostFrequentDigit(12233), 2)
    assertEqual(mostFrequentDigit(-112233), 1)
    assertEqual(mostFrequentDigit(1223322332), 2)
    assertEqual(mostFrequentDigit(123456789), 1)
    assertEqual(mostFrequentDigit(1234567789), 7)
    assertEqual(mostFrequentDigit(1000123456789), 0)
    print('Passed!')

def testNthPowerfulNumber():
    print('Testing nthPowerfulNumber()... ', end='')
    assertEqual(nthPowerfulNumber(0), 1)
    assertEqual(nthPowerfulNumber(1), 4)
    assertEqual(nthPowerfulNumber(2), 8)
    assertEqual(nthPowerfulNumber(3), 9)
    assertEqual(nthPowerfulNumber(4), 16)
    assertEqual(nthPowerfulNumber(5), 25)
    assertEqual(nthPowerfulNumber(10), 64)
    assertEqual(nthPowerfulNumber(15), 121)
    assertEqual(nthPowerfulNumber(20), 196)
    print('Passed!')

def testLongestDigitRun():
    print('Testing longestDigitRun()... ', end='')
    assertEqual(longestDigitRun(117773732), 7)
    assertEqual(longestDigitRun(-677886), 7)
    assertEqual(longestDigitRun(5544), 4)
    assertEqual(longestDigitRun(1), 1)
    assertEqual(longestDigitRun(0), 0)
    assertEqual(longestDigitRun(22222), 2)
    assertEqual(longestDigitRun(111222111), 1)
    print('Passed.')

def testLongestIncreasingRun():
    print('Testing longestIncreasingRun()... ', end='')
    assertEqual(longestIncreasingRun(27648923679), 23679)
    assertEqual(longestIncreasingRun(123345), 345)
    assertEqual(longestIncreasingRun(1232), 123)
    assertEqual(longestIncreasingRun(0), 0)
    assertEqual(longestIncreasingRun(1), 1)
    assertEqual(longestIncreasingRun(10012301230123), 123)
    assertEqual(longestIncreasingRun(12345678987654321), 123456789)
    print('Passed.')

def testNthPalindromicPrime():
    print('Testing nthPalindromicPrime()... ', end='')
    assertEqual(nthPalindromicPrime(0), 2)
    assertEqual(nthPalindromicPrime(1), 3)
    assertEqual(nthPalindromicPrime(5), 101)
    assertEqual(nthPalindromicPrime(10), 313)
    print('Passed.')

def testNthLeftTruncatablePrime():
    print('Testing nthLeftTruncatablePrime()... ', end='')
    assertAlmostEqual(nthLeftTruncatablePrime(0), 2)
    assertAlmostEqual(nthLeftTruncatablePrime(10), 53)
    assertAlmostEqual(nthLeftTruncatablePrime(1), 3)
    assertAlmostEqual(nthLeftTruncatablePrime(5), 17)
    print('Passed.')

def testCarolPrime():
    print('Testing nthCarolPrime()... ', end='')
    assertAlmostEqual(nthCarolPrime(0), 7)
    assertAlmostEqual(nthCarolPrime(1), 47)
    assertAlmostEqual(nthCarolPrime(3), 3967)
    assertAlmostEqual(nthCarolPrime(6), 16769023)
    print('Passed.')

def testPi():
    print('Testing pi()... ', end='')
    assertEqual(pi(1), 0)
    assertEqual(pi(2), 1)
    assertEqual(pi(3), 2)
    assertEqual(pi(4), 2)
    assertEqual(pi(5), 3)
    assertEqual(pi(100), 25)  # there are 25 primes in the range [2,100]
    print('Passed.')

def testH():
    print('Testing h()... ', end='')
    assertAlmostEqual(h(0),0)
    assertAlmostEqual(h(1),1/1            )  # h(1) = 1/1
    assertAlmostEqual(h(2),1/1 + 1/2      )  # h(2) = 1/1 + 1/2
    assertAlmostEqual(h(3),1/1 + 1/2 + 1/3)  # h(3) = 1/1 + 1/2 + 1/3
    print('Passed.')

def testEstimatedPi():
    print('Testing estimatedPi()... ', end='')
    assertEqual(estimatedPi(100), 27)
    print('Passed.')

def testEstimatedPiError():
    print('Testing estimatedPi()... ', end='')
    assertEqual(estimatedPiError(100), 2) # pi(100) = 25, estimatedPi(100) = 27
    assertEqual(estimatedPiError(200), 0) # pi(200) = 46, estimatedPi(200) = 46
    assertEqual(estimatedPiError(300), 1) # pi(300) = 62, estimatedPi(300) = 63
    assertEqual(estimatedPiError(400), 1) # pi(400) = 78, estimatedPi(400) = 79
    assertEqual(estimatedPiError(500), 1) # pi(500) = 95, estimatedPi(500) = 94
    print('Passed.')

def testHasOnlyOddDigits():
    print('Testing hasOnlyOddDigits()... ', end='')
    assertEqual(hasOnlyOddDigits(1), True)
    assertEqual(hasOnlyOddDigits(13579), True)
    assertEqual(hasOnlyOddDigits(111111), True)
    assertEqual(hasOnlyOddDigits(-999999999999), True)
    assertEqual(hasOnlyOddDigits(0), False)
    assertEqual(hasOnlyOddDigits(10), False)
    assertEqual(hasOnlyOddDigits(13579297531), False)
    assertEqual(hasOnlyOddDigits(-13579297531), False)
    print('Passed.')

def testIsRotation():
    print('Testing isRotation()... ', end='')
    assertEqual(isRotation(1, 1), True)
    assertEqual(isRotation(1234, 4123), True)
    assertEqual(isRotation(1234, 3412), True)
    assertEqual(isRotation(1234, 2341), True)
    assertEqual(isRotation(1234, 1234), True)
    assertEqual(isRotation(1234, -1234), False)
    assertEqual(isRotation(1234, 123), False)
    assertEqual(isRotation(1234, 12345), False)
    assertEqual(isRotation(1234, 1235), False)
    assertEqual(isRotation(1234, 1243), False)
    print('Passed.')

def testNthCircularPrime():
    print('Testing nthCircularPrime()... ', end='')
    assertEqual(nthCircularPrime(0), 2)
    assertEqual(nthCircularPrime(1), 3)
    assertEqual(nthCircularPrime(2), 5)
    assertEqual(nthCircularPrime(10), 73)
    assertEqual(nthCircularPrime(15), 197)
    assertEqual(nthCircularPrime(16), 199)
    print('Passed.')

#################################################
# Main
#################################################

def main():
    testAll(
        testMostFrequentDigit,
        testNthPowerfulNumber,
        testLongestDigitRun,
        testLongestIncreasingRun,
        testNthPalindromicPrime,
        testNthLeftTruncatablePrime,
        testCarolPrime,
        testPi,
        testH,
        testEstimatedPi,
        testEstimatedPiError,
        testHasOnlyOddDigits,
        testIsRotation,
        testNthCircularPrime,
    )

if __name__ == '__main__':
    main()
