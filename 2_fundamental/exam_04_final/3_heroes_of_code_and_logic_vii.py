heroes_hp = {}
heroes_mp = {}
max_hp = 100
max_mp = 200
heroes_count = int(input())

# Heroes Input and Format
for new_hero_count in range(heroes_count):
    new_hero_info = input().split(" ")
    new_hero_name = new_hero_info[0]
    new_hero_hp = int(new_hero_info[1])

    if new_hero_hp > max_hp:
        new_hero_hp = max_hp
    new_hero_mp = int(new_hero_info[2])
    if new_hero_mp > max_mp:
        new_hero_mp = max_mp

    heroes_hp[new_hero_name] = new_hero_hp
    heroes_mp[new_hero_name] = new_hero_mp

# Commands
while True:

    command = input().split(" - ")
    if command[0] == "End":
        break

    # Command - CastSpell
    elif command[0] == "CastSpell":
        hero_name = command[1]
        needed_mp = int(command[2])
        spell_name = command[3]
        if needed_mp <= heroes_mp[hero_name]:
            heroes_mp[hero_name] = heroes_mp[hero_name] - needed_mp
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_mp[hero_name]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    # Command - TakeDamage
    elif command[0] == "TakeDamage":
        hero_name = command[1]
        damage = int(command[2])
        hero_attacker = command[3]
        heroes_hp[hero_name] = heroes_hp[hero_name] - damage
        if heroes_hp[hero_name] > 0:
            print(f"{hero_name} was hit for {damage} HP by {hero_attacker} and now has {heroes_hp[hero_name]} HP left!")
        else:
            heroes_hp.pop(hero_name)
            heroes_mp.pop(hero_name)
            print(f"{hero_name} has been killed by {hero_attacker}!")

    # Command - Recharge
    elif command[0] == "Recharge":
        hero_name = command[1]
        recover_mp = int(command[2])
        heroes_mp[hero_name] = heroes_mp[hero_name] + recover_mp
        if heroes_mp[hero_name] > max_mp:
            recover_mp = recover_mp - (heroes_mp[hero_name] - max_mp)
            heroes_mp[hero_name] = max_mp
        print(f"{hero_name} recharged for {recover_mp} MP!")

    # Command - Heal
    elif command[0] == "Heal":
        hero_name = command[1]
        heal_hp = int(command[2])
        heroes_hp[hero_name] = heroes_hp[hero_name] + heal_hp
        if heroes_hp[hero_name] > max_hp:
            heal_hp = heal_hp - (heroes_hp[hero_name] - max_hp)
            heroes_hp[hero_name] = max_hp
        print(f"{hero_name} healed for {heal_hp} HP!")

for hero_print in heroes_hp.keys():
    print(hero_print)
    print(f"  HP: {heroes_hp[hero_print]}")
    print(f"  MP: {heroes_mp[hero_print]}")
