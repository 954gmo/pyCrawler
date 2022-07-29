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
    .span(n) : (starting idx, ending+1 idx)
    .start(n)
    .end(n)
    [n]: 0 
    .group(n)
    .groups()
    .string
    .re
    .pos
    .endpos
    
re.Pattern

re.Pattern <= re.compile(pattern, flags=0)

# performing matches

re.Match <= re.search(pattern, string, flags=0)
re.Match <= re.Pattern.search(string[, pos [, endpos])

re.Match <= re.fullmatch(pattern, string, flags=0)
re.Match <= re.Pattern.fullmatch(string)

[str,] or [(str,),]<= re.findall(pattern, string, flags=0)

iterable <= re.finditer(pattern, string, flags=0)

re.Match.expand


# modifying string
str <= re.sub(pattern, repl, string, count=0, flags=0)
(str, n) <= re.Pattern.sub(repl, string, count=0, flags=0)
str <= re.subn(pattern, repl, string, count=0, flags=0)


re.escape
re.split(pattern, string, maxsplit=0, flags=0)



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

# d) For the given input strings, replace all matches from the list words with A.
s1 = 'plate full of slate'
s2 = "slated for later, don't be late"
words = ['late', 'later', 'slated']

pat = re.compile('|'.join(sorted(words, key=len, reverse=True)))
pat.sub('A', s1)
pat.sub('A', s2)

# e) Filter all whole elements from the input list items based on elements listed in words.
items = ['slate', 'later', 'plate', 'late', 'slates', 'slated ']
words = ['late', 'later', 'slated']
pat = re.compile('|'.join(sorted(words, key=len, reverse=True)))
[i for i in items if pat.fullmatch(i)]
# or, remark, whole words : \A \Z, not \b \b
pat = re.compile(r'\A(' + '|'.join(sorted(words, key=len, reverse=True)) + r')\Z')
[i for i in items if pat.search(i)]


"""
    ------------- 6 --------------
"""
bool(re.search(r'b^2', 'a^2 + b^2 - C*3'))      # F
bool(re.search(r'b\^2', 'a^2 + b^2 - C*3'))     # T
re.sub(r'\(|\)', '', '(a*b) + c')
re.sub(r'\\', '/', r'\learn\by\example')

# For real world use cases, ask yourself if regular expressions is needed at all?
eqn = 'f*(a^b) - 3*(a^b)'
eqn.replace('(a^b)', 'c')

# replace only at end of string
expr = '(a^b)'
eqn = 'f*(a^b) - 3*(a^b)'
re.sub(re.escape(expr) + r'\Z', 'c', eqn)

terms = ['a_42', '(a^b)', '2|3']
# using 're.escape' and 'join' to construct the pattern
pat1 = re.compile('|'.join(re.escape(s) for s in terms))
# using only 'join' to construct the pattern
pat2 = re.compile('|'.join(terms))
s = 'ba_423 (a^b)c 2|3 a^b'
pat1.sub('X', s)
pat2.sub('X', s)

# escape sequences
re.sub(r'\t', ':', 'a\tb\tc')
re.sub(r'\n', ' ', '1\n2\n3')
re.search(r'\e', 'hello')

# represent a character using hexadecimal escape of the format \xNN
re.sub(r'\x20', '', 'h e l l o')    # \x20 is space character
re.sub(r'\x7c3', '5', '12|30')      # \x7c is '|' character

# a) Transform the given input strings to the expected output using same logic on both strings.
str1 = '(9-2)*5+qty/3'
str2 = '(qty+4)/2-(9-2)*5+pq/4'
expr = '(9-2)*5'
pat = re.compile(re.escape(expr))
pat.sub('35', str1)
pat.sub('35', str2)

# b) Replace (4)\| with 2 only at the start or end of given input strings.
s1 = r'2.3/(4)\|6 foo 5.3-(4)\|'
s2 = r'(4)\|42 - (4)\|3'
s3 = 'two - (4)\\|\n'

expr = '(4)\|'
pat = re.compile(r'\A' + re.escape(expr) + r'|' + re.escape(expr) + r'\Z')
pat.sub('2', s1)
pat.sub('2', s2)
pat.sub('2', s3)

# c) Replace any matching element from the list items with X for given the input strings.
# Match the elements from items literally.
# Assume no two elements of items will result in any matching conflict.
items = ['a.b', '3+n', r'x\y\z', 'qty||price', '{n}']
pat = re.compile('|'.join([re.escape(i) for i in items]))
pat.sub('X', '0a.bcd')
pat.sub('X', 'E{n}AMPLE')
pat.sub('X', r'43+n2 ax\y\ze')

# d) Replace backspace character \b with a single space character for the given input string.
ip = '123\b456'
re.sub(re.escape('\b'), ' ', ip)

# e) Replace all occurrences of \e with e.
ip = r'th\er\e ar\e common asp\ects among th\e alt\ernations'
re.sub(re.escape('\e'), 'e', ip)

# f) Replace any matching item from the list eqns with X for given the string ip. Match the items from eqns literally.
ip = '3-(a^b)+2*(a^b)-(a/b)+3'
eqns = ['(a^b)', '(a/b)', '(a^b)+2']
pat = re.compile('|'.join(sorted([re.escape(i) for i in eqns], key=len, reverse=True)))
pat.sub('X', ip)

"""
    ------------- 7 -------------
"""

# matches character 'c', any character and then character 't'
re.sub(r'c.t', 'X', 'tac tin cat abc;tuv acute')
# matches character 'r', any two characters and then character 'd'
re.sub(r'r..d', 'X', 'breadth markedly reported overrides')
# matches character '2', any character and then character '3'
re.sub(r'2.3', '8', '42\t35')
# by default, dot metacharacter doesn't match newline character
bool(re.search(r'a.b', 'a\nb'))     # F

# same as: 'apple-85-mango-70'.split('-')
re.split('-', 'apple-85-mango-70')
# maxsplit determines the maximum number of times to split the input
re.split('-', 'apple-85-mango-70', maxsplit=1)

re.split(r':.:', 'bus:3:car:5:van')

# same as: r'ear|ar'
re.sub(r'e?ar', 'X', 'far feat flare fear')
# same as: r'\bpar(t|)\b'
re.sub(r'\bpart?\b', 'X', 'par spare part party')
# same as: r'\b(re.d|red)\b'
words = ['red', 'read', 'ready', 're;d', 'road', 'redo', 'reed', 'rod']
[w for w in words if re.search(r'\bre.?d\b', w)]
# same as: r'part|parrot'
re.sub(r'par(ro)?t', 'X', 'par part parrot parent')
# same as: r'part|parent|parrot'
re.sub(r'par(en|ro)?t', 'X', 'par part parrot parent')

# match 't' followed by zero or more of 'a' followed by 'r'
re.sub(r'ta*r', 'X', 'tr tear tare steer sitaara')
# match 't' followed by zero or more of 'e' or 'a' followed by 'r'
re.sub(r't(e|a)*r', 'X', 'tr tear tare steer sitaara')
# match zero or more of '1' followed by '2'
re.sub(r'1*2', 'X', '3111111111125111142')

# last element is empty because there is nothing after 2 at the end of string
re.split(r'1*2', '3111111111125111142')
re.split(r'1*2', '3111111111125111142', maxsplit=1)

# empty string matches at start and end of string
# it matches between every character
# and, there is an empty match after the split at u
re.split(r'u*', 'cloudy')

re.sub(r'ta+r', 'X', 'tr tear tare steer sitaara')
re.sub(r't(e|a)+r', 'X', 'tr tear tare steer sitaara')

demo = ['abc', 'ac', 'adc', 'abbc', 'xabbbcz', 'bbb', 'bc', 'abbbbbc']
[d for d in demo if re.search(r'ab{1,4}c', d)]
[d for d in demo if re.search(r'ab{3,}c', d)]
[d for d in demo if re.search(r'ab{,2}c', d)]
[d for d in demo if re.search(r'ab{3}c', d)]

# conditional AND
# match 'Error' followed by zero or more characters followed by 'valid'
bool(re.search(r'Error.*valid', 'Error: not a valid input'))
bool(re.search(r'Error.*valid', 'Error: key not found'))

seq1 = 'cat and dog'
seq2 = 'dog and cat'
bool(re.search(r'cat.*dog|dog.*cat', seq1))
# if you just need True/False result, this would be a scalable approach
pat = (r'cat', r'dog')
all(re.search(p, seq1) for p in pat)
all(re.search(p, seq2) for p in pat)

# a more practical example
# prefix '<' with '\' if it is not already prefixed
# both '<' and '\<' will get replaced with '\<'
# note the use of raw string for all the three arguments
re.sub(r'\\?<', r'\<', r'blah \< foo < bar \< blah < baz')

re.sub(r'hand(y|ful)?', 'X', 'hand handy handful')

# non-greedy quantifiers, lazy or reluctant quantifiers
re.sub(r'f.??o', 'X', 'foot')
re.sub(r'.{2,5}?', 'X', '123456789')    # XXXX9
re.split(r':.*?:', 'green:3.14:teal::brown:oh!:blue')

# a) Replace 42//5 or 42/5 with 8 for the given input.
ip = 'a+42//5-c pressure*3+42/5-14256'
# re.sub(r'42/+5', '8', ip)
re.sub(r'42//?5', '8', ip)

# b) For the list items, filter all elements starting with hand and ending with at most one more character or le.
items = ['handed', 'hand', 'handled', 'handy', 'unhand', 'hands', 'handle']
[i for i in items if re.search(r'\Ahand(.|le)?\Z', i)]
[i for i in items if re.search(r'hand(.|le)?', i)]

# c) Use re.split to get the output as shown for the given input strings.
eqn1 = 'a+42//5-c'
eqn2 = 'pressure*3+42/5-14256'
eqn3 = 'r*42-5/3+42///5-42/53+a'

pat = re.compile(r'42//?5')
pat.split(eqn1)     # ['a+', '-c']
pat.split(eqn2)     # ['pressure*3+', '-14256']
pat.split(eqn3)     # ['r*42-5/3+42///5-', '3+a']

# d) For the given input strings, remove everything from the first occurrence of i till end of the string.
s1 = 'remove the special meaning of such constructs'
s2 = 'characters while constructing'
pat = re.compile(r'i.*\Z')
pat = re.compile(r'i.*')
pat.sub('', s1)

# e) For the given strings, construct a RE to get output as shown.
str1 = 'a+b(addition)'
str2 = 'a/b(division) + c%d(#modulo)'
str3 = 'Hi there(greeting). Nice day(a(b)'
pat = re.compile(r'\(.*?\)')
pat.sub('', str1)

# f) Correct the given RE to get the expected output.
words = 'plink incoming tint winter in caution sentient'
p = ['int', 'in', 'ion', 'ing', 'inco', 'inter', 'ink']
pat = re.compile('|'.join(sorted(p, key=len, reverse=True)))
pat = re.compile(r'in(ter|co|g|t|k)?|ion')
pat.sub('X', words)

# g) For the given greedy quantifiers, what would be the equivalent form using {m,n} representation?

# ? is same as {0,1}
# * is same as {0,}
# + is same as {1,}

# i) For the given input strings,
# remove everything from the first occurrence of test (irrespective of case) till end of the string,
# provided test isn't at the end of the string.
s1 = 'this is a Test'
s2 = 'always test your RE for corner cases'
s3 = 'a TEST of skill tests?'
pat = re.compile(r'test.+\Z', flags=re.I)
pat = re.compile(r'test.+', flags=re.I)
pat.sub('', s1)

# j) For the input list words,
# filter all elements starting with s and containing e and t in any order.
words = ['sequoia', 'subtle', 'exhibit', 'asset', 'sets', 'tests', 'site']
# [w for w in words if re.search(r'^s.*[et].*', w)]
[w for w in words if re.search(r'^s.*e.*', w) and re.search(r'^s.*t.*', w)]
[w for w in words if re.search(r'\As.*(e.*t|t.*e)', w)]

# k) For the input list words, remove all elements having less than 6 characters.
words = ['sequoia', 'subtle', 'exhibit', 'asset', 'sets', 'tests', 'site']
[w for w in words if re.search(r'.{6,}', w)]

# l) For the input list words, filter all elements starting with s or t and having a maximum of 6 characters.
words = ['sequoia', 'subtle', 'exhibit', 'asset', 'sets', 'tests', 'site']
[w for w in words if re.search(r'\A[st].{0,5}\Z', w)]
[w for w in words if re.fullmatch(r'[st].{,5}', w)]
[w for w in words if re.fullmatch(r'(s|t).{,5}', w)]

# m) Can you reason out why this code results in the output shown?
# The aim was to remove all <characters> patterns but not the <> ones.
# The expected result was 'a 1<> b 2<> c'.
ip = 'a<apple> 1<> b<bye> 2<> c<cat>'
re.sub(r'<.+?>', '', ip)    # 'a 1 2'
re.sub(r'<\w+?>', '', ip)

# n) Use re.split to get the output as shown below for given input strings.
s1 = 'go there  //   "this // that"'
s2 = 'a//b // c//d e//f // 4//5'
s3 = '42// hi//bye//see // carefully'

pat = re.compile(r'\s+//\s+')

pat.split(s1, maxsplit=1)# ['go there', '"this // that"']
# ['a//b', 'c//d e//f // 4//5']
# ['42// hi//bye//see', 'carefully']

"""
    --------------- 9 -------------------
"""

# assignment expressions
if m := re.search(r'(.*)s', 'oh!'):
    print(m[1])

text = ['type: fruit', 'date: 2020/04/28']
for ip in text:
    if m := re.search(r'type: (.*)', ip):
        print(m[1])
    elif m := re.search(r'date: (.*?)/(.*?)/', ip):
        print(f'month: {m[2]}, year: {m[1]}')

# using functions in replacement section
# an re.Match object will be passed to the function as argument
re.sub(r'(a|b)\^2', lambda m: m[0].upper(), 'a^2 + b^2 - C*3')
re.sub(r'2|3', lambda m: str(int(m[0])**2), 'a^2 + b^2 - C*3')

# using dict in replacement section
# one to one mappings
d = {'1': 'one', '2': 'two', '4': 'four'}
re.sub(r'1|2|4', lambda m: d[m[0]], '9234012')

# if the matched text doesn't exist as a key, default value will be used
re.sub('\d', lambda m: d.get(m[0], 'X'), '9234012')

swap = {'cat': 'tiger', 'tiger': 'cat'}
words = 'cat tiger dog tiger cat'
re.sub(r'cat|tiger', lambda m: swap[m[0]], words)

# note that numbers have been converted to strings here
# otherwise, you'd need to convert it in the lambda code
d = {'hand': '1', 'handy': '2', 'handful': '3', 'a^b': '4'}
words = sorted(d.keys(), key=len, reverse=True)
pat = re.compile('|'.join(re.escape(s) for s in words))
pat.sub(lambda m: d[m[0]], 'handful hand pin handy (a^b)')

re.findall(r'ab*c', 'abc ac adc abbbc')
re.findall(r'\bs?pare?\b', 'PAR spar apparent SpArE part pare', flags=re.I)
re.findall(r'ab*c', 'abc ac adc abbc xabbbcz bbb bc abbbbbc')

# with capture group(s)
re.findall(r'a(b*)c', 'abc ac adc abbc xabbbcz bbb bc abbbbbc')
re.findall(r'a(?:b*)c', 'abc ac adc abbc xabbbcz bbb bc abbbbbc')
re.findall(r'(.*?)/(.*?)/(.*?),', '2020/04/25,1986/Mar/02,77/12/31')

re.finditer(r'ab+c', 'abc ac adc abbbc')

# each element is a re.Match object corresponding to the matched portion
m_iter = re.finditer(r'ab+c', 'abc ac adc abbbc')
for m in m_iter:
    print(m)

d = '2020/04/25,1986/Mar/02,77/12/31'
m_iter = re.finditer(r'(.*?)/(.*?)/(.*?),', d)
[m.groups() for m in m_iter]

# to include the matching portions of the pattern as well in the output
re.split(r'(1*4?2)', '31111111111251111426')
# without capture group
re.split(r'1*4?2', '31111111111251111426')
# here 4?2 is outside capture group, so that portion won't be in output
re.split(r'(1*)4?2', '31111111111251111426')
# multiple capture groups example
# note that the portion matched by b+ isn't present in the output
re.split(r'(a+)b+(c+)', '3.14aabccc42')
# here (4)? matches zero times on the first occasion
re.split(r'(1*)(4)?2', '31111111111251111426')
['3', '1111111111', None, '5', '1111', '4', '6']

# Use of capture groups and maxsplit=1 gives behavior similar to str.partition(separator) method.
# first element is portion before the first match
# second element is portion matched by the pattern itself
# third element is rest of the input string
re.split(r'(a+b+c+)', '3.14aabccc42abc88', maxsplit=1)
['3.14', 'aabccc', '42abc88']

greeting = 'Have a nice weekend'
re.subn(r'e', 'E', greeting)

word = 'coffining'
# recursively delete 'fin'
while True:
    word, cnt = re.subn(r'fin', '', word)
    if cnt == 0:
        break

# a) For the given strings, extract the matching portion from first is to last t.
str1 = 'This the biggest fruit you have seen?'
str2 = 'Your mission is to read and practice consistently'
pat = re.compile(r'(is.*t)')
pat.search(str1)[0]

# b) Find the starting index of first occurrence of is or the or was or to for the given input strings.
s1 = 'match after the last newline character'
s2 = 'and then you want to test'
s3 = 'this is good bye then'
s4 = 'who was there to see?'
pat = re.compile(r'(the|was|is|to)')
pat.search(s1).start(1)

# c) Find the starting index of last occurrence of is or the or was or to for the given input strings.
s1 = 'match after the last newline character'
s2 = 'and then you want to test'
s3 = 'this is good bye then'
s4 = 'who was there to see?'

pat = re.compile(r'.*(the|was|is|to)')
pat.search(s1).start(1)

# d) The given input string contains : exactly once. Extract all characters after the : as output.
ip = 'fruits:apple, mango, guava, blueberry'
re.search(r':(.*)', ip)[1]

# e) The given input strings contains some text followed by - followed by a number.
# Replace that number with its log value using math.log().
import math
s1 = 'first-3.14'
s2 = 'next-123'
pat = re.compile(r'-(\d+[.]?\d+)')
pat.sub(lambda m: '-' + str(math.log(float(m[1]))), s1)

# f) Replace all occurrences of par with spar, spare with extra and park with garden for the given input strings.
str1 = 'apartment has a park'
str2 = 'do you have a spare cable'
str3 = 'write a parser'
d = {"par": "spar", "spare": "extra", "park": "garden"}
pat = re.compile(r"(" + "|".join(sorted([k for k in d.keys()], key=len, reverse=True)) + r')')
pat.sub(lambda m: d[m[1]], str1)

# g) Extract all words between ( and ) from the given input string as a list.
# Assume that the input will not contain any broken parentheses.
ip = 'another (way) to reuse (portion) matched (by) capture groups'
re.findall(r'\((.*?)\)', ip)

# h) Extract all occurrences of < up to next occurrence of >,
# provided there is at least one character in between < and >.
ip = 'a<apple> 1<> b<bye> 2<> c<cat>'
re.findall(r'(<.+?>)', ip)

# i) Use re.findall to get the output as shown below for the given input strings.
# Note the characters used in the input strings carefully.
row1 = '-2,5 4,+3 +42,-53 4356246,-357532354 '
row2 = '1.32,-3.14 634,5.63 63.3e3,9907809345343.235 '

pat = re.compile(r'(.*?),(.*?) ')
pat.findall(row1)

# j) This is an extension to previous question.
# For row1, find the sum of integers of each tuple element. For example, sum of -2 and 5 is 3.
# For row2, find the sum of floating-point numbers of each tuple element. For example, sum of 1.32 and -3.14 is -1.82.
[int(p[0]) + int(p[1]) for p in pat.findall(row1)]
[float(p[0]) + float(p[1]) for p in pat.findall(row2)]

# k) Use re.split to get the output as shown below.
ip = '42:no-output;1000:car-truck;SQEX49801'
# ['42', 'output', '1000', 'truck', 'SQEX49801']
re.split(r';|:.*?-', ip)
re.split(r':.+?-(.+?);', ip)

# l) For the given list of strings,
# change the elements into a tuple of original element and number of times t occurs in that element.
words = ['sequoia', 'attest', 'tattletale', 'asset']
[(w, re.subn(r't', '', w)[1]) for w in words]
[re.subn(r't', '', w) for w in words]

# m) The given input string has fields separated by :.
# Each field contains four uppercase alphabets followed optionally by two digits.
# Ignore the last field, which is empty.
# See docs.python: Match.groups and use re.finditer to get the output as shown below.
# If the optional digits aren't present, show 'NA' instead of None.
ip = 'TWXA42:JWPA:NTED01:'
# [('TWXA', '42'), ('JWPA', 'NA'), ('NTED', '01')]
[m.groups(default='NA') for m in re.finditer(r'(\w{4})(\d\d)?:')]
[m.groups(default='NA') for m in re.finditer(r'(.{4})(..)?:')]

# n) Convert the comma separated strings to corresponding dict objects as shown below.
row1 = 'name:rohan,maths:75,phy:89,'
row2 = 'name:rose,maths:88,phy:92,'
pat = re.compile(r'(.*?):(.*?),')
# {'name': 'rohan', 'maths': '75', 'phy': '89'}
{m[1]:m[2] for m in pat.finditer(row1)}
# {'name': 'rose', 'maths': '88', 'phy': '92'}

"""
    -------------- 10 -------------------
"""
words = ['cute', 'cat', 'cot', 'coat', 'cost', 'scuttle']
# same as: r'cot|cut' or r'c(o|u)t'
[w for w in words if re.search(r'c[ou]t', w)]
# same as: r'(a|e|o)+t'
re.sub(r'[aeo]+t', 'X', 'meeting cute boat site foot')

re.findall(r'[0-9]+', 'Sample123string42with777numbers')

# whole words made up of lowercase alphabets and digits only
re.findall(r'\b[a-z0-9]+\b', 'coat Bin food tar12 best')

# whole words made up of lowercase alphabets, but starting with 'p' to 'z'
re.findall(r'\b[p-z][a-z]*\b', 'coat tin food put stoop best')

# whole words made up of only 'a' to 'f' and 'p' to 't' lowercase alphabets
re.findall(r'\b[a-fp-t]+\b', 'coat tin food put stoop best')

# all non-digits
re.findall(r'[^0-9]+', 'Sample123string42with777numbers')
re.findall(r'\D+', 'Sample123string42with777numbers')

# remove first two columns where : is delimiter
re.sub(r'\w+?:', '', 'foo:123:bar:baz', count=2)
re.sub(r'\A([^:]+:){2}', '', 'foo:123:bar:baz', count=1)

# deleting characters at end of string based on a delimiter
'foo=42; baz=123'
re.sub(r'=[^=]+\Z', '', 'foo=42; baz=123')

dates = '2020/04/25,1986/Mar/02,77/12/31'
# Note that the third character set negates comma as well
# and comma is matched optionally outside the capture groups
re.findall(r'([^/]+)/([^/]+)/([^/,]+),?', dates)

words = ['tryst', 'fun', 'glyph', 'pity', 'why']
# words not containing vowel characters
[w for w in words if re.fullmatch(r'[^aeiou]+', w)]
[w for w in words if re.search(r'\A[^aeiou]+\Z', w)]
[w for w in words if not re.search(r'[aeiou]', w)]

# - should be first or last character or escaped using \.
re.findall(r'\b[a-z-]{2,}\b', 'ab-cd gh-c 12-423')
re.findall(r'\b[a-z\-0-9]{2,}\b', 'ab-cd gh-c 12-423')

# ^ should be other than first character or escaped using \.
re.findall(r'a[+^]b', 'f*(a^b) - 3*(a+b)')
re.findall(r'a[\^+]b', 'f*(a^b) - 3*(a+b)')

# [ can be escaped with \ or placed as last character. ] can be escaped with \ or placed as first character.
re.search(r'[]a-z0-9[]+', 'words[5] = tea')[0]
re.search(r'[a-z\[\]0-9]+', 'words[5] = tea')[0]

# \ should be escaped using \.
print(re.search(r'[a\\b]+', r'5ba\babc2')[0])

# \w is similar to [a-zA-Z0-9_] for matching word characters (recall the definition for word boundaries)
# \d is similar to [0-9] for matching digit characters
# \s is similar to [ \t\n\r\f\v] for matching whitespace characters

re.split(r'\d+', 'Sample123string42with777numbers')
re.findall(r'\d+', 'foo=5, bar=3; x=83, y=120')

''.join(re.findall(r'\b\w', 'sea eat car rat eel tea'))
re.findall(r'[\w\s]+', 'tea sea-pit sit-lean\tbean')

re.sub(r'\D+', '-', 'Sample123string42with777numbers')
re.sub(r'\W+', '', 'foo=5, bar=3; x=83, y=120')

s = '   1..3  \v\f  foo_baz 42\tzzz   \r\n1-2-3  '
re.findall(r'\S+', s)
re.findall(r'[\w.-]+', s)

# numeric ranges
# numbers between 10 to 29
re.findall(r'\b[12]\d\b', '23 154 12 26 98234')

# numbers >= 100
re.findall(r'\b[1-9]\d{2,}\b', '23 154 12 26 98234')
re.findall(r'\b\d{3,}\b', '23 154 12 26 98234')
# numbers >= 100 if there are leading zeros
re.findall(r'\b0*[1-9]\d{2,}\b', '0501 035 154 12 26 98234')

# numbers < 350
m_iter = re.finditer(r'\d+', '45 349 651 593 4 204')
[m[0] for m in m_iter if float(m[0]) < 350]


def num_range(s):
    return '1' if 200 <= int(s[0]) <= 650 else '0'

re.sub(r'\d+', num_range, '45 349 651 593 4 204')
re.sub(r'\d+', lambda m: '1' if 200 <= int(m[0]) <= 650 else '0', '45 349 651 593 4 204')

# a) For the list items, filter all elements starting with hand and ending with s or y or le.
items = ['-handy', 'hand', 'handy', 'unhand', 'hands', 'handle']
[i for i in items if re.search('\Ahand.*?(s|y|le)\Z', i)]
[i for i in items if re.fullmatch('hand.*?([sy]|le)', i)]

# b) Replace all whole words reed or read or red with X.
ip = 'redo red credible :read: rod reed'
re.sub(r'\bre[ea]?d\b', 'X', ip)

# c) For the list words, filter all elements containing e or i followed by l or n. Note that the order mentioned should be followed.
words = ['surrender', 'unicorn', 'newer', 'door', 'empty', 'eel', 'pest']
[w for w in words if re.search(r'[ei].*[ln]', w)]

# d) For the list words, filter all elements containing e or i and l or n in any order.
words = ['surrender', 'unicorn', 'newer', 'door', 'empty', 'eel', 'pest']
[w for w in words if re.search(r'[ei]', w) and re.search(r'[ln]', w)]
[w for w in words if re.search(r'([ei].*[ln]|[ln].*[ei])', w)]

# e) Extract all hex character sequences, with 0x optional prefix.
# Match the characters case insensitively,
# and the sequences shouldn't be surrounded by other word characters.
str1 = '128A foo 0xfe32 34 0xbar'
str2 = '0XDEADBEEF place 0x0ff1ce bad'
pat = re.compile(r'\b(0x)?[a-f\d]+\b', flags=re.I)
[s[0] for s in pat.finditer(str1)]

# f) Delete from ( to the next occurrence of ) unless they contain parentheses characters in between.
str1 = 'def factorial()'
str2 = 'a/b(division) + c%d(#modulo) - (e+(j/k-3)*4)'
str3 = 'Hi there(greeting). Nice day(a(b)'

pat = re.compile(r'\([^(]*?\)')
pat = re.compile(r'\([^()]*\)')
pat.sub('', str1)

# g) For the list words, filter all elements not starting with e or p or u.
words = ['surrender', 'unicorn', 'newer', 'door', 'empty', 'eel', 'pest']
[w for w in words if re.search(r'\A[^epu]', w)]

# h) For the list words, filter all elements not containing u or w or ee or -.
words = ['p-t', 'you', 'tea', 'heel', 'owe', 'new', 'reed', 'ear']
[w for w in words if not re.search(r'[uw\-]|ee', w)]
[w for w in words if not re.search(r'([uw\-]|ee)', w)]

# i) The given input strings contain fields separated by , and fields can be empty too. Replace last three fields with WHTSZ323.
row1 = '(2),kite,12,,D,C,,'
row2 = 'hi,bye,sun,moon'
pat = re.compile(r'([^,]*?,[^,]*?,[^,]*?)\Z')
pat.sub('WHTSZ323', row1)

pat = re.compile(r'(,[^,]*?){3}\Z')
pat.sub(',WHTSZ323', row1)

# j) Split the given strings based on consecutive sequence of digit or whitespace characters.
str1 = 'lion \t Ink32onion Nice'
str2 = '**1\f2\n3star\t7 77\r**'

pat = re.compile(r'[\s\d]+')
pat.split(str1)

# k) Delete all occurrences of the sequence <characters> where characters is one or more non > characters and cannot be empty.
ip = 'a<apple> 1<> b<bye> 2<> c<cat>'
re.sub(r'<[^>]+>', '', ip)

# m) For the given list, filter all elements containing any number sequence greater than 624.
items = ['hi0000432abcd', 'car00625', '42_624 0512', '3.14 96 2 foo1234baz']
# [i for i in items if re.search(r'') ]
pat = re.compile(r'\d+[.]?\d+')
for i in items:
    for m in pat.finditer(i):
        if float(m[0]) > 624:
            print(i)

# [i for i in items if float(m[0]) > 624 for m in pat.finditer(i)]
[i for i in items if any(float(m[0]) > 624 for m in pat.finditer(i))]

# n) Count the maximum depth of nested braces for the given strings.
# Unbalanced or wrongly ordered braces should return -1.
# Note that this will require a mix of regular expressions and Python code.


def max_nested_braces(ip):
    cnt = 0
    while True:
        ip, no_of_subs = re.subn(r'\{[^{}]*\}', ip)
        if no_of_subs == 0:
            break
        cnt += 1
    if re.search(r'[{}]', ip):
        return -1
    return cnt


max_nested_braces('a*b')
# 0
max_nested_braces('}a+b{')
# -1
max_nested_braces('a*b+{}')
# 1
max_nested_braces('{{a+2}*{b+c}+e}')
# 2
max_nested_braces('{{a+2}*{b+{c*d}}+e}')
# 3
max_nested_braces('{{a+2}*{\n{b+{c*d}}+e*d}}')
# 4
max_nested_braces('a*{b+c*{e*3.14}}}')
# -1

# o) By default, str.split method will split on whitespace and remove empty strings from the result.
# Which re module function would you use to replicate this functionality?
ip = ' \t\r  so  pole\t\t\t\n\nlit in to \r\n\v\f  '
re.split(r'\s+', ip)    # ['', 'so', 'pole', 'lit', 'in', 'to', '']
re.findall(r'\S+', ip)  # ['so', 'pole', 'lit', 'in', 'to']

# p) Convert the given input string to two different lists as shown below.
ip = 'price_42 roast^\t\n^-ice==cat\neast'
pat = re.compile(r'(\w+)[\^\s=-]*')
pat = re.compile(r'\b\w+\b')
pat.findall(ip)
# ['price_42', 'roast', 'ice', 'cat', 'east']
re.split(r'(\b\W+\b)', ip)
# ['price_42', ' ', 'roast', '^\t\n^-', 'ice', '==', 'cat', '\n', 'east']

# q) Filter all elements whose first non-whitespace character is not a # character.
# Any element made up of only whitespace characters should be ignored as well.
items = ['    #comment', '\t\napple #42', '#oops', 'sure', 'no#1', '\t\r\f']
[i for i in items if not re.search(r'^(\s*)#.*|^\s*$', i)]
[i for i in items if re.search(r'\A\s*[^#\s]', i)]


"""
    ----------------- 11 -----------------------
"""
# remove square brackets that surround digit characters
# note that use of raw strings for replacement string
re.sub(r'\[(\d+)\]', r'\1', '[52] apples and [31] mangoes')

# replace __ with _ and delete _ if it is alone
re.sub(r'(_)?_', r'\1', '_foo_ __123__ _baz_')

# swap words that are separated by a comma
re.sub(r'(\w+),(\w+)', r'\2,\1', 'good,bad 42,24')

# ambiguity between \N and digit characters part of replacement string
# re.error: invalid group reference 15 at position 2
re.sub(r'\[(\d+)\]', r'(\15)', '[52] apples and [31] mangoes')
# \g<N> solves this issue
re.sub(r'\[(\d+)\]', r'(\g<1>5)', '[52] apples and [31] mangoes')
# you can also use octal escapes
re.sub(r'\[(\d+)\]', r'(\1\065)', '[52] apples and [31] mangoes')

# add something around the matched strings using \g<0>
re.sub(r'[a-z]+', r'{\g<0>}', '[52] apples and [31] mangoes')
# note the use of '+' instead of '*' quantifier to avoid empty matching
re.sub(r'.+', r'Hi. \g<0>. Have a nice day', 'Hello world')
# duplicate first field and add it as last field
re.sub(r'\A([^,]+),.+', r'\g<0>,\1', 'fork,42,nice,3.14')

# whole words that have at least one consecutive repeated character
# \g<N> syntax is not available in RE definition,
# use formats like hexadecimal escapes to avoid ambiguity between normal digit characters and backreferences.
words = ['effort', 'flee', 'facade', 'oddball', 'rat', 'tool']
[w for w in words if re.search(r'(\w)\1', w)]
[w for w in words if re.search(r'\b\w*(\w)\1\w*\b', w)]

# non-capturing groups
# normal capture group will hinder ability to get whole match
# non-capturing group to the rescue
re.findall(r'\b\w*(?:st|in)\b', 'cost akin more east run against')
re.findall(r'\b\w*(st|in)\b', 'cost akin more east run against')

# capturing wasn't needed here, only common grouping and quantifier
re.split(r'hand(?:y|ful)?', '123hand42handy777handful500')
re.split(r'hand(y|ful)?', '123hand42handy777handful500')

# with normal grouping, need to keep track of all the groups
re.sub(r'\A(([^,]+,){3})([^,]+)', r'\1(\3)', '1,2,3,4,5,6,7')
# using non-capturing groups, only relevant groups have to be tracked
re.sub(r'\A((?:[^,]+,){3})([^,]+)', r'\1(\2)', '1,2,3,4,5,6,7')

re.search(r'\A(([^,]+,){3})', '1,2,3,4,5,6,7')

s = 'hi 123123123 bye 456123456'
re.findall(r'(123)+', s)
# text matched by a capture group with a quantifier will give only the last match, not entire match.
# Use a capture group around the grouping and quantifier together to get the entire matching portion.
re.findall(r'(?:123)+', s)

# note that this issue doesn't affect substitutions
re.sub(r'(123)+', 'X', s)

row = 'one,2,3.14,42,five'
# surround only fourth column with double quotes
# note the loss of columns in the first case
re.sub(r'(([^,]+,){3})([^,]+),', r'\1"\3",', row)
re.sub(r'(([^,]+,){3})([^,]+)', r'\1"\3"', row)
# re.sub(r'\A([^,]+,){3}([^,]+)', r'\1"\2"', row)
re.sub(r'\A(([^,]+,){3})([^,]+)', r'\1"\3"', row)

# However, there are situations where capture groups cannot be avoided. In such cases, you'd need to manually work with re.Match objects to get desired results.
# whole words containing at least one consecutive repeated character
words = 'effort flee facade oddball rat tool'
# re.findall(r'\b\w*(\w)\1\w*\b', words)
[m[0] for m in re.finditer(r'\b\w*(\w)\1\w*\b', words)]

# Named capture groups
re.sub(r'(?P<fw>\w+),(?P<sw>\w+)', r'\g<sw>,\g<fw>', 'good,bad 42,24')
s = 'aa a a a 42 f_1 f_1 f_13.14'
re.sub(r'\b(?P<dup>\w+)( (?P=dup))+\b', r'\g<dup>', s)

sentence = 'I bought an apple'
m = re.search(r'(?P<fruit>\w+)\Z', sentence)
m[1], m['fruit'], m.group('fruit')

details = '2018-10-25,car,2346'
re.search(r'(?P<date>[^,]+),(?P<product>[^,]+)', details).groupdict()
# normal groups won't be part of the output
re.search(r'(?P<date>[^,]+),([^,]+)', details).groupdict()

# multiple matches
s = 'good,bad 42,24'
[m.groupdict() for m in re.finditer(r'(?P<fw>\w+),(?P<sw>\w+)', s)]

# conditional groups
words = ['"hi"', 'bye', 'bad"', '"good"', '42', '"3']
pat = re.compile(r'(?P<quote>")?\w+(?(quote)")')
pat = re.compile(r'(")?\w+(?(1)")')
pat = re.compile(r'"\w+"|\w+')
[w for w in words if pat.fullmatch(w)]

# filter elements containing word characters surrounded by ()
# or, containing word characters separated by a hyphen
words = ['(hi)', 'good-bye', 'bad', '(42)', '-oh', 'i-j', '(-)']
# same as: r'\(\w+\)|\w+-\w+'
pat = re.compile(r'(\()?\w+(?(1)\)|-\w+)')
[w for w in words if pat.fullmatch(w)]
# ['(hi)', 'good-bye', '(42)', 'i-j']

re.sub(r'w(.*)m', r'[\1]', 'awesome')
re.search(r'w(.*)m', 'awesome').expand(r'[\1]')

dates = '2020/04/25,1986/03/02,77/12/31'
[m.expand(r'Month:\2, Year:\1') for m in re.finditer(r'(\d+?)/(\d+?)/(\d+?),?', dates)]
[m.expand(r'Month:\2, Year:\1') for m in re.finditer(r'([^/]+?)/([^/]+)/([^,]+),?', dates)]

# a) Replace the space character that occurs after a word ending with a or r with a newline character.
ip = 'area not a _a2_ roar took 22'
print(re.sub(r'\b(.*?[ar])\b', r'\1\n', ip))    # why not
print(re.sub(r'\b(\w*?[ar])\b', r'\1\n', ip))   # why not
print(re.sub(r'(\b\w*?[ar]\b)', r'\1\n', ip))   # why not
print(re.sub(r'([ar]) ', r'\1\n', ip))      # ??

# b) Add [] around words starting with s and containing e and t in any order.
ip = 'sequoia subtle exhibit asset sets tests site'
# re.sub(r'\b(s.*?(?:e.*?t|t.*?e).*?)\b', r'[\1]', ip)
# re.sub(r'(s.*?e.*?t|s.*?t.*?e)', r'[\1]', ip)
re.sub(r'\bs\w*(t\w*e|e\w*t)\w*', r'[\g<0>]', ip)