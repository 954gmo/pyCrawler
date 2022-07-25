# Regular Expressions

* **essence**: a mini "programming language"
* **usage**: text processing
* **Syntax and features of regular expressions vary from language to language, here it is using Python**
* formal language theory
* state diagram of a finite-state automation
* does this string match the pattern? or Is there a match for the pattern anywhere in this string?
* modify a string
* split it apart in various ways.
* not all possible string processing tasks can be done using RE, use python code
* before turning to the re module, consider whether your problem can be solved with a faster and simpler string method.
* always use **raw string** to construct RE pattern `r'string', rb'string'`
* 
> **matching characters**
> 
> **repeating things**: `?, +, *, {m,n}, {m,}, {,n}, {n}`, greedy and non-greedy
> 
> **modifying strings**
> 
### Metacharacters
>> **metacharacters**: characters with special meaning,  *restrictions* are made by metacharacters, can be escaped with `\ `, 
>> 
>> a complete list of metacharacters: `. ^ $ * + ? { } [ ] \ | ( ) \A \Z \b \B \W \w \d \D`
>>
>> `\ ` used to signal special sequences or escape metacharacters
>> 

### Anchors
> **String anchors**, **Line anchors**, **word anchors**,
>> `\A, \Z`; `^, $`; `\b, \B`
> 
> **string anchors**
>
> `( \A pat \Z )` V.S. `re.fullmatch(pattern, string, flags=0)` 
> 
> similar to `str.startwith(prefix[, start[, end]])` and `str.endwith(suffix[, start[, end]])`
> 
> `re.fullmatch` similar to `==`
> 
> return `re.Match` object
>
> **line anchors**
>
> `^` and `$`, start and end of line
> 
> a string input may contain single or multiple lines. 
> 
> if there are no newline characters in the input string, these will behave same as `\A` and `\Z`
>
> **word anchors**
>
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

### Character class
> `[]`
> 
> a set of characters that you wish to match, characters can be listed individually, or a range of characters.
> 
> metacharacters(except `\ `) are not active inside classes. 
> 
> complement of a set `[^]`

### Alternation
> `|` and  precedence rules
> 
> similar to logical OR, allows you to combine multiple patterns.
> 
> precedence rules: no ambiguity for testing a match to get T/F, but for other things like string replacement.
> 
> the alternative which matches earliest in the input string gets precedence
> 
> if alternatives match on same index, the precedence is then left to right in the order of declaration.
> 

### Grouping
> `()`
>
> **backreference**
> 
>> backreference : same as `re.Match.group(n)`, but used directly in RE definition as well as replacement section without having to invoke and apply quantifiers to backreference
> `\1, \2 ... \99`
> `\0, \NNN` will be interpreted as octal value
> `\g<1>, \g<2> ...`
> `\g<0>` refer to entire matched portion `== re.Match[0]`
>
> **non-capturing groups**: `(?:pat)`
> 
> **named capture groups** : `(?P<name>pat), (?P=name)`, `groupdict()`
> 
> **conditional groups**: `(?(id/name)yes-pattern|no-pattern)`
> 
> **Lookarounds assertion** (zero-width assertion)
>
>> **negative lookahead**: `(?!pat)`
>>
>> **negative lookbehind**: `(?<!pat)`
>>
>> **positive lookahead**: `(?=pat)`: 
>>
>> **positive lookbehind**: `(?<=pat)`
>>

### Quantifiers
> **greedy quantifier** `?, *, +, {m,n}, {m,}, {,n}, {n}`
> 
> **non-greedy quantifier** : append `?` to greedy quantifier

### Flags
> `re.IGNORECASE or re.I`
> 
> `re.DOTALL or re.S`
> 
> `re.MULTILINE or re.M`
> 
> `re.VERBOSE or re.X`
> 
> `re.ASCII or re.A`
> 
> `re.LOCALE or re.L`

