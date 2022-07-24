`re.Match` object

`re.Match.span()` : get the starting and ending+1 indexes of the matching portion. 

when capture groups are used with `re.search` or `re.fullmatch`, they can be retrieved using an index or `re.Match.group()`, 
the first element is always the entire matched portion and rest of the elements are for capture groups if they are present. 


using functions in replacement section

`re.sub(r'(a|b)\^2', lambda m: m[0].upper(), 'a^2 + b^2 - C*3')`

`re.sub(r'2|3', lambda m: str(int(m[0])**2), 'a^2 + b^2 - C*3)`

using dict in replacement section

`d = {'1': 'one', '2': 'two', '4':'four'}`

`re.sub(r'1|2|4', lambda m: d[m[0]], '9234012')`

`re.sub(r'[0-9]', lambda m: d.get(m[0], 'X'), '9234012')`

`swap = {'cat': 'tiger', 'tiger': 'cat'}`

`words = 'cat tiger dog tiger cat`

`re.sub(r'cat|tiger', lambda m: swap[m[0]], words)`



>
> assignment expressions
> 
> `if m:= re.search(r'(.*)s', 'oh!'): print(m[1])`
> 
> 
> 

>
> `re.search(r'b.*d', 'abc ac adc abbbc')[0]`
> 
> `re.search(r'b.*d', 'abc ac adc abbbc').group(0)`
> 
> `m = re.fullmatch(r'a(.*?) (.*)d(.*)c', 'abc ac adc abbbc')`
> 
> `m.group(3, 1)`
> 
> `m[2]`
> 
> `m.groups()`
> 
> `m.start(1), m.end(1), m.span(), m.start(), m.span(1)`
> 
> `pat = re.compile(r'hi.*bye')`
> 
> `m = pat.search('this is goodbye then', 1, 15)`
> 
> `m.pos, m.endpos, m.re, m.string`
> 
>
> 