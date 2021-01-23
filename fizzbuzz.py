fizzBuzz = lambda multiples, *rangeArg: [(print(''.join([multiples[multiple]*(i%multiple==0) for multiple in multiples]) or i)) for i in range(*rangeArg)]
multiples = {3: 'Fizz', 5: 'Buzz'}
fizzBuzz(multiples, 1, 100)