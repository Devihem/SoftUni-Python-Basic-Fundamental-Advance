# Trying overcomplicated comprehension
[print(el, end=' ') for row in reversed([row.split() for row in input().split('|')]) for el in row if el != " "]
