element_set = set()
for _ in range(int(input())):
    for element in input().split():
        element_set.add(element)
print(*element_set, sep='\n')
