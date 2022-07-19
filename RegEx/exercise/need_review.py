# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import re

# https://learnbyexample.github.io/py_regular_expressions/character-class.html
# m) For the given list, filter all elements containing any number sequence greater than 624.



# pat = re.compile(r'0*(\d+[\.]?\d+)')
# # [m[0] for m in [m_iter for m_iter in [pat.finditer(w) for w in items]]]
# for w in items:
#     for m in pat.finditer(w):
#         if float(m[1]) > 624:
#             print(m[1])

# [m[1] for m in [pat.finditer(w) for w in items]]

items = ['hi0000432abcd', 'car00625', '42_624 0512', '3.14 96 2 foo1234baz']
[e for e in items if any(float(m[0])>624 for m in re.finditer(r'\d+', e))]

# n) Count the maximum depth of nested braces for the given strings.
# Unbalanced or wrongly ordered braces should return -1.
# Note that this will require a mix of regular expressions and Python code.


def max_nested_braces(ip):
    count = 0
    while True:
        ip, no_of_subs = re.subn(r'\{[^{}]*\}', '', ip)
        if no_of_subs == 0:
            break
        count += 1
    if re.search(r'[{}]', ip):
        return -1
    return count


# replace __ with _ and delete _ if it is alone
re.sub(r'(_)?_', r'\1', '_foo_ __123__ _baz_')

if __name__ == "__main__":
    print(max_nested_braces('a*b'))
    print(max_nested_braces('}a+b{'))
    print(max_nested_braces('a*b+{}'))
    print(max_nested_braces('{{a+2}*{b+c}+e}'))
    print(max_nested_braces('{{a+2}*{b+{c*d}}+e}'))
    print(max_nested_braces('{{a+2}*{\n{b+{c*d}}+e*d}}'))
    print(max_nested_braces('a*{b+c*{e*3.14}}}'))
    