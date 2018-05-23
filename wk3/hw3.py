#################################################
# Hw3
#################################################

from cs112_f16_wk3 import assertEqual, assertAlmostEqual, lintAll, testAll
import math, string

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

def patternedMessage(msg, pattern):
    msg = msg.replace(' ', '')
    pattern = pattern.strip('\n')

    i = 0
    s = 0
    output = ''
    while i < len(pattern):
        if pattern[i] in string.whitespace:
            output += pattern[i]
        else:
            output += msg[s]
            s = (s + 1) % len(msg)
        i += 1
    return output

def encodeRightLeftCipher(text, rows):
    colums = (len(text) // rows) + 1
    text = text + string.ascii_lowercase[::-1]
    output = str(rows)
    i = 0
    s = 0
    tracker = 0
    line = ''
    while i < rows:
        while s <= (colums - 1) * 4:
            line += text[i + s]
            s += rows
        if tracker % 2 == 0:
            output += line
        else:
            output += line[::-1]
        tracker += 1
        i += 1
        s = 0
        line = ''
    return output

def decodeRightLeftCipher(cipher):
    return 42

###### BONUS #######
def topLevelFunctionNames(code): return 42
def getEvalSteps(expr): return 42
def bonusEncode1(msg): return 42
def bonusDecode1(msg): return 42
def bonusEncode2(msg): return 42
def bonusDecode2(msg): return 42
def bonusEncode3(msg): return 42
def bonusDecode3(msg): return 42

#################################################
# Test Functions
#################################################

def testEncodeRightLeftCipher():
    print("Testing encodeRightLeftCipher()...", end="")
    text = "WEATTACKATDAWN"
    rows = 4
    # W T A W
    # E A T N
    # A C D z
    # T K A y
    rightLeft = "4"+"WTAWNTAEACDzyAKT"
    cipher = encodeRightLeftCipher(text, rows)
    assertEqual(rightLeft, cipher)
    print("passed!")

def testDecodeRightLeftCipher():
    print("testing decodeRightLeftCipher()...", end="")
    text = "WEATTACKATDAWN"
    rows = 6
    cipher = encodeRightLeftCipher(text, rows)
    plaintext = decodeRightLeftCipher(cipher)
    assertEqual(plaintext, text)
    print("passed!")

def testPatternedMessage():
    print("Testing patternedMessage()...", end="")
    parms = [
    ("Go Pirates!!!", """
***************
******   ******
***************
"""),
    ("Three Diamonds!","""
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
"""),
    ("Go Steelers!","""
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$'$$$$$$'           o$$$
               $$$$o                                o$$$'
                '$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
                     '$$$$$oooo  '$$$o$$$$$$$$$'
                        '$$$$$$$oo $$$$$$$$$$
                                '$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$'
                                      '$$$'
""")]
    solns = [
"""
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
"""
,
"""
    T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
    m     o     n
"""
,
"""
                          GoSteelers!GoSteeler
                      s!GoSteelers!GoSteelers!GoS
                   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
  oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
  s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
    GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
   eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
   rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
  rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
  !GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
            elers     !GoSteelers!GoSteelers!         GoS
              teel          ers!GoSteel           ers!
               GoSte                                elers
                !GoSte      elers!GoSteele        rs!Go
                  Steelers     !GoSteelers!   GoStee
                     lers!GoSte  elers!GoSteeler
                        s!GoSteele rs!GoSteel
                                ers!GoSteele
                                    rs!GoSteeler
                                     s!GoSteeler
                                      s!GoS
"""
    ]
    parms = [("A-C D?", """
*** *** ***
** ** ** **
"""),
    ("A", "x y z"),
    ("The pattern is empty!", "")
    ]
    solns = [
"""
A-C D?A -CD
?A -C D? A-
""",
"A A A",
""
    ]
    for i in range(len(parms)):
        (msg,pattern) = parms[i]
        soln = solns[i]
        soln = soln.strip("\n")
        observed = patternedMessage(msg, pattern)
        #observed = patternedMessage(msg, pattern).strip("\n")
        #print "\n\n***********************\n\n"
        #print msg, pattern
        #print "<"+patternedMessage(msg, pattern)+">"
        #print "<"+soln+">"
        assertEqual(observed, soln)
    print("Passed!")

def testTopLevelFunctionNames():
    print("Testing topLevelFunctionNames()...", end="")

    # no fn defined
    code = """\
# This has no functions!
# def f(): pass
print("Hello world!")
"""
    assertEqual(topLevelFunctionNames(code), "")

    # f is redefined
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    assertEqual(topLevelFunctionNames(code), "f.g")

    # def not at start of line
    code = """\
def f(): return "def g(): pass"
"""
    assertEqual(topLevelFunctionNames(code), "f")

    # g() is in triple-quotes (''')
    code = """\
def f(): return '''
def g(): pass'''
"""
    assertEqual(topLevelFunctionNames(code), "f")

    # g() is in triple-quotes (""")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assertEqual(topLevelFunctionNames(code), "f")

    # triple-quote (''') in comment
    code = """\
def f(): return 42 # '''
def g(): pass # '''
"""
    assertEqual(topLevelFunctionNames(code), "f.g")

    # triple-quote (""") in comment
    code = '''\
def f(): return 42 # """
def g(): pass # """
'''
    assertEqual(topLevelFunctionNames(code), "f.g")

    # comment character (#) in quotes
    code = """\
def f(): return '#' + '''
def g(): pass # '''
def h(): return "#" + '''
def i(): pass # '''
def j(): return '''#''' + '''
def k(): pass # '''
"""
    assertEqual(topLevelFunctionNames(code), "f.h.j")
    print("Passed!")

def testGetEvalSteps():
    print("Testing getEvalSteps()...", end="")
    assertEqual(getEvalSteps("0"), "0 = 0")
    assertEqual(getEvalSteps("2"), "2 = 2")
    assertEqual(getEvalSteps("3+2"), "3+2 = 5")
    assertEqual(getEvalSteps("3-2"), "3-2 = 1")
    assertEqual(getEvalSteps("3**2"), "3**2 = 9")
    assertEqual(getEvalSteps("31%16"), "31%16 = 15")
    assertEqual(getEvalSteps("31*16"), "31*16 = 496")
    assertEqual(getEvalSteps("32//16"), "32//16 = 2")
    assertEqual(getEvalSteps("2+3*4"), "2+3*4 = 2+12\n      = 14")
    assertEqual(getEvalSteps("2*3+4"), "2*3+4 = 6+4\n      = 10")
    assertEqual(getEvalSteps("2+3*4-8**3%3"), """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")
    assertEqual(getEvalSteps("2+3**4%2**4+15//3-8"), """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    print("Passed!")

import random

def testBonusDecode(testFn, encodeFn, decodeFn):
    print("Testing " + testFn + "...", end="")
    s1 = ""
    for c in range(15):
        if (random.random() < 0.80):
            s1 += random.choice(string.ascii_letters)
        else:
            s1 += random.choice(" \n\n") + random.choice(string.digits)
    for s in ["a", "abc", s1]:
        assertEqual(decodeFn(encodeFn(s)), s)
    print("Passed!")

def testBonusDecode1():
    testBonusDecode("testBonusDecode1", bonusEncode1, bonusDecode1)

def testBonusDecode2():
    testBonusDecode("testBonusDecode2", bonusEncode2, bonusDecode2)

def testBonusDecode3():
    testBonusDecode("testBonusDecode3", bonusEncode3, bonusDecode3)

#################################################
# Main
#################################################

def main():
    lintAll()
    testAll(
        testPatternedMessage,
        testEncodeRightLeftCipher,
        testDecodeRightLeftCipher,
        testTopLevelFunctionNames,
        testGetEvalSteps,
        testBonusDecode1,
        testBonusDecode2,
        testBonusDecode3,
    )

if __name__ == '__main__':
    main()
