from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(number) for number in input().split()]
locks = deque([int(number) for number in input().split()])
safe_reward_value = int(input())
bullets_count = len(bullets)
loaded_bullets_in_barrel = deque([bullets.pop() for _ in range(gun_barrel_size) if bullets])
bullets_cost = 0

while bullets_count > 0 and locks:

    # Current Lock and Bullet loaded
    current_lock = locks.popleft()
    current_bullet = loaded_bullets_in_barrel.popleft()
    bullets_count -= 1
    bullets_cost += bullet_price

    # Unlocking or Fail
    if current_bullet <= current_lock:
        print("Bang!")
    else:
        locks.appendleft(current_lock)
        print("Ping!")

    # Reloading
    if len(loaded_bullets_in_barrel) == 0 and len(bullets) > 0:
        loaded_bullets_in_barrel = deque([bullets.pop() for _ in range(gun_barrel_size) if bullets])
        print("Reloading!")
else:
    if locks:
        print(f"Couldn't get through. Locks left: {len(locks)}")
    else:
        print(f"{bullets_count} bullets left. Earned ${safe_reward_value - bullets_cost}")