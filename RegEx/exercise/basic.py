# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

"""
REF: https://www.w3schools.com/python/python_regex.asp
   
    RegEx functions
    findall(): 
        return a list containing all matches
    search():
        return a Match object if there is a match anywhere in the string
    split():
        Returns a list where the string has been split at each match
    sub():
        
RegEx functions        
MetaCharacters
Special Sequences
Sets

Match Object
    an object containing information about the search and results
    - .span(),  returns a tuple containing the start-, and end positions of the match
    - 

[] : 
    - a set of characters 
    - "[a-m]"
\: 
    - signal a special sequence(can also be used to 
"""

import re

txt = "the rain in Spain"
x = re.search("^the.*Spain$", txt)
print(x)    # <re.Match object; span=(0, 17), match='the rain in Spain'>
x = re.search("^The.*Spain$", txt)
print(x)    # None

x = re.search(' ', txt)
print(f"the first white-space character is located in position : {x.start()} ")

x = re.findall('ai', txt)
print(x)  # ['ai', 'ai']
x = re.findall('Portugal', txt)
print(x)  # []

txt = "the,train,in,Spain,"
x = re.split("", txt)
print(x)
x = re.split(',', txt)
print(x)
txt = txt.replace(',', " ")
print(txt)
x = re.split("\s", txt)
print(x)
x = re.sub("\s", "9", txt)
print(x)
x = re.sub(" ", "7", txt, 2)
print(x)

x = re.search(' ', txt)
print(x.span())
print(x.string)
x = re.search(r'\bS\w+', txt)
print(x.span())
print(x.group())

if __name__ == "__main__":
    pass
