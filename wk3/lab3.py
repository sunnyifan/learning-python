#################################################
# Lab3
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

def leastFrequentLetters(s):
    if len(s) == 0:
        return ''
    s = s.lower()
    alpha = string.ascii_lowercase
    i = 0
    minCount = 1000
    output = ''
    while i < 26:
        count = s.count(alpha[i])
        if minCount > count > 0:
            minCount = count
            output = alpha[i]
        elif minCount == count:
            output += alpha[i]
        i += 1
    if output == '':
        return output
    return output

def bestStudentAndAvg(gradebook):
    max_avg = -100
    output = ''
    for line in gradebook.splitlines():
        if line.startswith('#') or line == '':
            continue
        total = 0
        num_of_subjects = 0
        name = line.split(',')[0]
        scores = line.split(',')[1:]
        for factor in scores:
                num_of_subjects += 1
                total += int(factor)
                avg = total // num_of_subjects
        if max_avg <= avg:
            max_avg = avg
            best_student = name
            output = best_student + ':' + str(max_avg)
    return output

#################################################
# Test Functions
#################################################

def testLeastFrequentLetters():
    print('Testing leastFrequentLetters()... ', end='')
    assertEqual(leastFrequentLetters('abc def! GFE"cag!!!'), 'bd')
    assertEqual(leastFrequentLetters('abc def! GFE"cag!!!'.lower()), 'bd')
    assertEqual(leastFrequentLetters('abc def! GFE"cag!!!'.upper()), 'bd')
    assertEqual(leastFrequentLetters(''), '')
    assertEqual(leastFrequentLetters(string.punctuation), '')
    assertEqual(leastFrequentLetters(string.whitespace), '')
    assertEqual(leastFrequentLetters(string.ascii_lowercase),
                string.ascii_lowercase)
    assertEqual(leastFrequentLetters(string.ascii_uppercase),
                string.ascii_lowercase)
    noq = string.ascii_lowercase.replace('q','')
    nor = string.ascii_lowercase.replace('r','')
    nos = string.ascii_lowercase.replace('s','')
    assertEqual(leastFrequentLetters(string.ascii_lowercase + noq), 'q')
    assertEqual(leastFrequentLetters(nor + string.ascii_lowercase), 'r')
    assertEqual(leastFrequentLetters(nos + nor + ' aaa ' +
                                     5*string.ascii_lowercase), 'rs')
    print('Passed.')

def testBestStudentAndAvg():
    print("Testing bestStudentAndAvg()...", end="")
    gradebook = """
# ignore  blank lines and lines starting  with  #'s
wilma,91,93
fred,80,85,90,95,100
betty,88
"""
    assertEqual(bestStudentAndAvg(gradebook), "wilma:92")
    gradebook   =   """
#   ignore  blank   lines   and lines   starting    with    #'s
wilma,93,95

fred,80,85,90,95,100
betty,88
"""
    assertEqual(bestStudentAndAvg(gradebook), "wilma:94")
    gradebook = "fred,0"
    assertEqual(bestStudentAndAvg(gradebook), "fred:0")
    gradebook = "fred,-1\nwilma,-2"
    assertEqual(bestStudentAndAvg(gradebook), "fred:-1")
    gradebook = "fred,100"
    assertEqual(bestStudentAndAvg(gradebook), "fred:100")
    gradebook = "fred,100,110"
    assertEqual(bestStudentAndAvg(gradebook), "fred:105")
    gradebook = "fred,49\nwilma" + ",50"*50
    assertEqual(bestStudentAndAvg(gradebook), "wilma:50")
    print("Passed!")

#################################################
# Main
#################################################

def main():
    lintAll()
    testAll(
        testLeastFrequentLetters,
        testBestStudentAndAvg,
    )

if __name__ == '__main__':
    main()
