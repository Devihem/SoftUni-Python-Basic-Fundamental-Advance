import re


def demon_hp(hp_symbols: list):
    hp = 0
    for symbol in hp_symbols:
        hp += ord(symbol)
    return hp


def demon_dmg(dmg_numbers: list):
    dmg = 0
    for number in dmg_numbers:
        dmg += float(number)
    return dmg


def demon_multiplier_dmg(demon_dmg_pure: float, multiplier_symbols: list):
    multiply = multiplier_symbols.count("*")
    divide = multiplier_symbols.count("/")
    total_multiplier = multiply - divide
    if total_multiplier > 0:
        for multiplier_two in range(total_multiplier):
            demon_dmg_pure *= 2

    return demon_dmg_pure


pattern_hp = r"[^0-9\+\-\*\/\.]"
pattern_dmg = r"([\+\-]?[\d]+[.]?[\d]*)"
pattern_multiplier = r"([\*\/])"
demon_names_list = [demon_name.strip() for demon_name in input().split(",")]
demon_names_list = sorted(demon_names_list)
for demon in demon_names_list:
    match_hp = re.findall(pattern_hp, demon)
    match_dmg = re.findall(pattern_dmg, demon)
    match_multiplier = re.findall(pattern_multiplier, demon)
    demon_health = demon_hp(match_hp)
    demon_damage = demon_dmg(match_dmg)
    demon_damage = demon_multiplier_dmg(demon_damage, match_multiplier)
    print(f"{demon} - {demon_health} health, {demon_damage:.2f} damage")
