def fill_the_box(*args):
    width, height, depth, *commands = args
    box_size = width * height * depth
    filling_the_box = 0
    for command in commands:
        if command == "Finish":
            break
        filling_the_box += command
    if box_size > filling_the_box:
        return f"There is free space in the box. You could put {box_size - filling_the_box} more cubes."
    else:
        return f"No more free space! You have {filling_the_box - box_size} more cubes."

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))