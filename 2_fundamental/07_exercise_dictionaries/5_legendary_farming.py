legendary_materials_dict = {"shards": 0, "fragments": 0, "motes": 0}
junk_materials_dict = {}
legendary_weapon_flag = False
legendary_name = ""
while True:
    for material in legendary_materials_dict:
        if legendary_materials_dict[material] >= 250:
            legendary_weapon_flag = True
            if material == "shards":
                legendary_name = "Shadowmourne"
            elif material == "fragments":
                legendary_name = "Valanyr"
            elif material == "motes":
                legendary_name = "Dragonwrath"

            legendary_materials_dict[material] -= 250

    if legendary_weapon_flag:
        break

    new_farm = [item.lower() for item in input().split()]

    for items in range(0, len(new_farm), 2):
        for material in legendary_materials_dict:
            if legendary_materials_dict[material] >= 250:
                legendary_weapon_flag = True
        if legendary_weapon_flag:
            break

        if new_farm[items + 1] not in legendary_materials_dict:
            if new_farm[items + 1] not in junk_materials_dict:
                junk_materials_dict[new_farm[items + 1]] = int(new_farm[items])
            else:
                junk_materials_dict[new_farm[items + 1]] += int(new_farm[items])
        else:
            legendary_materials_dict[new_farm[items + 1]] += int(new_farm[items])

print(f"{legendary_name} obtained!")
[print(f"{items}: {legendary_materials_dict[items]}") for items in legendary_materials_dict]
[print(f"{items_junk}: {junk_materials_dict[items_junk]}") for items_junk in junk_materials_dict]
