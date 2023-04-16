from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(number) for number in input().split()]
locks = [int(number) for number in input().split()]
safe_reward_value = int(input())
bullets_count = len(bullets)
loaded_bullets_in_barrel = deque([])

while bullets_count > 0 and locks:

    # Reloading
    if len(loaded_bullets_in_barrel) == 0:
        loaded_bullets_in_barrel = [bullets.pop() for _ in range(gun_barrel_size) if bullets]

    current_bullet = loaded_bullets_in_barrel.popleft()
    bullets_count -= 1

    print("BULLET")


print(bullet_price)
print(gun_barrel_size)
print(bullets)
print(locks)
print(safe_reward_value)