# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

# https://learnbyexample.github.io/py_regular_expressions/re-introduction.html#re-introduction

import re


# re.search(pattern, txt, flags=0)
# re.Match or None
# flags = re.I


words = ['cat', 'attempt', 'tattle']
l = [w for w in words if re.search(r'tt', w, flags=re.IGNORECASE)]
all(re.search(r'at', w) for w in words)
any(re.search(r'stat', w) for w in words)


# str.replace()
# re.sub(pattern, repl, string, count=0, flags=0)
greeting = "Have a nice weekend"
re.sub(r'e', 'E', greeting)
re.sub(r'e', 'E', greeting, count=2)
word = 'cater'
word = re.sub(r'cat', 'wa', word)


# compiling regular expressions
# if the RE has to be used in multiple places or called upon multiple times inside a loop
# re.compile(pattern, flags=0)
# re.Pattern

pet = re.compile(r'dog')
bool(pet.search('They bought a dog'))
pet.sub('cat', 'They bought a dog')

sentence = "This is a sample string"
word = re.compile(r'is')
bool(word.search(sentence, 4))
bool(word.search(sentence, 5))
bool(word.search(sentence, 2, 4))

byte_data = b'This is a sample string'
re.search(rb'is', byte_data)

# check whether the given strings contain 0xB0
line1 = 'start address: 0xA0, func1 address: 0xC0'
line2 = 'end address: 0xFF, func2 address: 0xB0'

re.search(r'0xB0', line1)
re.search(r'0xB0', line2)
# b) Replace all occurrences of 5 with five for the given string.
ip = 'They ate 5 apples and 5 oranges'
re.sub(r'5', 'five', ip)

# c) Replace first occurrence of 5 with five for the given string.
re.sub(r'5', 'five', ip, count=1)

# d) For the given list, filter all elements that do not contain e.
items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
[w for w in items if not re.search('e', w)]

# Replace all occurrences of note irrespective of case with
ip = 'This note should not be NoTeD'
re.sub('note', 'X', ip, flags=re.IGNORECASE)

# Check if at is present in the given byte input data.
ip = b'tiger imp goat'
bool(re.search(rb'at', ip))

# g) For the given input string, display all lines not containing start irrespective of case.

para = '''good start
 Start working on that
 project you always wanted
 stars are shining brightly
 hi there
 start and try to
 finish the book
 bye'''
pat = re.compile('start', flags=re.IGNORECASE)
for line in para.split('\n'):
    if not pat.search(line):
        print(line)

# h) For the given list, filter all elements that contains either a or w.
items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
[w for w in items if re.search('[aw]', w)]

# i) For the given list, filter all elements that contains both e and n.
items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
[w for w in items if re.search('e', w) and re.search('n', w)]


# others) For the given string, replace 0xA0 with 0x7F and 0xC0 with 0x1F.
ip = 'start address: 0xA0, func1 address: 0xC0'


# anchors
# \A restricts the matching to the start of string.
# \Z restricts the matching to the end of string
bool(re.search(r'\Acat', 'cater'))  # T
bool(re.search(r'\Acat', 'concatenation'))  # F
bool(re.search(r'\Ahi', 'hi hello\ntop spot'))  # T
bool(re.search(r'\Atop', 'hi hello\ntop spot')) # F
bool(re.search(r'are\z', 'spare'))  # T
bool(re.search(r'are\Z', 'nearest'))    # F

words = ['surrender', 'unicorn', 'newer', 'door', 'empty', 'eel', 'pest']
[w for w in words if re.search(r'er\Z', w)]
[w for w in words if re.search(r't\Z', w)]

# string concatenation
re.sub(r'\A', 're', 'live')
re.sub(r'\A', 're', 'send')

# string appending
re.sub(r'\Z', 'er', 'cat')
re.sub(r'\Z', 'er', 'hack')

word_pat = re.compile(r'\Aat')
bool(word_pat.search('cater', 1))   # F
bool(word_pat.search('cater'[1:]))  # T

# re.fullmatch
word_pat = re.compile(r'\Acat\Z')
bool(word_pat.search('cat'))  # T
bool(word_pat.search('concatenation')) # F

word_pat = re.compile(r'\Acat\Z', flags=re.I)
bool(word_pat.fullmatch('Cat'))  # T
bool(word_pat.fullmatch('Scatter'))  # F

# line anchors
pets = 'cat and dog'
bool(re.search(r'^cat', pets))  # T
bool(re.search(r'^dog', pets))  # F
bool(re.search(r'dog$', pets))  # T
bool(re.search(r'^dog$', pets))  # F

greeting = 'hi there\nhave a nice day\n'
bool(re.search(r'day$', greeting))   # T
bool(re.search(r'day\n$', greeting))    # T
bool(re.search(r'day\Z', greeting))     # F
bool(re.search(r'day\n\Z', greeting))   # T

bool(re.search(r'^top', 'hi hello\ntop spot', flags=re.MULTILINE))  # T
bool(re.search(r'ar$', 'spare\npar\ndare', flags=re.MULTILINE)) # T

elements = ['spare\ntool', 'par\n', 'dare']
[e for e in elements if re.search(r'are$', e, flags=re.MULTILINE)]

bool(re.search(r'^par$', 'spare\npar\ndare', flags=re.MULTILINE))   # T

