counter = 0
prime = 0
non_prime = 0
loop_is = True
while loop_is:
    number = input()
    if number == "stop":
        break
    else:
        number = int(number)
        for i in range(1, number+1):
            for f in range(1, i+1):
                if i % f == 0:
                    counter += 1
            if counter == 2:
                prime += i
            elif counter > 2:
                non_prime += i
            counter = 0

print(prime)
print(non_prime)