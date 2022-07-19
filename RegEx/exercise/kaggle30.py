# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

# https://www.kaggle.com/code/albeffe/regex-exercises-solutions/notebook

import re


def contains_only_a_certain_set_of_characters(txt):
    char_re = re.compile(r'[a-zA-Z0-9]')
    return bool(re.search(char_re, txt))


def a_followed_by_zero_or_more_b(txt):
    char_re = re.compile(r'ab*')
    return bool(re.search(char_re, txt))


def a_followed_by_one_or_more_b(txt):
    char_re = re.compile(r'ab+')
    return bool(re.search(char_re, txt))


def a_followed_by_zero_or_one_b(txt):
    char_re = 'ab{0,1}'
    print(re.search('ab{0,1}', txt))
    return bool(re.search(char_re, txt))


if __name__ == "__main__":
    # print(contains_only_a_certain_set_of_characters(txt='ABCDEFabcdef123450{$'))
    # print(contains_only_a_certain_set_of_characters(txt='{$@'))
    # print(a_followed_by_zero_or_more_b('sdfsd'))
    # print(a_followed_by_zero_or_more_b('abbcc'))
    # print(a_followed_by_zero_or_more_b('a'))
    # print(a_followed_by_one_or_more_b('a'))
    # print(a_followed_by_one_or_more_b('bab'))
    # print(a_followed_by_zero_or_one_b('a'))
    print(a_followed_by_zero_or_one_b('abbcc'))