ip_lines = 'catapults\nconcatenate\ncat'
print(re.sub('^', '* ', ip_lines, flags=re.MULTILINE))
print(re.sub('$', '.', ip_lines, flags=re.MULTILINE))

# word anchor
# \b

words = 'par spar apparent spare part'
re.sub(r'par', 'X', words)  # replace 'par' irrespective of where it occurs
re.sub(r'\bpar', 'X', words)    # replace 'par' only at start of word
re.sub(r'par\b', 'X', words)    # replace 'par' only at end of word
re.sub(r'\bpar\b', 'X', words)  # replace 'par' only if it is not part of another word

words = 'par spar apparent spare part'
print(re.sub(r'\b', '"', words).replace(' ', ','))
print(re.sub(r'\b', ' ', '---------hello----------'))
re.sub(r'\b', ' ', 'foo_baz=num1+35*42/num2').strip()

re.sub(r'\Bpar', 'X', words)    # replace 'par' if it is not start of word
re.sub(r'\Bpar\b', 'X', words)  # replace 'par' at the end of word but not whole word 'par'
re.sub(r'par\B', 'X', words)    # replace 'par' if it is not end of word
re.sub(r'\Bpar\B', 'X', words)  # replace 'par' if it is surrounded by word characters

re.sub(r'\b', ':', 'copper')
re.sub(r'\B', ':', 'copper')
re.sub(r'\b', ' ', '-----hello------')
re.sub(r'\B', ' ', '-----hello------')


# Check if the given strings start with be.
line1 = 'be nice'
line2 = '"best!"'
line3 = 'better?'
line4 = 'oh no\nbear spotted'

lines = [line1, line2, line3, line4]
for line in lines:
    print(bool(re.search(r'\Abe', line)))   # T F T F

# b) For the given input string, change only whole word red to brown
words = 'bred red spread credible'
re.sub(r'\bred\b', 'brown', words)

# c) For the given input list, filter all elements that contains 42 surrounded by word characters.
words = ['hi42bye', 'nice1423', 'bad42', 'cool_42a', 'fake4b']
[w for w in words if re.search(r'\B42\B', w)]

# d) For the given input list, filter all elements that start with den or end with ly.
items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\n', 'dent']
[w for w in items if (re.search(r'\Aden', w) or re.search(r'ly\Z', w))]

# e) For the given input string, change whole word mall to 1234 only if it is at the start of a line.

para = '''\
ball fall wall tall
mall call ball pall
wall mall ball fall
mallet wallet malls'''

print(re.sub(r'^\bmall\b', '1234', para, flags=re.M))

# f) For the given list, filter all elements having a line starting with den or ending with ly.
items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\nfar', 'dent']
[w for w in items if (re.search(r'^den', w, flags=re.M) or re.search(r'ly$', w, flags=re.M))]

# g) For the given input list, filter all whole elements 12\nthree irrespective of case.
items = ['12\nthree\n', '12\nThree', '12\nthree\n4', '12\nthree']
[w for w in items if re.search(r'\A12\nthree\Z', w, flags=re.I)]

# h) For the given input list, replace hand with X for all elements that start with hand followed by at least one word character.
items = ['handed', 'hand', 'handy', 'unhanded', 'handle', 'hand-2']
[re.sub(r'^hand\B', 'X', w) for w in items]

# i) For the given input list, filter all elements starting with h. Additionally, replace e with X for these filtered elements.
items = ['handed', 'hand', 'handy', 'unhanded', 'handle', 'hand-2']
[re.sub(r'e', 'X', w) for w in items if re.search(r'^h', w)]

# alternation and grouping
# match either 'cat' or 'dog'
bool(re.search(r'cat|dog', 'I like cats'))   # T
bool(re.search(r'cat|dog', 'I like dogs'))  # T
bool(re.search(r'cat|dog', 'I like parrots'))   # F

# replace either 'cat' at start of string or 'cat' at end of word
re.sub('\Acat|cat\b', 'X', 'catapults concatenate cat scat')
# replace either 'cat' or 'dog' or 'fox' with 'mammal'
re.sub(r'cat|dog|fox', 'mamal', 'cat dog bee parrot fox')

'|'.join(['car', 'jeep'])
words = ['cat', 'dog', 'fox']
re.sub('|'.join(words), 'mamal', 'cat dog bee parrot fox' )

re.sub(r'reform|rest', 'X', 'red reform read arrest')
re.sub(r're(form|st)', 'X', 'red reform read arrest')
re.sub(r'\bpar\b|\bpart\b', 'X', 'par spare part party')
re.sub(r'\b(par|part)\b', 'X', 'par spare part party')
re.sub(r'\bpar(|t)\b', 'X', 'par spare part party')


words = ['cat', 'par']
'|'.join(words)
re.sub("|".join(words), 'X', 'cater cat concatenate par spare')
alt = re.compile(r'\b(' + '|'.join(words) + r')\b')
alt.sub('X', 'cater cat concatenate par spare')
alt.pattern

terms = ['no', 'ten', 'it']
items = ['dip', 'nobody', 'it', 'oh', 'no', 'bitten']
alt = re.compile('|'.join(terms))
[w for w in items if alt.fullmatch(w)]
[w for w in items if alt.search(w)]

# precedence rule
words = 'lion elephant are rope not'
re.search(r'on', words)
re.search(r'ant', words)
re.sub(r'ant|on', 'X', words)

