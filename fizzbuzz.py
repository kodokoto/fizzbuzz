fizzBuzz = lambda multiples, *args: [(print(''.join([multiples[multiple]*(i%multiple==0) for multiple in multiples if i%multiple==0]) or i)) for i in range(*args)]
multiples = {3: 'Fizz', 5: 'Buzz'}
fizzBuzz(multiples, 1, 100)