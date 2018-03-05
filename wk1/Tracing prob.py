#Tracing problems
import math
def p(x): print(x, end='   ') # prints and stays on same line
p(3 - 1 + 2 * 6 // 5)
p(3 - 1 + 2 * 6 / 5)
p(2**4/10 + 2**4//10)
p(max(8/3,math.ceil(8/3)))
print()


# Note: we provide roundHalfUp and roundHalfEven for you. 
# Use these instead of the builtin round function, since that
# function may not behave as you expect.

import decimal
def roundHalfUp(d):
   # Round to nearest with ties going away from zero.
   rounding = decimal.ROUND_HALF_UP
   return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def roundHalfEven(d):
   # Round to nearest with ties going to nearest even integer.
   rounding = decimal.ROUND_HALF_EVEN
   return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def p(x): print(x, end='   ') # prints and stays on same line
p(round(1.5))
p(roundHalfUp(1.5))
p(roundHalfEven(1.5))
print()
p(round(2.5))
p(roundHalfUp(2.5))
p(roundHalfEven(2.5))
print()


def p(x): print(x, end='   ') # prints and stays on same line
def f(x, y):
  if (x > y):
    if (x > 2*y): p('A')
    else: p('B')
  else:
    p('C')
def g(x, y):
  if (abs(x%10 - y%10) < 2): p('D')
  elif (x%10 > y%10): p('E')
  else:
    if (x//10 == y//10): p('F')
    else: p('G')
f(4,2)
f(2,3)
f(5,2)
print()
g(11,14)
g(11,24)
g(207,6)
g(207,5)
print()


def rc1(n):
    if ((n < 0) or (n > 99)): return False
    d1 = n%10
    d2 = n//10
    m = 10*d1 + d2
    return ((m < n) and (n < 12))
    
def rc2(n):
    if ((n <= 0) or (n > 99)): return False
    if (n//2*2 != n): return False
    if (n//5*5 != n): return False
    return (n//7*7 == n)