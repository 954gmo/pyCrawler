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