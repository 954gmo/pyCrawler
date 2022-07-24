# Anchors ( *string* / *line* / *word* anchors)
**string anchors**

> `( \A` and `\Z )` and `re.fullmatch(pattern, string, flags=0)` 
> 
> similar to `str.startwith(prefix[, start[, end]])` and `str.endwith(suffix[, start[, end]])`
> 
> `re.fullmatch` similar to `==`
> 
> return `re.Match` object

**line anchors**

> `^` and `$`, start and end of line
> 
> a string input may contain single or multiple lines. 
> 
> if there are no newline characters in the input string, these will behave same as `\A` and `\Z`

**word anchors**

> alphabets(irrespective of case), digits and the underscore character
> 
>  word characters: `[a-zA-Z0-9_]`, 
> 
> `\b` and `\B` word boundary, start of word and end of word
> 
> start of word means either the character prior to the word is a non-word character or there is no character(start of string)
> 
> end of word means either the character after the word is a non-word character or no character(end of string), 
> 

>`bool(re.search(r'\Acat', 'cater'))`
> 
> `bool(re.search(r'are\Z', 'spare'))`
> 
> `re.sub(r'\A', 're', 'live')`
> 
> `re.sub(r'\Z', 'er', 'hack')`
> 
> `pat = re.compile(r'\Aat')`
> 
> `bool(pat.search('cater', 1))`
> 
> `bool(pat.search('cater'[1:]))`
> 
> `pat = re.compile(r'\Acat\Z')`
> 
> `bool(pat.search('cat'))`
> 
> `pat = re.compile(r'cat', flags=re.I)`
> 
> `bool(pat.fullmatch('Cat'))`
> 
> `pets = 'cat and dog`
> 
> `bool(re.search(r'^cat', pets)`
> 
> `bool(re.search(r'dog$', pets)`
> 
> `greeting = 'hi there\nhave a nice day\n`
> 
> `bool(re.search(r'day$', greeting))`
> 
> `bool(re.search(r'day\n$', greeting))`
> 
> `bool(re.search(r'day\Z', greeting))`
> 
> `bool(re.search(r'day\n\Z', greeting))`
> 
> `bool(re.search(r'^par$', 'spare\npar\ndare', flags=re.M))`
> 
> `ip_lines = 'catapults\nconcatenate\ncat'`
> 
> `bool(re.sub(r'^', '* ', ip_lines, flags=re.M))`
> 
> `bool(re.sub(r'$', '.', ip_lines, flags=re.M))`
> 
> `words = 'par spar apparent spare part'`
> 
> `re.sub(r'par', 'X', words) # replace 'par' irrespective of where it occurs` 
> 
> `re.sub(r'\bpar\b', 'X', words)`
> 
> 
