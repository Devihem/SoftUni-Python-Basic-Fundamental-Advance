men_count = int(input())
women_count = int(input())
max_tables = int(input())
counter = 0

for m in range(1, men_count+1):
    pass
    for f in range(1, women_count+1):
        if counter >= max_tables:
            break
        counter += 1
        print(f"({m} <-> {f})", end=" ")