words = 'ear xerox at mare part learn eye'
re.sub(r'ar|are|art', 'X', words)   # same as r'ar'
re.sub(r'are|ar|art', 'X', words)   # same as r'are|ar'
re.sub(r'are|art|ar', 'X', words)   #

words = ['hand', 'handy', 'handful']
alt = re.compile('|'.join(sorted(words, key=len, reverse=True)))
alt.sub('X', 'hands handful, handed, handy')

# a) For the given input list, filter all elements that start with den or end with ly
items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\n', 'dent']
[w for w in items if re.search(r'\Aden|ly\Z', w)]

# For the given list, filter all elements having a line starting with den or ending with ly.
items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\nfar', 'dent']
[w for w in items if re.search(r'^den|ly$', w, flags=re.M)]

# c) For the given input strings, replace all occurrences of removed or reed or received or refused with X.
s1 = 'creed refuse removed read'
s2 = 'refused reed redo received'

pat = re.compile('re(ceived|moved|fused|ed)')
print(pat.sub(s1))
print(pat.sub(s2))

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
[w for w in items if pat.fullmatch(w)]
pat = re.compile(r'\b(' + '|'.join(sorted(words, key=len, reverse=True)) + r')\b')
[w for w in items if pat.search(w)]

txt = 'a^2 + b^2 - c*3'
bool(re.search(r'b^2', txt))    # F
bool(re.search(r'b\^2', txt))   # T

# re.escape
expr = '(a^b)'
print(re.escape(expr))

eqn = 'f*(a^b) - 3*(a^b)'
re.sub(re.escape(expr) + r'\Z', 'c', eqn)

terms = ['a_42', '(a^b)', '2|3']
pat1 = re.compile('|'.join(sorted([re.escape(s) for s in terms], key=len, reverse=True)))
pat2 = re.compile('|'.join(sorted(terms, key=len, reverse=True)))

# a) Transform the given input strings to the expected output using same logic on both strings.
str1 = '(9-2)*5+qty/3'
str2 = '(qty+4)/2-(9-2)*5+pq/4'

pat = re.compile(re.escape(r'(9-2)*5'))
print(pat.sub('35', str1))
print(pat.sub('35', str2))

# b) Replace (4)\| with 2 only at the start or end of given input strings.
s1 = r'2.3/(4)\|6 foo 5.3-(4)\|'
s2 = r'(4)\|42 - (4)\|3'
s3 = 'two - (4)\\|\n'
expr = re.escape(r'(4)\|')
pat = re.compile(r'\A' + expr + r"|" + expr + '\Z' )
pat.sub('2', s1)
pat.sub('2', s2)
pat.sub('2', s3)

# c) Replace any matching element from the list items with X for given the input strings.
# Match the elements from items literally.
# Assume no two elements of items will result in any matching conflict.
items = ['a.b', '3+n', r'x\y\z', 'qty||price', '{n}']
pat = re.compile('|'.join(sorted([re.escape(w) for w in items], key=len, reverse=True)))
pat.sub('X', '0a.bcd')
pat.sub('X', 'E{n}AMPLE')
pat.sub('X', r'43+n2 ax\y\ze')

# d) Replace backspace character \b with a single space character for the given input string.
ip = '123\b456'
expr = re.escape('\b')
pat = re.compile(expr)
pat.sub(' ', ip)

# e) Replace all occurrences of \e with e.
ip = r'th\er\e ar\e common asp\ects among th\e alt\ernations'
pat = re.compile(re.escape('\e'))
pat.sub('e', ip)

# f) Replace any matching item from the list eqns with X for given the string ip. Match the items from eqns literally.
ip = '3-(a^b)+2*(a^b)-(a/b)+3'
eqns = ['(a^b)', '(a/b)', '(a^b)+2']

pat = re.compile('|'.join(sorted([re.escape(e) for e in eqns], key=len, reverse=True)))
pat.sub('X', ip)

re.sub(r'c.t', 'X', 'tac tin cat abc;tuv acute')
re.sub(r'c..d', 'X', 'breadth markedly reported overrides')
re.sub(r'2.3', '8', '42\t35')
bool(re.search(r'a.b', 'a\nb'))     # F

# re.split(pattern, string, maxsplit=0, flags=0)
# same as: 'apple-85-mango-70'.split('-')
re.split(r'-', 'apple-85-mango-70')
# maxsplit determines the maximum number of times to split the input
re.split(r'-', 'apple-85-mango-70', maxsplit=1)
# example with dot metacharacter
re.split(r':.:', 'bus:3:car:5:van')

# same as: r'ear|ar'
re.sub(r'e?ar', 'X', 'far feat flare fear' )
# same as: r'\bpar(t|)\b'
re.sub('\bpart?\b', 'X', 'par spare part party')
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
re.sub(r't[ea]*r', 'X', 'tr tear tare steer sitaara')
re.sub(r't(e|a)*r', 'X', 'tr tear tare steer sitaara')
# match zero or more of '1' followed by '2'
re.sub(r'1*2', 'X', '3111111111125111142' )
# last element is empty because there is nothing after 2 at the end of string
re.split(r'1*2','3111111111125111142', maxsplit=1)
# later, you'll see how maxsplit helps to get behavior like str.partition
re.split(r'1*2', '3111111111125111142')
# empty string matches at start and end of string
# it matches between every character
# and, there is an empty match after the split at u
re.split(r'u*', 'cloudy')

