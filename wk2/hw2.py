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

def nthPrime(n):
    found = 0
    guess = 0
    while found <= n:
        guess += 1
        if isPrime(guess):
            found += 1
    return guess

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

def sumOfDigits(n):
    n = abs(n)
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    return total

def sumOfPrimeFactors(n):
    total = 0
    trail = 0
    if n <= 1:
        return 0
    while n > 1:
        if n % nthPrime(trail) == 0:
            total += sumOfDigits(nthPrime(trail))
            n //= nthPrime(trail)
            trail = 0
        else:
            trail += 1
    return total

def isSmithNumber(n):
    if isPrime(n):
        return False
    return sumOfDigits(n) == sumOfPrimeFactors(n)

def isWeaklyPrime(n):
    if not isPrime(n):
        return False
    nOrig = n
    digitUnit = 1
    while n > 0:
        digit = n % 10
        for factor in range(0, 10):
            nAlt = nOrig + ((factor - digit) * digitUnit)
            if nAlt != nOrig:
                if isPrime(nAlt):
                    return False
        n //= 10
        digitUnit *= 10
    return True

#################################################
# Helper Functions for play112
#################################################

def makeBoard(moves):
    board = 8
    while moves > 1:
        board = board * 10 + 8
        moves -= 1
    return board

def kthDigit(n,k):
    n = abs(n)
    if k > digitCount(n):
        return 0
    while k >= 0:
        digit = n % 10
        n //= 10
        k -= 1
    return digit

def replaceKthDigit(n,k,d):
    nOrig = n
    n = abs(n)
    digit = kthDigit(n,k)
    nAlt = nOrig + (d - digit) * (10**k)
    if nOrig < 0:
        return -nAlt
    return nAlt

def getLeftmostDigit(n):
    count = digitCount(n)
    k = count - 1
    return kthDigit(n,k)

def clearLeftmostDigit(n):
    count = digitCount(n)
    digit = getLeftmostDigit(n)
    result = n - digit * (10**(count-1))
    return result

def makeMove(board, position, move):
    if position < 1 or position > digitCount(board):
        return "offboard!"
    if move != 1 and move != 2:
        return "move must be 1 or 2!"
    k = digitCount(board) - position
    if kthDigit(board, k) != 8:
        return "occupied!"
    return replaceKthDigit(board, k, move)

def isWin(board):
    while board > 100:
        count = digitCount(board)
        trio = board // (10**(count-3))
        if trio == 112:
            return True
        board = clearLeftmostDigit(board)
    return False

def isFull(board):
    while board > 0:
        digit = board % 10
        if digit == 8:
            return False
        board //= 10
    return True

def whoseTurn(game):
    allTurns = digitCount(game) - 1
    if allTurns % 4 == 0:
        return "Player 2"
    else:
        return "Player 1"

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
        carrylessSum = 0
        x1 //= 10
        digitUnit *= 10
    return carrylessMultiply

def nthSmithNumber(n):
    found = 0
    guess = 0
    while found <= n:
        guess += 1
        if isSmithNumber(guess):
            found += 1
    return guess

###### BONUS #######

def nthWeaklyPrime(n):
    found = 0
    guess = 0
    while found <= n:
        guess += 1
        if isWeaklyPrime(guess):
            found += 1
    return guess

def play112(game):
    # initiate board settings
    gameOrig = game
    board = makeBoard(getLeftmostDigit(game))
    # generate final board condition
    game = clearLeftmostDigit(game)
    while game > 0:
        position = getLeftmostDigit(game)
        game = clearLeftmostDigit(game)
        move = getLeftmostDigit(game)
        if isinstance(makeMove(board, position, move), int):
            board = makeMove(board, position, move)
            game = clearLeftmostDigit(game)
        else:
            return str(board) + ": " + str(whoseTurn(gameOrig)) + ": " + str(makeMove(board, position, move))
    result = str(board) + ": "
    # decide result of the game
    if isWin(board):
        result += str(whoseTurn(gameOrig)) + " wins!"
    elif isFull(board):
        result += "Tie!"
    else:
        result += "Unfinished!"
    return result

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
    assertEqual(nthWeaklyPrime(0), 294001)
    assertEqual(nthWeaklyPrime(1), 505447)
    assertEqual(nthWeaklyPrime(2), 584141)
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

