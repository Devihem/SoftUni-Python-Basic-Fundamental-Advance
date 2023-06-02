import random
import time

start_time = time.perf_counter()

x = random.randint(0, 1_000_000)
print(x)
y = -1
while y != x:
    y = random.randint(0, 1_000_000)




print(y)
end_time = time.perf_counter()

total_work_time = end_time - start_time

print(total_work_time)