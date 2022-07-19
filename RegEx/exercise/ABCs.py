# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

"""
ref : 
    https://docs.python.org/3/library/re.html
    https://docs.python.org/3/howto/regex.html#regex-howto
    https://regexone.com/
"""

"""
metacharacter
sequence
set

wildcard Dot . match any single character(letter, digit, whitespace, everything)
    letters
    digits
\d : any digit
\D : any non-digit
.  : any character
\. : period
matching specific characters
    [abc]
excluding specific characters
    [^abc] 
character range
\w <==> [A-Za-z0-9]

repetitions
a{1,3}
a{3}
{m,n} m to n repetition
{m} m repetition.

kleene star, kleene plus
\d* : any number of digit
\d+ : at least one digit
[abc]+ : one or more of any a, b, c
.* : zero or more of any character

characters optional: ? , zero of one of the preceding character or group

whitespace: \t, ,\r,\n, \s

starting and ending : ^, $
match groups: extract information for further processing
nested groups: extract multiple layers of information
conditional
back referencing

negative lookahead (?!)
positive lookahead (?=)
positive lookbehind (?<=)
flags(modifier)
greedy matching
lazy matching

"""

import re


def ABCs():
    txts = ['abcdefg', 'abcde', 'abc']
    for txt in txts:
        print(re.search('abc', txt))


def match_and_skip():
    txts = ['cat.', '896.', '?=+.', 'abc1']  # skip 'abc1'
    pattern = r'...\.'  # or '...\.', '.{3}\.'

    txts = ['can', 'man', 'fan', 'dan', 'ran', 'pan']  # skip the last three strings
    pattern = '[cmf]an'  # or '[^drp]..' or [^drp]an or [cmf].{2}


def match_decimal_num():
    pattern = '^-?\d+(,\d+)?(\.\d+)?(e\d+)?$'

def match_phone_number():
    pattern = '1?[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}'

def match_area_code():
    pattern = '(\d{3})'

def match_email():
    pattern = ''


def match_data_from_uri():
    pattern = '(\w+)://([\w\-\.]+)(:(\d+))?'

def example():
    regex = r'([a-zA-Z]+)\s(\d+)'
    match = re.search(regex, 'June 24, July 4')
    if match:
        print(match.start(), match.end())
        print(match.group(1))


if __name__ == "__main__":
    example()
