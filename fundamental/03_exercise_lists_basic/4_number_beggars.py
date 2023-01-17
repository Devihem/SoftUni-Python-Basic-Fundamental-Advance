rewards_list = input().split(", ")
beggars_count = int(input())
beggars_given_rewards = []
beggar_order = 0
reward_sum = 0

for beggar in range(beggars_count):
    beggars_given_rewards.append(0)

for current_reward in rewards_list:
    beggar_order += 1
    reward_sum = int(current_reward) + int(beggars_given_rewards[beggar_order-1])
    beggars_given_rewards[beggar_order-1] = reward_sum

    if beggar_order == beggars_count:
        beggar_order = 0

print(beggars_given_rewards)

