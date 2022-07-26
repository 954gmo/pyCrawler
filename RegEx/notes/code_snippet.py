# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

# https://docs.python.org/3/library/re.html
# https://learnbyexample.github.io/py_regular_expressions

"""
re.Match
re.Pattern

re.Pattern <= re.compile(pattern, flags=0)

# performing matches

re.Match <= re.search(pattern, string, flags=0)
re.Match <= re.Pattern.search(string[, pos [, endpos])

re.Match <= re.fullmatch(pattern, string, flags=0)
re.Match <= re.Pattern.fullmatch(string)


# modifying string
str <= re.sub(pattern, repl, string, count=0, flags=0)
(str, n) <= re.Pattern.sub(repl, string, count=0, flags=0)





"""

import re

"""
    ---------------- 3 ----------------
"""

sentence = 'This is a sample string'
# check if 'sentence' contains the given search string
'is' in sentence  # T
'xyz' in sentence  # F
bool(re.search(r'is', sentence))  # T
bool(re.search(r'xyz', sentence))  # F
bool(re.search(r'this', sentence, flags=re.I))  # T

# re.search in conditional expressions
if re.search(r'ring', sentence):
    print('mission success')

if not re.search(r'xyz', sentence):
    print('mission failed')

words = ['cat', 'attempt', 'tattle']
[w for w in words if re.search(r'tt', w)]  # ['attempt', 'tattle']
all(re.search(r'at', w) for w in words)  # T
any(re.search(r'stat', w) for w in words)  # F

greeting = 'Have a nice weekend'
re.sub(r'e', 'E', greeting)  # 'HavE a nicE wEEkEnd'
re.sub(r'e', 'E', greeting, count=2)  # 'HavE a nicE weekend'

pet = re.compile(r'dog')
type(pet)
bool(pet.search('They bought a dog'))  # T
bool(pet.search('a cat crossed their path'))  # F
pet.sub('cat', 'They bought a dog')

word = re.compile(r'is')
bool(word.search(sentence, 4))  # T
bool(word.search(sentence, 2, 4))  # T

byte_data = b'This is a sample string'
bool(re.search(rb'is', byte_data))

# a) Check whether the given strings contain 0xB0
line1 = 'start address: 0xA0, func1 address: 0xC0'
line2 = 'end address: 0xFF, func2 address: 0xB0'
pat = re.compile(r'0xB0')
bool(pat.search(line1))  # F
bool(pat.search(line2))  # T

# b) Replace all occurrences of 5 with five for the given string.
ip = 'They ate 5 apples and 5 oranges'
re.sub(r'5', 'five', ip)

# c) Replace first occurrence of 5 with five for the given string.
re.sub(r'5', 'five', ip, count=1)

# d) For the given list, filter all elements that do not contain e.
items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
[i for i in items if not re.search(r'e', i)]  # ['goal', 'sit']

# e) Replace all occurrences of note irrespective of case with X.
ip = 'This note should not be NoTeD'
re.sub(r'note', 'X', ip, flags=re.I)

# f) Check if at is present in the given byte input data.
ip = b'tiger imp goat'
bool(re.search(rb'at', ip))  # T

# g) For the given input string, display all lines not containing start irrespective of case.
para = '''
        good start
        Start working on that
        project you always wanted
        stars are shining brightly
        hi there
        start and try to
        finish the book
        bye
'''
for p in para.split('\n'):
    if not re.search(r'start', p, flags=re.I):
        print(p.strip())

pat = re.compile(r'start', flags=re.I)
for p in para.split('\n'):
    if not re.search(p):
        print(p.strip())

# h) For the given list, filter all elements that contains either a or w.
items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
[i for i in items if re.search(r'[aw]', i)]

# i) For the given list, filter all elements that contains both e and n.
[i for i in items if re.search(r'e', i) and re.search(r'n', i)]

# j) For the given string, replace 0xA0 with 0x7F and 0xC0 with 0x1F.
ip = 'start address: 0xA0, func1 address: 0xC0'
re.sub(r'0xC0', '0x1F', re.sub(r'0xA0', '0x7F', ip))

"""
 ------------- 4 -------------
"""

