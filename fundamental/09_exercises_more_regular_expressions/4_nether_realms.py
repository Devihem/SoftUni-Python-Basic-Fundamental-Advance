import re


#  Възможен проблем със спейсовете в имената ?
#  Да се направят още два Дефф-а за ДМГ


def demon_hp(hp_symbols: list):
    hp = 100
    for symbol in hp_symbols:
        print(symbol)
    return hp


pattern_hp = r"[^0-9\+\-\*\/\.]"
pattern_dmg = r"([\+\-]?[\d+][.]?[\d]*)"
pattern_multiplier = r"([\*\/])"
demon_names_list = sorted(input().split(", "))
for demon in demon_names_list:
    print(demon)
    match_hp = re.findall(pattern_hp, demon)
    match_dmg = re.findall(pattern_dmg, demon)
    match_multiplier = re.findall(pattern_multiplier, demon)
    demon_health = demon_hp(match_hp)
    print(match_hp)
    print(match_dmg)
    print(match_multiplier)
