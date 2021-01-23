# lambda takes in dict of multiples and range      || This part prints each value depending if the key(multiple) goes into i, else print i      || iterate through i by range given
fizzBuzz = lambda multiples, *rangeArg: [(print(''.join([multiples[multiple]*(i%multiple==0) for multiple in multiples if i%multiple==0]) or i)) for i in range(*rangeArg)]
# dictionary of multiples, key = multiples, value = word || You can add more than 2!
multiples = {3: 'Fizz', 5: 'Buzz'}
fizzBuzz(multiples, 1, 100)