from math import floor
from functools import reduce

symbols = input().split()
result = 0
functions = {
    '*': lambda i: reduce(lambda x, y: int(x) * int(y), symbols[0:index]),
    '/': lambda i: reduce(lambda x, y: int(x) / int(y), symbols[0:index]),
    '+': lambda i: reduce(lambda x, y: int(x) + int(y), symbols[0:index]),
    '-': lambda i: reduce(lambda x, y: int(x) - int(y), symbols[0:index])
}
index = 0

while index < len(symbols):
    if symbols[index] in ['*', '+', '/', '-']:
        result = functions[symbols[index]](index)
        symbols = symbols[index:]
        symbols[0] = result
        index = 0
    index += 1

print(floor(result))
