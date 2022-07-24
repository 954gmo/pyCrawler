# alternation and grouping

**alternation** 

> similar to logical OR, allows you to combine multiple patterns. 
> 
> `|`
> 
> precedence rules: no ambiguity for testing a match to get T/F, but for other things like string replacement.
> 
> the alternative which matches earliest in the input string gets precedence
> 
> if alternatives match on same index, the precedence is then left to right in the order of declaration.
> 

**grouping**


> `re.sub(r'\Acat|cat\b', 'X', 'catapults concatenate cat scat')`
> 
> `words = ['cat', 'dog', 'fox']`
> 
> `re.sub(r'|'.join(words), 'mammal', 'cat dog bee parrot fox') `
> 
> `re.sub(r're(form|st)', 'X', 'red reform read arrest')`
> 
> `alt = re.compile(r'\b(' + '|'.join(words) + r')\b')`
> 
> `alt.sub('X', 'cater cat concatenate par spare')`
> 
> `terms = ['no', 'ten', 'it']`
> 
>  `items = ['dip', 'nobody', 'it', 'oh', 'no', 'bitten']`
> 
> `pat = re.compile('|'.join(terms))`
> 
> `[w for w in words if pat.fullmatch(w)]`
> 
> `words = ['hand', 'handy', 'handful']`
> 
> `alt = re.compile('|'.join(sorted(words, key=len, reverse=True)))`
> 