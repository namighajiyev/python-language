print('"Isn\'t," she said.')  # "Isn't," she said.
s = 'First line.\nSecond line.'
print(s)
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

sconcat = 3 * 'un' + 'ium'
print(sconcat)

sconcat2 = 'Py' 'thon'
print(sconcat2)

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

word = 'Python'
word[0]  # character in position 0
word[5]  # character in position 5

word[-1]  # last character
#'n'
word[-2]  # second-last character
#'o'
word[-6]
#'P'
word[0:2]  # characters from position 0 (included) to 2 (excluded)
#'Py'
word[2:5]  # characters from position 2 (included) to 5 (excluded)
#'tho'
word[:2] + word[2:]
#'Python'
word[:4] + word[4:]
#'Python'
#word[42]  # the word only has 6 characters IndexError: string index out of range

# out of range slice indexes are handled gracefully when used for slicing
word[4:42]
#'on'
word[42:]
#''
# Python strings cannot be changed — they are immutable.
#word[0] = 'J'

# TypeError: 'str' object does not support item assignment
#word[2:] = 'py'
# TypeError: 'str' object does not support item assignment
a = 'J' + word[1:]
#'Jython'
word[:2] + 'py'
#'Pypy'

s = 'supercalifragilisticexpialidocious'
l = len(s)  # 34