re.sub(r'ta+r', 'X', 'tr tear tare steer sitaara')
re.sub(r't(e|a)+r', 'X', 'tr tear tare steer sitaara')
re.split(r'1+', '3111111111125111142')
re.split(r'u+', 'cloudy')

demo = ['abc', 'ac', 'adc', 'abbc', 'xabbbcz', 'bbb', 'bc', 'abbbbbc']
[w for w in demo if re.search(r'ab{1,4}c', w)]
[w for w in demo if re.search(r'ab{3,}c', w)]
[w for w in demo if re.search(r'ab{,2}c', w)]
[w for w in demo if re.search(r'ab{3}c', w)]

# construct conditional AND using dot metacharacter and quantifiers.
bool(re.search(r'Error.*valid', 'Error: not a valid input'))    # T
bool(re.search(r'Error.*valid', 'Error: key not found'))    # F

seq1 = 'cat and dog'
seq2 = 'dog and cat'
bool(re.search(r'cat.*dog|dog.*cat', seq1))  # T
bool(re.search(r'cat.*dog|dog.*cat', seq2))  # T

patterns = (r'cat', r'dog')
all(re.search(p, seq1) for p in patterns)
all(re.search(p, seq2) for p in patterns)
re.sub(r'f.?o', 'X', 'foot')

# a more practical example
# prefix '<' with '\' if it is not already prefixed
# both '<' and '\<' will get replaced with '\<'
# note the use of raw string for all the three arguments
re.sub(r'\\?<', r'\<', r'blah \< foo < bar \< blah < baz')
# say goodbye to r'handful|handy|hand' shenanigans
re.sub(r'hand(ful|y)?', 'X', 'hand handy handful')
# backtracking
sentence = 'that is quite a fabricated tale'
# r't.*a' will always match from first 't' to last 'a'
# also, note that count argument is set to 1 for illustration purposes
re.sub(r't.*a', 'X', sentence, count=1)
re.sub(r't.*a', 'X', 'star', count=1)
# matching first 't' to last 'a' for t.*a won't work for these cases
# the engine backtracks until .*q matches and so on
re.sub(r't.*a.*q.*f', 'X', sentence)
re.sub(r't.*a.*q.*u', 'X', sentence)

# non-greedy quantifiers
re.sub(r'f.??o', 'X', 'foot')
re.sub(r'f.??o', 'X', 'frost')
re.sub(r'.{2,5}?', 'X', '123456789')
re.split(r':.*?:', 'green:3.14:teal::brown:oh!:blue')

sentence = 'that is quite a fabricated tale'
# r't.*?a' will always match from first 't' to first 'a'
re.sub(r't.*?a', 'X', sentence, count=1)
re.sub(r't.*?a', 'X', sentence, count=2)
re.sub(r't.*?a', 'X', sentence)

re.sub(r't.*?a.*?f', 'X', sentence, count=1)


# a) Replace 42//5 or 42/5 with 8 for the given input.
ip = 'a+42//5-c pressure*3+42/5-14256'

re.sub(r'42/{1,2}5', '8', ip)
re.sub(r'42//?5', '8', ip)

# b) For the list items, filter all elements starting with hand and ending with at most one more character or le.
items = ['handed', 'hand', 'handled', 'handy', 'unhand', 'hands', 'handle']
[w for w in items if re.search(r'\Ahand(.{,1}|le)\Z', w)]
[w for w in items if re.search(r'\Ahand(.?|le)\Z', w)]
[w for w in items if re.search(r'hand(.|le)?', w)]

# c) Use re.split to get the output as shown for the given input strings.
eqn1 = 'a+42//5-c'
eqn2 = 'pressure*3+42/5-14256'
eqn3 = 'r*42-5/3+42///5-42/53+a'

re.split(r'42//?5', eqn1)
re.split(r'42/{1,2}5', eqn2)
re.split(r'42//?5', eqn3)

# d) For the given input strings, remove everything from the first occurrence of i till end of the string.
s1 = 'remove the special meaning of such constructs'
s2 = 'characters while constructing'
re.sub(r'i.*', '', s1)
re.sub(r'i.*', '', s2)

# e) For the given strings, construct a RE to get output as shown.
str1 = 'a+b(addition)'
str2 = 'a/b(division) + c%d(#modulo)'
str3 = 'Hi there(greeting). Nice day(a(b)'

pat = re.compile(r'\(.*?\)')
pat.sub('', str1)

# f) Correct the given RE to get the expected output.
words = 'plink incoming tint winter in caution sentient'
change = re.compile(r'int|in|ion|ing|inco|inter|ink')
# correct
change = re.compile(r'inter|inco|int|ing|ink|ion|in')
change = re.compile(r'in(ter|co|t|g|k)?|ion')
change.sub('X', words)

# g) For the given greedy quantifiers, what would be the equivalent form using {m,n} representation?
# ? ==> {,1}
# * ==> {0,}
# + ==> {1,}

# h) (a*|b*) is same as (a|b)* — True or False? F

# i) For the given input strings,
# remove everything from the first occurrence of test (irrespective of case) till end of the string, provided test isn't at the end of the string.
s1 = 'this is a Test'
s2 = 'always test your RE for corner cases'
s3 = 'a TEST of skill tests?'
pat = re.compile('test.+\Z', flags=re.I)
pat = re.compile('test.+', flags=re.I)
pat.sub('', s1)

