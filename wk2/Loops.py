# 1. for loops
def sumFromMToN(m, n):
    total = 0
    # note that range(x, y) includes x but excludes y
    for x in range(m, n+1):     
        total += x
    return total

print(sumFromMToN(5, 10) == 5+6+7+8+9+10)

# Actually, we don't need a loop here...
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
    for x in range(n+1):
        total += x
    return total

print(sumToN(5) == 0+1+2+3+4+5)

# What if we add a third parameter?
def sumEveryKthFromMToN(m, n, k):
    total = 0
    for x in range(m, n+1, k):
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
    for x in range(n, m-1, -2):  # be careful here!
        total += x
    return total

print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))

def sumOfOddsFromMToN(m, n):
    if (m % 2 == 0): m += 1
    return sum(range(m, n+1, 2))

print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))

# This is the worst way so far -- too confusing.
def sumOfOddsFromMToN(m, n):
    return sum(range(m + (1 - m%2), n+1, 2)) # this works, but it's gross!

print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))