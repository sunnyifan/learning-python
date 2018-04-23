# 1. String literals
# most common: single-quoted or double-quoted strings
print('single-quotes')
print("double-quotes")

# triple-qouted strings
print('''triple single-quotes''')
print("""triple double-quotes""")

# 2. New lines in strings
print("abc\ndef")  # \n is a single newline character
print("""abc
def""")            # '''(\) start a new line '''

print("""\
You can use a backslash at the end of a line in a string to exclude
the newline after it. This should almost never be used, but one good
use of it is in this example, at the start of a multi-line string, so
the whole string can be entered with the same indentation (none, that is).
""")

# 3. More escape sequences
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

# 4. Concatenated Literals
s = 'abc' 'def'         # ok (but "abc" + "def" is preferred)
print(s)
# error: s = s 'def'(only works with string literals, not variables)

# 5. String literals as multi-line comments
"""
Python does not have multiline comments, but you can do something similar
by using a top-level multiline string, such as this. Technically, this is
not a comment, and Python will evaluate this string, but then ignore it
and garbage collect it!
"""
print("wow!")