# others) For the input list words, filter all elements starting with s and containing e and t in any order.
words = ['sequoia', 'subtle', 'exhibit', 'asset', 'sets', 'tests', 'site']
[w for w in words if re.search(r'\As.*(e.*t|t.*e)+.*', w)]
[w for w in words if re.search(r'\As.*(e.*t|t.*e)+.*', w)]
[w for w in words if re.search(r'\As.*(e.*t|t.*e)', w)]

# k) For the input list words, remove all elements having less than 6 characters.
words = ['sequoia', 'subtle', 'exhibit', 'asset', 'sets', 'tests', 'site']
[w for w in words if re.search(r'.{6,}', w)]

# l) For the input list words, filter all elements starting with s or t and having a maximum of 6 characters.
words = ['sequoia', 'subtle', 'exhibit', 'asset', 'sets', 'tests', 'site']
[w for w in words if re.search(r'\A[st].{,5}\Z', w)]
[w for w in words if re.search(r'\A(s|t).{,5}\Z', w)]
[w for w in words if re.fullmatch(r'(s|t).{,5}', w)]

# m) Can you reason out why this code results in the output shown?
# The aim was to remove all <characters> patterns but not the <> ones.
# The expected result was 'a 1<> b 2<> c'.
ip = 'a<apple> 1<> b<bye> 2<> c<cat>'
re.sub(r'<.+?>', '', ip)

# n) Use re.split to get the output as shown below for given input strings.
s1 = 'go there  //   "this // that"'
s2 = 'a//b // c//d e//f // 4//5'
s3 = '42// hi//bye//see // carefully'

re.split(r' +// +', s2, maxsplit=1)
pat = re.compile(r' +// +')
pat.split(s1, maxsplit=1)
pat.split(s1, maxsplit=2)

# re.Match object
# re.search and re.fullmatch
# matched portion of string, location of matched portion
# only for the first match
# re.Match.span() # the starting and ending+1 indexes of the matching portion
sentence = 'that is quite a fabricated tale'
m = re.search(r'q.*?t', sentence)
m.span()

# capture group
re.search(r'b.*d', 'abc ac adc abbbc')
# retrieving entire matched portion using index
re.search(r'b.*d', 'abc ac adc abbbc')[0]
# retrieving entire matched portion using 'group' method
# you can also skip passing '0' as that is the default value
re.search(r'b.*d', 'abc ac adc abbbc').group()
re.search(r'b.*d', 'abc ac adc abbbc').group(0)

m = re.fullmatch(r'a(.*?) (.*)d(.*)c', 'abc ac adc abbbc')
m[2] # 'ac a'
m.group(3, 1, 2, 2)
m.groups()

m = re.search(r'w(.*)me', 'awesome')
m.span()
m.span(1)
m.start(1)
m.end(2)

if m := re.search(r'(.*)s', 'oh!'):
    print(m[1])

text = ['type: fruit', 'date: 2020/04/28']
for ip in text:
    if m := re.search(r'type: (.*)', ip):
        print(m[1])
    elif m := re.search(r'date (.*?)/(.*?)/', ip):
        print(f"month {m[2]}, year: {m[1]}")

re.sub(r'(a|b)\^2', lambda m: m[0].upper(), 'a^2 + b^2 - C*3')
re.sub(r'2|3', lambda m: str(int(m[0])**2), 'a^2 + b^2 - C*3')

d = {'1': 'one', '2': 'two', '4': 'four'}
re.sub(r'1|2|4', lambda m:d[m[0]], '9234012')
re.sub(r'[0-9]', lambda m:d.get(m[0], 'X'), '9234012')
re.sub(r"0|1|2|3|4|5|6|7|8|9", lambda m:d.get(m[0], 'X'), '9234012')

# For swapping two or more portions without using intermediate result, using a dict object is recommended.
swap = {'cat': 'tiger', 'tiger': 'cat'}
words = 'cat tiger dog tiger cat'
re.sub(r'cat|tiger', lambda m: swap[m[0]], words)

d = {'hand': '1', 'handy': '2', 'handful': '3', 'a^b': '4'}
words = sorted(d.keys(), key=len, reverse=True)
pat = re.compile('|'.join(re.escape(s) for s in words))
pat.sub(lambda m: d[m[0]], 'handful hand pin handy (a^b)')

# re.findall(pattern, string, flags=0)
re.findall(r'ab*c', 'abc ac adc abbbc')
re.findall(r'ab+c', 'abc ac adc abbbc')
s = 'PAR spar apparent SpArE part pare'
re.findall(r'\bs?pare?\b', s, flags=re.I)

re.findall(r'ab*c', 'abc ac adc abbc xabbbcz bbb bc abbbbbc')
re.findall(r'a(b*)c', 'abc ac adc abbc xabbbcz bbb bc abbbbbc')
re.findall(r'(.*?)/(.*?)/(.*?),', '2020/04/25,1986/Mar/02,77/12/31')

m_iter = re.finditer(r'ab+c', 'abc ac adc abbbc')
for m in m_iter:
    print(m[0].upper(), m.span(), sep='\t')

# same as: re.findall(r'(.*?)/(.*?)/(.*?),', d)
d = '2020/04/25,1986/Mar/02,77/12/31'
m_iter = re.finditer(r'(.*?)/(.*?)/(.*?),', d)
[m.groups() for m in m_iter]

