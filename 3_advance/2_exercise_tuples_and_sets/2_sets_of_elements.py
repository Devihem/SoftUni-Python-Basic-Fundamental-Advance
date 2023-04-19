length_set_1, length_set_2 = [int(x) for x in input().split()]

set_1 = {int(input()) for _ in range(length_set_1)}
set_2 = {int(input()) for _ in range(length_set_2)}

print(*set_1.intersection(set_2), sep='\n')
