first_letter = input()
last_letter = input()
no_letter = input()
counter = 0

for i in range(ord(first_letter), ord(last_letter)+1):
    if i == ord(no_letter):
        continue
    for f in range(ord(first_letter), ord(last_letter)+1):
        if f == ord(no_letter):
            continue
        for g in range(ord(first_letter), ord(last_letter)+1):
            if g == ord(no_letter):
                continue
            print(f"{chr(i)}{chr(f)}{chr(g)}", end=" ")
            counter += 1
print(counter)
