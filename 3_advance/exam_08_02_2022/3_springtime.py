def start_spring(**spring_dict):
    new_spring_dict = {}
    for key, value in spring_dict.items():
        if value not in new_spring_dict:
            new_spring_dict[value] = []
        new_spring_dict[value].append(key)

    new_spring_dict = {key: sorted(value) for key, value in new_spring_dict.items()}

    sorted_types = sorted(new_spring_dict.items(), key=lambda k: (-len(k[1]), k[0]))

    final_print_string = ''
    for key, value in sorted_types:
        final_print_string += key + ':\n'
        for val in value:
            final_print_string += '-'+ val+'\n'

    return final_print_string


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird", }
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
