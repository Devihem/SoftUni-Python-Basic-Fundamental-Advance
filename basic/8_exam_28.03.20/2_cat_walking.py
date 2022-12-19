minuets_walking = int(input())
walkings = int(input())
calories = int(input())

total_burned = minuets_walking * walkings * 5

if calories/2 <= total_burned:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_burned}." )
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_burned}.")