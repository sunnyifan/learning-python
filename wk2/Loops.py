# 1. for loops
def sumFromMToN(m, n):
    total = 0
    # note that range(x, y) includes x but excludes y
    for x in range(m, n+1):     
        total += x
    return total

print(sumFromMToN(5, 10) == 5+6+7+8+9+10)

# Function without loop
def sumFromMToN(m, n):
    return sum(range(m, n+1))

print(sumFromMToN(5, 10) == 5+6+7+8+9+10)

# And we can even do this with a closed-form formula
def sumToN(n):              # helper function
    return n*(n+1)//2

def sumFromMToN_byFormula(m, n):
    return (sumToN(n) - sumToN(m-1))

print(sumFromMToN_byFormula(5, 10) == 5+6+7+8+9+10)

# What if we omit the first parameter?
def sumToN(n):
    total = 0
    for x in range(n+1):    # assumed range(0, n+1)
        total += x
    return total

print(sumToN(5) == 0+1+2+3+4+5)

# What if we add a third parameter?
def sumEveryKthFromMToN(m, n, k):
    total = 0
    for x in range(m, n+1, k):  # third parameter stands for increment
        total += x
    return total

print(sumEveryKthFromMToN(5, 20, 7) == (5 + 12 + 19))

# Sum just odd numbers from m to n:
def sumOfOddsFromMToN(m, n):
    total = 0
    for x in range(m, n+1):
        if (x % 2 == 1):
            total += x
    return total

print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))

# Once again:
def sumOfOddsFromMToN(m, n):
    if (m % 2 == 0):
        # m is even, add 1 to start on an odd
        m += 1
    total = 0
    for x in range(m, n+1, 2):
        total += x
    return total

print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))

# Here we will range in reverse (not wise in this case, but instructional)
def sumOfOddsFromMToN(m, n):
    if (n % 2 == 0):
        # n is even, subtract 1 to start on an odd
        n -= 1
    total = 0
    for x in range(n, m-1, -2):  # -2 corresponds with inverse order
        total += x
    return total

print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))

def sumOfOddsFromMToN(m, n):
    if (m % 2 == 0): m += 1     # if condition in 1 line
    return sum(range(m, n+1, 2))

print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))

# This is the worst way so far -- too confusing.
def sumOfOddsFromMToN(m, n):
    return sum(range(m + (1 - m%2), n+1, 2)) # this works, but readability..

print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))


# 2. Nested for loops
def printCoordinates(xMax,yMax):
    for x in range(xMax+1):
        for y in range(yMax+1):
            print('(',x,',',y,')',end = '')
        print()
        
printCoordinates(4,5)

# Some stars
def printStarRectangle(n):
    # print an "n x n" rectangle of asterisks
    for row in range(n):
        for col in range(n):
            print('*', end='')
        print()

printStarRectangle(5)

# Another example
def printMysteryStarShape(n):
    for row in range(n):
        print(row, end='')
        for col in range(row):
            print('*', end='')
        print()
printMysteryStarShape(5)


# 3. While loops
# use while loops when there is an indeterminate number of iterations
def leftmostDigit(n):
    n = abs(n)
    while (n >= 10):
        n = n // 10
    return n

print(leftmostDigit(72658489290098) == 7)

# Example: nth positive integer with some property
# eg: find the nth number that is a multiple of either 4 or 7
def isMultipleOf4or7(x):
    return ((x % 4) == 0) or ((x % 7) == 0)

def nthMultipleOf4or7(n):
    found = 0
    guess = -1
    while (found <= n):
        guess += 1
        if (isMultipleOf4or7(guess)):
            found += 1
    return guess

print("Multiples of 4 or 7: ", end="")
for n in range(15):
    print(nthMultipleOf4or7(n), end=" ")
print()

# Misuse: While loop over a fixed range
# sum numbers from 1 to 10
# note:  this works, but you should not use "while" here.
#        instead, do this with "for" (once you know how)
def sumToN(n):
    total = 0
    counter = 1
    while (counter <= n):
        total += counter
        counter += 1
    return total

print(sumToN(5) == 1+2+3+4+5)

# Once again, but with a bug
def buggySumToN(n):
    # note: this not only uses a "while" instead of a "for" loop,
    # but it also contains a bug. Ugh.
    total = 0
    counter = 0
    while (counter <= n):
        counter += 1
        total += counter
    return total

print(buggySumToN(5) == 1+2+3+4+5)

# once again, with a for loop:
# A for loop is the preferred way to loop over a fixed range.
def sumToN(n):
    total = 0
    for counter in range(n+1):
        total += counter
    return total

print(sumToN(5) == 1+2+3+4+5)


# 4. break and continue
for n in range(200):
    if (n % 3 == 0):
        continue # skips rest of this pass (rarely a good idea to use "continue")
    elif (n == 8):
        break # skips rest of entire loop
    print(n, end=" ")
print()

# Infinite "while" loop with break:
def readUntilDone():
    linesEntered = 0
    while (True):
        response = input("Enter a string (or 'done' to quit): ")
        if (response == "done"):
            break
        print("  You entered: ", response)
        linesEntered += 1
    print("Bye!")
    return linesEntered

linesEntered = readUntilDone()
print("You entered", linesEntered, "lines (not counting 'done').")


# 5. isPrime
# Note: there are faster/better ways.  We're just going for clarity and simplicity here.
def isPrime(n):
    if (n < 2):
        return False
    for factor in range(2,n):
        if (n % factor == 0):
            return False
    return True

# And take it for a spin
for n in range(100):
    if isPrime(n):
        print(n, end=" ")
print()
