# One line modular fizzbuzz function

This is a modular, one line fizzbuzz function. You are able to easily change the range, the multiples, the words and the amount of both!

```
fizzBuzz = lambda multiples, *rangeArg: [(print(''.join([multiples[multiple]*(i%multiple==0) for multiple in multiples]) or i)) for i in range(*rangeArg)]
```


dictionary of multiples, key = multiples, value = word || You can add more than 2!

```
multiples = {3: 'Fizz', 5: 'Buzz'}
```

example of a call

```
fizzBuzz(multiples, 1, 100)
```

# Explination:

lambda takes in dict of multiples and range arguments 

```
lambda multiples, *rangeArg:
```

output the values if the multiple goes into i

```
multiples[multiple]*(i%multiple==0)
```

for each multiple in the multiples dictionary

```
for multiple in multiples
```

else output i

```
or i
```

do this for every number i in the range given
```
for i in range(*rangeArg)
```