bool(re.search(r'\Acat', 'cater'))  # T
bool(re.search(r'\Acat', 'concatenation'))  # F
bool(re.search(r'\Ahi', 'hi hello\ntop spot'))  # T
bool(re.search(r'\Atop', 'hi hello\ntop spot'))  # F
bool(re.search(r'are\Z', 'spare'))  # T
bool(re.search(r'are\Z', 'nearest'))    # F

words = ['surrender', 'unicorn', 'newer', 'door', 'empty', 'eel', 'pest']
[w for w in words if re.search(r'er\Z', w)]
[w for w in words if re.search(r't\Z', w)]

# insert text at the start of a string
re.sub(r'\A', 're', 'live')
re.sub(r'\A', 're', 'send')

# appending text
re.sub(r'\Z', 'er', 'cat')
re.sub(r'\Z', 'er', 'hack')

pat = re.compile(r'\Aat')
bool(pat.search('cater', 1))    # F
bool(pat.search('cater'[1:]))   # T

pat = re.compile(r'cat', flags=re.I)
bool(pat.fullmatch('Cat'))  # T
bool(pat.fullmatch('Scatter'))  # F

pets = 'cat and dog'
bool(re.search(r'^cat', pets))  # T
bool(re.search(r'^dog', pets))  # F
bool(re.search(r'dog$', pets))  # T
bool(re.search(r'^dog$', pets))  # F

greeting = 'hi there\nhave a nice day\n'
bool(re.search(r'day$', greeting))  # T
bool(re.search(r'day\n$', greeting))    # T
bool(re.search(r'day\Z', greeting))     # F
bool(re.search(r'day\n\Z', greeting))   # T

# check if any line in the string starts with 'top'
bool(re.search(r'^top', 'hi hello\ntop spot', flags=re.M))  # T
# check if any line in the string ends with 'ar'
bool(re.search(r'ar$', 'spare\npar\ndare', flags=re.M))     # T

# filter all elements having lines ending with 'are'
elements = ['spare\ntool', 'par\n', 'dare']
[e for e in elements if re.search(r'are$', e, flags=re.M)]

# check if any complete line in the string is 'par'
re.search(r'^par$', 'spare\npar\ndare', flags=re.M)

ip_lines = 'catapults\nconcatenate\ncat'
re.sub(r'^', '* ', ip_lines)
re.sub(r'$', '.', ip_lines)

words = 'par spar apparent spare part'
# replace 'par' irrespective of where it occurs
re.sub(r'par', 'X', words)
# replace 'par' only at start of word
re.sub(r'\bpar', 'X', words)
# replace 'par' only at end of word
re.sub(r'par\b', words)
# replace 'par' only if it is not part of another word
re.sub(r'\bpar\b', words)

words = 'par spar apparent spare part'
re.sub(r'\b', '"', words).replace(' ', ',')
re.sub(r'\b', ' ', '-----hello-----')

# replace 'par' if it is not start of word
re.sub(r'\Bpar', 'X', words)
# replace 'par' at end of word but not whole word 'par'
re.sub(r'\Bpar\b', 'X', words)
# replace 'par' if it is not end of word
re.sub(r'par\B', 'X', words)
# replace 'par' if it is surrounded by word characters
re.sub(r'\Bpar\B', 'X', words)

re.sub(r'\b', ':', 'copper')
re.sub(r'\B', ':', 'copper')

# a) Check if the given strings start with be.
line1 = 'be nice'
line2 = '"best!"'
line3 = 'better?'
line4 = 'oh no\nbear spotted'

pat = re.compile(r'\Abe')
bool(pat.search(line1))
bool(pat.search(line2))
bool(pat.search(line3))
bool(pat.search(line4))

# b) For the given input string, change only whole word red to brown
words = 'bred red spread credible'
re.sub(r'\bred\b', 'brown', words)

# c) For the given input list, filter all elements that contains 42 surrounded by word characters.
words = ['hi42bye', 'nice1423', 'bad42', 'cool_42a', 'fake4b']
[w for w in words if re.search('\B42\B', w)]
# ['hi42bye', 'nice1423', 'cool_42a']

# d) For the given input list, filter all elements that start with den or end with ly.
items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\n', 'dent']
[i for i in items if re.search(r'\Aden|ly\Z', i)]
[i for i in items if re.search(r'\Aden') or re.search(r'ly\Z')]
# ['lovely', '2 lonely', 'dent']

