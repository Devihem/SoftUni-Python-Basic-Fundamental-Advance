import re

pattern_star_finder = r"[STAR]"
pattern_decrypt = r"@([A-Za-z]+)[^\@\-\!\:\>]*:(\d+)[^\@\-\!\:\>]*!([AD])![^\@\-\!\:\>]*->(\d+)"
messages_loop = int(input())
attacked_planets = []
destroyed_planets = []

for message_count in range(messages_loop):
    new_message = input()
    match_keys = re.findall(pattern_star_finder, new_message, re.IGNORECASE)
    msg_key = len(match_keys)
    decrypt_msg = ""
    for symbol in new_message:
        decrypt_symbol = chr(ord(symbol) - msg_key)
        decrypt_msg += decrypt_symbol
    match_message = re.search(pattern_decrypt, decrypt_msg)
    if match_message:
        planet, population, attack_type, soldiers = match_message.groups()
        if attack_type == "A":
            attacked_planets.append(planet)
        elif attack_type == "D":
            destroyed_planets.append(planet)

sorted_attacked_planets = sorted(attacked_planets)
sorted_destroyed_planets = sorted(destroyed_planets)

print(f"Attacked planets: {len(attacked_planets)}")
[print(f"-> {planet_a}") for planet_a in sorted_attacked_planets]
print(f"Destroyed planets: {len(destroyed_planets)}")
[print(f"-> {planet_d}") for planet_d in sorted_destroyed_planets]
