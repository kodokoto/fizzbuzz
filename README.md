# One line modular fizzbuzz function

This is a modular, one line fizzbuzz function. You are able to easily change the range, the multiples, the words and the amount of both!

```
fizzBuzz = lambda multiples, *rangeArg: [(print(''.join([multiples[multiple]*(i%multiple==0) for multiple in multiples if i%multiple==0]) or i)) for i in range(*rangeArg)]
```


dictionary of multiples, key = multiples, value = word || You can add more than 2!

```
multiples = {3: 'Fizz', 5: 'Buzz'}
```

example of a call

```
fizzBuzz(multiples, 1, 100)
```