re.split(r'1*4?2', '31111111111251111426')
# to include the matching portions of the pattern as well in the output
re.split(r'(1*4?2)', '31111111111251111426')
# here 4?2 is outside capture group, so that portion won't be in output
re.split(r'(1*)4?2', '31111111111251111426')
# multiple capture groups example
# note that the portion matched by b+ isn't present in the output
re.split(r'(a+)b+(c+)', '3.14aabccc42')

re.subn(r'e', 'E', greeting)

word = 'coffining'
while True:
    word, cnt = re.subn(r'fin', '', word)
    if cnt == 0:
        break

# a) For the given strings, extract the matching portion from first is to last t.
str1 = 'This the biggest fruit you have seen?'
str2 = 'Your mission is to read and practice consistently'
pat = re.compile(r'is.*t')
pat.findall(str1)
pat.findall(str2)
pat.search(str1)[0]
pat.search(str2)[0]

# b) Find the starting index of first occurrence of is or the or was or to for the given input strings.
s1 = 'match after the last newline character'
s2 = 'and then you want to test'
s3 = 'this is good bye then'
s4 = 'who was there to see?'

pat = re.compile(r'is|the|was|to')
pat.search(s1).start()

# c) Find the starting index of last occurrence of is or the or was or to for the given input strings.
s1 = 'match after the last newline character'
s2 = 'and then you want to test'
s3 = 'this is good bye then'
s4 = 'who was there to see?'

pat = re.compile(r'.*(is|the|was|to)')
pat.search(s1).start(1)

# d) The given input string contains : exactly once. Extract all characters after the : as output.
ip = 'fruits:apple, mango, guava, blueberry'
pat = re.compile(r':(.*)')
pat.search(ip).group(1)
pat.search(ip)[1]

import math
# e) The given input strings contains some text followed by - followed by a number. Replace that number with its log value using math.log().
s1 = 'first-3.14'
s2 = 'next-123'
pat = re.compile('-(.*)')
pat.sub(lambda m: '-' + str(math.log(float(m[1]))), s1)

# f) Replace all occurrences of par with spar, spare with extra and park with garden for the given input strings.
str1 = 'apartment has a park'
str2 = 'do you have a spare cable'
str3 = 'write a parser'

d = {'par': 'spar', 'spare': 'extra', 'park': 'garden'}
# pat = re.compile(r'(par|spare|park)')
pat = re.compile(r'spare|park?')
pat.sub(lambda m: d[m[0]], str1)

# g) Extract all words between ( and ) from the given input string as a list. Assume that the input will not contain any broken parentheses.\
ip = 'another (way) to reuse (portion) matched (by) capture groups'
pat = re.compile(r'\((.*?)\)')
pat.findall(ip)

# h) Extract all occurrences of < up to next occurrence of >, provided there is at least one character in between < and >.
ip = 'a<apple> 1<> b<bye> 2<> c<cat>'
re.findall(r'(<.+?>)', ip)

# i) Use re.findall to get the output as shown below for the given input strings. Note the characters used in the input strings carefully.
row1 = '-2,5 4,+3 +42,-53 4356246,-357532354 '
row2 = '1.32,-3.14 634,5.63 63.3e3,9907809345343.235 '

pat = re.compile(r'(-?\d+,-?\d+) ')
pat = re.compile(r'(.*?),(.*?) ')
pat.findall(row1)

# others) This is an extension to previous question.
#
# For row1, find the sum of integers of each tuple element. For example, sum of -2 and 5 is 3.
# For row2, find the sum of floating-point numbers of each tuple element. For example, sum of 1.32 and -3.14 is -1.82.

row1 = '-2,5 4,+3 +42,-53 4356246,-357532354 '
row2 = '1.32,-3.14 634,5.63 63.3e3,9907809345343.235 '

pat = re.compile(r'(.*?),(.*?) ')
[float(res[0]) - float(res[1]) for res in pat.findall(row1)]

# k) Use re.split to get the output as shown below.
ip = '42:no-output;1000:car-truck;SQEX49801'
# re.split(r'(:.*?-?)', ip)
re.split(r':.+?-(.+?);', ip)

# l) For the given list of strings, change the elements into a tuple of original element and number of times t occurs in that element.
words = ['sequoia', 'attest', 'tattletale', 'asset']
[(w, len(re.findall(r't', w))) for w in words]

# m) The given input string has fields separated by :.
# Each field contains four uppercase alphabets followed optionally by two digits.
# Ignore the last field, which is empty.
# See docs.python: Match.groups and use re.finditer to get the output as shown below.
# If the optional digits aren't present, show 'NA' instead of None.
ip = 'TWXA42:JWPA:NTED01:'
[(res[1], res[2] if res[2] else 'NA') for res in re.finditer(r'(.*?)(\d*):', ip)]

# n) Convert the comma separated strings to corresponding dict objects as shown below.
row1 = 'name:rohan,maths:75,phy:89,'
row2 = 'name:rose,maths:88,phy:92,'
pat = re.compile(r'(.*?):(.*?),')
{res[1]: res[2] for res in pat.finditer(row1)}

words = ['cute', 'cat', 'cot', 'coat', 'cost', 'scuttle']
# same as: r'cot|cut' or r'c(o|u)t'
[w for w in words if re.search(r'c[ou]t', w)]
# same as: r'(a|e|o)+t'
[w for w in words if re.search(r'[aeo]+t', w)]
re.sub(r'[aeo]+t', 'X',  'meeting cute boat site foot')

re.findall(r'\d+', 'Sample123string42with777numbers')
re.findall(r'[0-9]+', 'Sample123string42with777numbers')