# e) For the given input string, change whole word mall to 1234 only if it is at the start of a line.
para = '''\
ball fall wall tall
mall call ball pall
wall mall ball fall
mallet wallet malls'''
print(re.sub(r'^\bmall\b', '1234', para, flags=re.M))
print(re.sub(r'^mall\b', '1234', para, flags=re.M))


# f) For the given list, filter all elements having a line starting with den or ending with ly.
items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\nfar', 'dent']
[i for i in items if re.search(r'^den|ly$', i, flags=re.M)]
[i for i in items if re.search(r'^den', i, flags=re.M) or re.search(r'ly$', i, flags=re.M)]

# g) For the given input list, filter all whole elements 12\nthree irrespective of case.
items = ['12\nthree\n', '12\nThree', '12\nthree\n4', '12\nthree']
[i for i in items if re.search(r'\A12\nthree\Z', i, flags=re.I)]
[i for i in items if re.fullmatch(r'12\nthree', i, flags=re.I)]

# h) For the given input list, replace hand with X for all elements that start with hand followed by at least one word character.
items = ['handed', 'hand', 'handy', 'unhanded', 'handle', 'hand-2']
[re.sub(r'\Ahand\B', 'X', i) for i in items]
[re.sub(r'\bhand\B', 'X', i) for i in items]

# i) For the given input list, filter all elements starting with h. Additionally, replace e with X for these filtered elements.
items = ['handed', 'hand', 'handy', 'unhanded', 'handle', 'hand-2']
[re.sub(r'e', 'X', i) for i in items if re.search(r'\Ah', i)]

"""
    ---------------- 5 -------------------
"""
# match either 'cat' or 'dog'
bool(re.search(r'cat|dog', 'I like cats'))  # T
# replace either 'cat' at start of string or 'cat' at end of word
re.sub(r'\Acat|cat\b', 'X', 'catapults concatenate cat scat')
# replace either 'cat' or 'dog' or 'fox' with 'mammal'
re.sub(r'cat|dog|fox', 'mammal', 'cat dog bee parrot fox')

'|'.join(['car', 'jeep'])
words = ['cat', 'dog', 'fox']
re.sub('|'.join(words), 'mammal', 'cat dog bee parrot fox')

# without grouping
re.sub(r'reform|rest', 'X', 'red reform read arrest')
re.sub(r'\bpar\b|\bpart\b', 'X', 'par spare part party')
# with grouping
re.sub(r're(form|st)', 'X', 'red reform read arrest')
re.sub(r'\b(par|part)\b', 'X', 'par spare part party')
re.sub(r'\bpar(|t)\b', 'X', 'par spare part party')

words = ['cat', 'par']
# without word boundaries, any matching portion will be replaced
re.sub('|'.join(words), 'X', 'cater cat concatenate par spare')
alt = re.compile(r'\b(' + '|'.join(words) + r')\b')
alt.sub('X', 'cater cat concatenate par spare')

terms = ['no', 'ten', 'it']
items = ['dip', 'nobody', 'it', 'oh', 'no', 'bitten']
pat = re.compile('|'.join(terms))
# matching only whole elements
[i for i in items if pat.fullmatch(i)]
# matching anywhere
[i for i in items if pat.search(i)]

# precedence rule
words = ['hand', 'handy', 'handful']
alt = re.compile('|'.join(sorted(words, key=len, reverse=True)))
alt.sub('X', 'hands handful handed handy')
re.sub('|'.join(words), 'X', 'hands handful handed handy')

# a) For the given input list, filter all elements that start with den or end with ly
items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\n', 'dent']
[i for i in items if re.search(r'\Aden|ly\Z', i)]

# b) For the given list, filter all elements having a line starting with den or ending with ly.
items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\nfar', 'dent']
[i for i in items if re.search(r'^den|ly$', i, flags=re.M)]

# c) For the given input strings, replace all occurrences of removed or reed or received or refused with X.
s1 = 'creed refuse removed read'
s2 = 'refused reed redo received'
pat = re.compile(r're(mov|ceiv|fus|)ed')
pat.sub('X', s1)
pat.sub('X', s2)