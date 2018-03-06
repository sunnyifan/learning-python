# 1. for loops
def sumFromMToN(m, n):
    total = 0
    # note that range(x, y) includes x but excludes y
    for x in range(m, n+1):     # m inlcusive, n+1 exclusive
        total += x
    return total

print(sumFromMToN(5, 10) == 5+6+7+8+9+10)

# Actually, we don't need a loop here...
def sumFromMToN(m, n):
    return sum(range(m, n+1))

print(sumFromMToN(5, 10) == 5+6+7+8+9+10)

# And we can even do this with a closed-form formula,
# which is the fastest way, but which doesn't really
# help us demonstrate loops.  :-)

def sumToN(n):
    # helper function
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