# whole words made up of lowercase alphabets and digits only
re.findall(r'\b[a-z0-9]+\b', 'coat Bin food tar12 best')

# whole words made up of lowercase alphabets, but starting with 'p' to 'z'
re.findall(r'\b[p-z][a-z]*\b', 'coat tin food put stoop best')

# whole words made up of only 'a' to 'f' and 'p' to 't' lowercase alphabets
re.findall(r'\b[a-fp-t]+\b', 'coat tin food put stoop best')

# all non-digits
re.findall(r'\D+', 'Sample123string42with777numbers')
re.findall(r'[^0-9]+', 'Sample123string42with777numbers')

# remove first two columns where : is delimiter
re.sub(r'[a-z0-9]+:', '', 'foo:123:bar:baz', count=2)
re.sub(r'^[a-z0-9]+:[a-z0-9]+:', '', 'foo:123:bar:baz', count=1)
re.sub(r'\A([^:]+:){2}', '', 'foo:123:bar:baz', count=1)

# deleting characters at end of string based on a delimiter
re.sub(r'=[^=]+\Z', '', 'foo=42; baz=123')

dates = '2020/04/25,1986/Mar/02,77/12/31'
# Note that the third character set negates comma as well
# and comma is matched optionally outside the capture groups
re.findall(r'(\d+)/(\w+)/(\d+)', dates)
re.findall(r'([^/]+)/([^/]+)/([^/,]+),?', dates)

words = ['tryst', 'fun', 'glyph', 'pity', 'why']
# words not containing vowel characters
[ w for w in words if re.search(r'\A[^aeiou]+\Z', w)]
[w for w in words if not re.search(r'[aeiou]', w)]

re.findall(r'\b[a-z-]{2,}\b', 'ab-cd gh-c 12-423')
re.findall(r'\b[a-z\-0-9]\b', 'ab-cd gh-c 12-423')

re.findall(r'a[\^+]b', 'f*(a^b) - 3*(a+b)')

re.search(r'\A\w+\[\d]', 'words[5] = tea')[0]
re.search(r'[]a-z0-9[]+', 'words[5] = tea')[0]

# numeric ranges
# numbers between 10 to 29
re.compile(r'\b[12]\d\b')

# numbers > 100
re.compile(r'\b[2-9]\d{2,}\b')
# numbers >= 100
re.compile(r'\b\d{3,}\b')
# numbers >= 100 if there are leading zeros
re.compile(r'\b0*[1-9]\d{2,}\b')
# If numeric range is difficult to construct, better to convert the matched portion to appropriate numeric format first.
pat = re.compile(r'\d+')
m_iter = pat.finditer('45 349 651 593 4 204')
[m[0] for m in m_iter if int(m[0]) < 350]

# a) For the list items, filter all elements starting with hand and ending with s or y or le.
items = ['-handy', 'hand', 'handy', 'unhand', 'hands', 'handle']
[ w for w in items if re.search(r'\Ahand.*[sy(le)]\Z', w)]
[w for w in items if re.search(r'^hand.*[sy(le)]$', w)]
[w for w in items if re.fullmatch(r'hand([sy]|le)', w)]
[w for w in items if re.search(r'\Ahand([sy]|le)\Z', w)]

# b) Replace all whole words reed or read or red with X.
ip = 'redo red credible :read: rod reed'
re.sub(r'\bre[ea]*d\b', 'X', ip)
re.sub(r'\bre[ea]?d\b', 'X', ip)
re.sub(r'\b(red|read|reed)\b', 'X', ip)

# c) For the list words, filter all elements containing e or i followed by l or n. Note that the order mentioned should be followed.
words = ['surrender', 'unicorn', 'newer', 'door', 'empty', 'eel', 'pest']
[w for w in words if re.search(r'[ei].*[ln]', w)]

# d) For the list words, filter all elements containing e or i and l or n in any order.
words = ['surrender', 'unicorn', 'newer', 'door', 'empty', 'eel', 'pest']
[w for w in words if re.search(r'[ei].*[ln].*|[ln].*[ei].*', w)]

# e) Extract all hex character sequences, with 0x optional prefix.
# Match the characters case insensitively, and the sequences shouldn't be surrounded by other word characters.
str1 = '128A foo 0xfe32 34 0xbar'
str2 = '0XDEADBEEF place 0x0ff1ce bad'
# hex_seq = re.compile(r'\b(0x[A-F]*\d*|0x\d*[A-F]*|[A-F]*\d*|\d*[A-F]*)\b', flags=re.I)
# hex_seq = re.compile(r'\b(0x)?([A-F]*\d*|\d*[A-F]*)\b', flags=re.I)
hex_seq = re.compile(r'\b(0x)?[\da-f]+\b', flags=re.I)
[m[0] for m in hex_seq.finditer(str1)]

# f) Delete from ( to the next occurrence of ) unless they contain parentheses characters in between.
str1 = 'def factorial()'
str2 = 'a/b(division) + c%d(#modulo) - (e+(others/k-3)*4)'
str3 = 'Hi there(greeting). Nice day(a(b)'

pat = re.compile(r'\([^\(\)]*?\)')
pat = re.compile(r'\([^()]*\)')
pat.sub('', str1)

