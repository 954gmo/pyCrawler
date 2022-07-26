# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

# https://docs.python.org/3/library/re.html

"""
re.Match
re.Pattern

re.Pattern <= re.compile(pattern, flags=0)

# performing matches
re.Match <= re.search(pattern, string, flags=0)
re.Match <= re.Pattern.search(string[, pos [, endpos])

# modifying string
str <= re.sub(pattern, repl, string, count=0, flags=0)
(str, n) <= re.Pattern.sub(repl, string, count=0, flags=0)





"""

import re

# ---------------- 3 ----------------

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

# ------------- 4 -------------

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
