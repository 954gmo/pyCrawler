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

sentence = 'This is a sample string'
# check if 'sentence' contains the given search string
'is' in sentence  # T
'xyz' in sentence  # F
bool(re.search(r'is', sentence))    # T
bool(re.search(r'xyz', sentence))   # F
bool(re.search(r'this', sentence, flags=re.I))  # T

# re.search in conditional expressions
if re.search(r'ring', sentence):
    print('mission success')

if not re.search(r'xyz', sentence):
    print('mission failed')

words = ['cat', 'attempt', 'tattle']
[w for w in words if re.search(r'tt', w)]   # ['attempt', 'tattle']
all(re.search(r'at', w) for w in words)  # T
any(re.search(r'stat', w) for w in words)   # F

greeting = 'Have a nice weekend'
re.sub(r'e', 'E', greeting)     # 'HavE a nicE wEEkEnd'
re.sub(r'e', 'E', greeting, count=2)    # 'HavE a nicE weekend'

pet = re.compile(r'dog')
type(pet)
bool(pet.search('They bought a dog'))   # T
bool(pet.search('a cat crossed their path'))    # F
pet.sub('cat', 'They bought a dog')

word = re.compile(r'is')
bool(word.search(sentence, 4))  # T
bool(word.search(sentence, 2, 4))   # T

byte_data = b'This is a sample string'
bool(re.search(rb'is', byte_data))