# g) For the list words, filter all elements not starting with e or p or u.
words = ['surrender', 'unicorn', 'newer', 'door', 'empty', 'eel', 'pest']
[w for w in words if re.fullmatch(r'[^epu].*', w)]
[w for w in words if re.search(r'\A[^epu].*\Z', w)]
[w for w in words if re.search(r'\A[^epu]', w)]

# h) For the list words, filter all elements not containing u or w or ee or -.
words = ['p-t', 'you', 'tea', 'heel', 'owe', 'new', 'reed', 'ear']
[w for w in words if not re.search(r'([uw-]|ee)', w)]
[w for w in words if not re.search(r'[wu-]|ee', w)]

# i) The given input strings contain fields separated by , and fields can be empty too. Replace last three fields with WHTSZ323.
row1 = '(2),kite,12,,D,C,,'
row2 = 'hi,bye,sun,moon'
# pat = re.compile(r'(.*?),')
# pat.sub(lambda m:m[0][::-1] + ',', row1, count=3)
pat = re.compile(r'(,[^,]*){3}\Z')
pat.sub('WHTSZ323', row1)

# others) Split the given strings based on consecutive sequence of digit or whitespace characters.
str1 = 'lion \t Ink32onion Nice'
str2 = '**1\f2\n3star\t7 77\r**'
pat = re.compile(r'[\s\d]+')
pat.split(str1)

# k) Delete all occurrences of the sequence <characters> where characters is one or more non > characters and cannot be empty.
ip = 'a<apple> 1<> b<bye> 2<> c<cat>'
re.sub(r'<[^>]+>', '', ip)

# l) \b[a-z](on|no)[a-z]\b is same as \b[a-z][on]{2}[a-z]\b. True or False? Sample input lines shown below might help to understand the differences, if any.
# False
print('known\nmood\nknow\npony\ninns')

# m) For the given list, filter all elements containing any number sequence greater than 624.
items = ['hi0000432abcd', 'car00625', '42_624 0512', '3.14 96 2 foo1234baz']
pat = re.compile(r'0*(\d+[\.]?\d+)')
# [m[0] for m in [m_iter for m_iter in [pat.finditer(w) for w in items]]]
for w in items:
    for m in pat.finditer(w):
        if float(m[1]) > 624:
            print(m[1])

# [m[1] for m in [pat.finditer(w) for w in items]]

# n) Count the maximum depth of nested braces for the given strings.
# Unbalanced or wrongly ordered braces should return -1.
# Note that this will require a mix of regular expressions and Python code.


# o) By default, str.split method will split on whitespace and remove empty strings from the result.
# Which re module function would you use to replicate this functionality?
ip = ' \t\r  so  pole\t\t\t\n\nlit in to \r\n\v\f  '
# re.split(r'\s+', ip)
re.findall(r'\S+', ip)

# p) Convert the given input string to two different lists as shown below.
ip = 'price_42 roast^\t\n^-ice==cat\neast'
re.findall(r'\w+|\W+', ip)

# q) Filter all elements whose first non-whitespace character is not a # character.
# Any element made up of only whitespace characters should be ignored as well.
items = ['    #comment', '\t\napple #42', '#oops', 'sure', 'no#1', '\t\r\f']
# [w for w in items if re.search(r'\s*(^#).*', w)]
[w for w in items if re.search(r'\A\s*[^#\s]', w)]

# remove square brackets that surround digit characters
# note that use of raw strings for replacement string
re.sub(r'\[(\d+)\]', r'\1', '[52] apples and [31] mangoes')

# replace __ with _ and delete _ if it is alone
re.sub(r'(_)?_', r'\1', '_foo_ __123__ _baz_')

# swap words that are separated by a comma
re.sub(r'(\w+),(\w+)', r'\2,\1', 'good,bad 42,24')

# ambiguity between \N and digit characters part of replacement string
# re.sub(r'\[(\d+)\]', r'(\15)', '[52] apples and [31] mangoes')
re.sub(r'\[(\d+)\]', r'(\g<1>5)', '[52] apples and [31] mangoes')
# \0 and \NNN will be interpreted as octal value
re.sub(r'\[(\d+)\]', r'(\1\065)', '[52] apples and [31] mangoes')
# add something around the matched strings using \g<0>
re.sub(r'[a-z]+', r'{\g<0>}', '[52] apples and [31] mangoes')
re.sub(r'.+', r'Hi. \g<0>. Have a nice day', 'Hello world')
# duplicate first field and add it as last field
re.sub(r'(\A[^,]+),(.*)', r'\1,\2,\1', 'fork,42,nice,3.14')
re.sub(r'\A([^,]+).+', r'\g<0>,\1','fork,42,nice,3.14')

# whole words that have at least one consecutive repeated character
words = ['effort', 'flee', 'facade', 'oddball', 'rat', 'tool']
[w for w in words if re.search(r'\b\w*(\w)\1\w*\b', w)]

# remove any number of consecutive duplicate words separated by space
# note the use of quantifier on backreferences
# use \W+ instead of space to cover cases like 'a;a<-;a'
# re.sub(r' (\w+) \1', r'', 'aa a a a 42 f_1 f_1 f_13.14')
re.sub(r'\b(\w+)( \1)+\b', r'\1', 'aa a a a 42 f_1 f_1 f_13.14')

# Since \g<N> syntax is not available in RE definition,
# use formats like hexadecimal escapes to avoid ambiguity between normal digit characters and backreferences.
s = 'abcdefghijklmna1d'
re.sub(r'(.).*\1\x31', 'X', s)

