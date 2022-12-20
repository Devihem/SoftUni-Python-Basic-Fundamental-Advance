number_one = int(input())
number_two = int(input())

vessel_one = number_one
vessel_two = number_two
number_one = vessel_two
number_two = vessel_one

print("Before:")
print(f"a = {vessel_one}")
print(f"b = {vessel_two}")
print("After:")
print(f"a = {number_one}")
print(f"b = {number_two}")