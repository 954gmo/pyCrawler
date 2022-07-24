
**escape sequences**

[docs.python: regular expression syntax](https://docs.python.org/3/library/re.html#regular-expression-syntax)

`\a \b \f \n \N \r \t \u \U \v \x \\`

using hexadecimal escape format \xNN

`re.escape()`

> `expr = '(a^b)`
> 
> `eqn = 'f*(a^b) - 3*(a^b)`
> 
> `re.sub(re.excape(expr) + r'\Z', 'c', eqn)`
> 
> `terms = ['a_42', '(a^b)', '2|3']`
> 
> `pat = re.compile('|'.join( re.escape(s) for s in terms))`
> 