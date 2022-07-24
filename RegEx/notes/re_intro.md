[ref-src](https://learnbyexample.github.io/py_regular_expressions/re-introduction.html)

[module *re* documentaion](https://docs.python.org/3/library/re.html)

good practice:
* always use **raw string** to construct RE pattern `r'string', rb'string'`


> `re.search(pattern, string, flags=0)`
> 
> return: `re.Match` object when found, otherwise `None`

search *pattern* in *string* with *flag* behavior 

similar to using `in` operator to test whether a string is part of another string or not.

> `re.sub(pattern, repl, string, count=0, flags=0)`
> 
similar to using `str.replace(old_val, new_val, count)`
`repl` can be callable or string, 

> `re.compile(pattern, flags=0)`
> 
> return: `re.Pattern` object
> 
> useful if the RE has to be used in multiple places or called upon multiple times inside a loop.

> `re.Pattern.search(string[, pos[, endpos]])`
> 
> the `pos(start)` and `endpos(end)` index positions is similar to `range()` and slicing notation, the ending index has to be specified 1 greater than desicred index.
>
> `re.split(pattern, string, maxsplit=0, flags=0)`
> 
> similar to `str.split([sep[, maxsplit]])`
> 
> if the pattern used to split contains capture groups, the portions matched by those groups will also be a part of the output list.
> 
> `re.split(r'1*4?2', '31111111111251111426')`
> 
> `re.split(r'(1*4?2), '31111111111251111426')`
> 
> if part of the pattern is outside a capture group, the text thus matched won't be in the output.
> 
> if a capture group didn't participate, it will be represented by `None` in the output list.
> 
> `re.split(r'(1*)4?2', '31111111111251111426')`
> 
> `re.split(r'(a+)b+(c+)', '3.14aabccc42')`
> 
> `re.split(r'(1*)(4)?2', '31111111111251111426')`
> 
> use of capture groups and `maxsplit=1` gives behavior similar to `str.partition` method. 
> 
> `re.split(r'(a+b+c)', '3.14aabccc42abc88', maxsplit=1) # ==> str.partition`
> 


>
> `re.findall(pattern, string, flags=0)`
> 
> `re.findall(r'ab*c', 'abc ac adc abbbc')`
> 
> it is used for debugging purposes as well, for example to see the potential matches before applying substitution.
> 
> `re.findall(r't.*?a', 'that is quite a fabricated tale')`
> 
> if a single capture group is used, output will be a list of strings, Each element will have only the portion matched by the capture group.
> 
> if more than one capture group is used, output will be a list of tuples. Each element will be a tuple containing portions matched by all the capturing groups
> 
> `re.findall(r'a(b*)c', 'abc ac adc abbc xabbbcz bbb bc abbbbbc')`
> 
> `re.findall(r'(.*?)/(.*?)/(.*?)', '2020/04/25,1986/Mar/02,77/12/31')`
> 
> `re.finditer(pattern, string, flags=0)`
> 
> return an iterator object with each element as re.Match objects for each matched portion. 
> 
> 
> 
> `m_iter = re.finditer(r'ab+c', 'abc ac adc abbbc')`
> 
> `for m in m_iter: print(m)`
> 
> `re.subn`
> 
> 

> `>>> sentence = 'here is a string'`
> 
>  `'is' in sentence`
> 
>  ` 'xyz' in sentence`
> 
>  `bool(re.search(r'is', sentence))`
> 
>  `bool(re.search(r'xyz', sentence)`
> 
> `bool(re.search(r'HeRe', sentence, flag=re.I)`
> 
> `bool(re.search(r'HeRe', sentence)`
> 
> `if re.search(r'ring', sentence): do sth`
> 
> `>>> words = ['cat', 'attempt', 'tattle']`
> 
> `[w for w in words if re.search(r'at', w)]`
> 
> `all(re.search(r'at', w) for w in words)`
> 
> `any(re.search(r'stat', w) for w in words)`
> 
> `greeting="Have a nice day"`
> 
> `re.sub(r'e', 'E', greeting)`
> 
> `greeting.replace('e', 'E')`
> 
> `re.sub(r'e', 'E', greeting, count=2)`
> 
> `greeting.replace('e', 'E', count=2)`
> 
> `pet = re.compile(r'duck')`
> 
> `type(pet)`
> 
> `bool(pet.search('They have ducks')`
> 
> `pet.sub('cat', 'They have ducks')`
> 
> `word = re.compile(r'is')`
> 
> `bool(word.search(sentence, 4)) # search for 'is' starting from 5th character of 'sentence' variable` 
> 
> `bool(word.search(sentence, 2, 4)) # search for 'is' between 3rd and 4th characters.`
> 
> `byte_data = b'This is a sample string'`
> 
> `bool(re.search(rb'is', byte_data))`
> 
> `re.split(r'-', 'apple-85-mango-70', maxsplit=1) # ==> 'apple-85-mango-8-70.split('-', maxsplit=1)`
> 
> `re.split(r':.:', 'bus:3:car:5:van)`
> 