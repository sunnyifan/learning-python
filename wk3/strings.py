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
def""")

print("""\
You can use a backslash at the end of a line in a string to exclude
the newline after it. This should almost never be used, but one good
use of it is in this example, at the start of a multi-line string, so
the whole string can be entered with the same indentation (none, that is).
""")