# fizzBuzz = lambda multiples, *args: [i if i%multiple==0 else multiples[multiple] for i in range(*args) for multiple in multiples]
fizzBuzz = lambda multiples, *args: [multiples[multiple] for i in range(*args) for multiple in multiples if i%multiple==0]

multiples = {3: 'Fizz', 5: 'Buzz'}
res = fizzBuzz(multiples, 1, 100)
print(res)


# def getFizzBuzz(multiples, *args):
#     for i in range(*args):