def testMakeBoard():
    print("Testing makeBoard()...", end="")
    assert (makeBoard(1) == 8)
    assert (makeBoard(2) == 88)
    assert (makeBoard(3) == 888)
    print("Passed!")

def testKthDigit():
    print("Testing kthDigit()...", end="")
    assert(kthDigit(789, 0) == kthDigit(-789, 0) == 9)
    assert(kthDigit(789, 1) == kthDigit(-789, 1) == 8)
    assert(kthDigit(789, 2) == kthDigit(-789, 2) == 7)
    assert(kthDigit(789, 3) == kthDigit(-789, 3) == 0)
    assert(kthDigit(789, 4) == kthDigit(-789, 4) == 0)
    print("Passed!")

def testReplaceKthDigit():
    print("Testing replaceKthDigit()...", end="")
    assert (replaceKthDigit(789, 0, 6) == 786)
    assert (replaceKthDigit(789, 1, 6) == 769)
    assert (replaceKthDigit(789, 2, 6) == 689)
    assert (replaceKthDigit(789, 3, 6) == 6789)
    assert (replaceKthDigit(789, 4, 6) == 60789)
    print("Passed!")

def testGetLeftmostDigit():
    print("Testing replaceKthDigit()...", end="")
    assert (getLeftmostDigit(7089) == 7)
    assert (getLeftmostDigit(89) == 8)
    assert (getLeftmostDigit(9) == 9)
    assert (getLeftmostDigit(0) == 0)
    print("Passed!")

def testClearLeftmostDigit():
    print("Testing replaceKthDigit()...", end="")
    assert (clearLeftmostDigit(789) == 89)
    assert (clearLeftmostDigit(89) == 9)
    assert (clearLeftmostDigit(9) == 0)
    assert (clearLeftmostDigit(0) == 0)
    assert (clearLeftmostDigit(60789) == 789)
    print("Passed!")

def testMakeMove():
    print("Testing replaceKthDigit()...", end="")
    assert (makeMove(8, 1, 1) == 1)
    assert (makeMove(888888, 1, 1) == 188888)
    assert (makeMove(888888, 2, 1) == 818888)
    assert (makeMove(888888, 5, 2) == 888828)
    assert (makeMove(888888, 6, 2) == 888882)
    assert (makeMove(888888, 6, 3) == "move must be 1 or 2!")
    assert (makeMove(888888, 7, 1) == "offboard!")
    assert (makeMove(888881, 6, 1) == "occupied!")
    print("Passed!")

def testIsWin():
    print("Testing replaceKthDigit()...", end="")
    assert (isWin(888888) == False)
    assert (isWin(112888) == True)
    assert (isWin(811288) == True)
    assert (isWin(888112) == True)
    assert (isWin(211222) == True)
    assert (isWin(212212) == False)
    print("Passed!")

def testIsFull():
    print("Testing replaceKthDigit()...", end="")
    assert (isFull(888888) == False)
    assert (isFull(121888) == False)
    assert (isFull(812188) == False)
    assert (isFull(888121) == False)
    assert (isFull(212122) == True)
    assert (isFull(212212) == True)
    print("Passed!")

#################################################
# Main
#################################################

def main():
    testAll(
        #testSumOfSquaresOfDigits,
        #testIsHappyNumber,
        #testNthHappyNumber,
        #testNthHappyPrime,
        #testNearestKaprekarNumber,
        #testCarrylessMultiply,
        #testNthSmithNumber,
        # bonus: (uncomment these to test them....)
        #testNthWeaklyPrime,
        testMakeBoard,
        testKthDigit,
        testReplaceKthDigit,
        testGetLeftmostDigit,
        testClearLeftmostDigit,
        testMakeMove,
        testIsWin,
        testIsFull,
        testPlay112,
    )

if __name__ == '__main__':
    main()
