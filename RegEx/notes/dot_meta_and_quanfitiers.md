greedy quantifiers, can be applied to characters and groupings

quantifiers have functionality like the string repetition operator and range function

> `?` : quantifies a character or group to match `0` or `1` times. that is optional match
> 
> `*` : `0` or more times
> 
> `+` : `1` or more times
> 
> `{m, n}, {m,}, {,n}, {n}`


**conditional AND** using dot metacharacter and quantifiers

`bool(re.search(r'Error.*valid', 'Error: not a valid input'))`

**Non-greedy/lazy/reluctant quantifiers**: appending a `?` to greedy quantifier

`[w for w in demo if re.search(r'ab{1,4}c', w)]`