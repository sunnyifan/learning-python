# 1. String literals
# 1.1 Four kinds of quotes
# most common: single-quoted or double-quoted strings
print('single-quotes')
print("double-quotes")

# triple-qouted strings
print('''triple single-quotes''')
print("""triple double-quotes""")

# 1.2 New lines in strings
print("abc\ndef")  # \n is a single newline character
print("""abc
def""")            # '''(\) start a new line '''

print("""\
You can use a backslash at the end of a line in a string to exclude
the newline after it. This should almost never be used, but one good
use of it is in this example, at the start of a multi-line string, so
the whole string can be entered with the same indentation (none, that is).
""")

# 1.3 More escape sequences
print("Double-quote: \"")
print("Backslash: \\")
print("Newline (in brackets): [\n]")
print("Tab (in brackets): [\t]")        # \t for tab

print("These items are tab-delimited, 3-per-line:")
print("abc\tdef\tg\nhi\tj\\\tk\n---")

# an escape sequence produces a single character
s = "a\\b\"c\td"
print("s =", s)
print("len(s) =", len(s))       # len for length

s = "a\\b\"cd"
print("s =", s)
print("len(s) =", len(s))       # len(\t) = 1

# 1.4 Concatenated Literals
s = 'abc' 'def'         # ok (but "abc" + "def" is preferred)
print(s)
# error: s = s 'def'(only works with string literals, not variables)

# 1.5 String literals as multi-line comments
"""
Python does not have multiline comments, but you can do something similar
by using a top-level multiline string, such as this. Technically, this is
not a comment, and Python will evaluate this string, but then ignore it
and garbage collect it!
"""
print("wow!")

# 2. Some String Constants:
import string
print(string.ascii_letters)   # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
print("-----------")
print(string.ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)          # 0123456789
print("-----------")
print(string.punctuation)     # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
print(string.printable)       # digits + letters + punctuation + whitespace
print("-----------")
print(string.whitespace)      # space + tab + linefeed + return + ...

# 3. Some String Operators
# 3.1  String + and *
print("abc" + "def")
print("abc" * 3)
# print("abc" + 3)   error: invalid combination

# 3.2 The in operator:
print("ring" in "strings")
print("wow" in "amazing!")
print("Yes" in "yes!")
print("" in "No way!")

# 3.3 String indexing and slicing
# 3.3.1 Indexing a single character
s = "abcdefgh"
print(s)
print(s[0])         # index from left to right, leftmost = [0]
print(s[1])
print(s[2])

print("-----------")
print(s[len(s)-1])
# print(s[len(s)])  # crashes (index out of range)

# 3.3.2 Negative indexes
s = "abcdefgh"
print(s)
print(s[-1])        # Counting backwards, -1 = last char
print(s[-2])

# 3.3.3 Slicing a range of characters
s = "abcdefgh"
print(s)
print(s[0:3])       # number of char indexed = difference between range
print(s[1:3])       # iow, ] not indexed, [ indexed
print("-----------")
print(s[2:3])
print(s[3:3])

# 3.3.4 Slicing with default parameters
s = "abcdefgh"
print(s)
print(s[3:])        # 4th to the last
print(s[:3])        # still ] not inclusive
print(s[:])

# 3.3.5 Slicing with a step parameter
print("This is not as common, but perfectly ok.")
s = "abcdefgh"
print(s)
print(s[1:7:2])
print(s[1:7:3])

# 3.3.6 Reversing a string
s = "abcdefgh"

print("This works, but is confusing:")
print(s[::-1])

print("This also works, but is still confusing:")
print("".join(reversed(s)))

print("Best way: write your own reverseString() function:")

def reverseString(s):
    return s[::-1]

print(reverseString(s))



