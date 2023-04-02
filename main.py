collected_items = {'shards': 0, 'fragments': 0, 'motes': 0}
obtained = False
collected_item = ''
legendary_item = ''

while not obtained:
    elements = [x.lower() for x in input().split()]
    for x in range(0, len(elements), 2):
        current_item = elements[x + 1]
        if current_item not in collected_items:
            collected_items[current_item] = int(elements[x])
        else:
            collected_items[current_item] += int(elements[x])
            if collected_items[current_item] >= 250:
                collected_item = current_item
                collected_items[current_item] -= 250
                obtained = True
                if collected_item == "shards":
                    legendary_item = "Shadowmourne"
                elif collected_item == 'fragments':
                    legendary_item = "Valanyr"
                elif collected_item == 'motes':
                    legendary_item = 'Dragonwrath'

                print(f'{legendary_item} obtained!')
                for kliuch, stoinost in collected_items.items():
                    print(f'{kliuch}: {stoinost}')
                break