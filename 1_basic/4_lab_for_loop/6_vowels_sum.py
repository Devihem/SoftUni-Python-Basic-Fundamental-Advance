zext = input()

sumz = 0

for i in zext:
    if i == "a":
        sumz = sumz+1
    if i == "e":
        sumz = sumz+2
    if i == "i":
        sumz = sumz+3
    if i == "o":
        sumz = sumz+4
    if i == "u":
        sumz = sumz+5

print(sumz)
