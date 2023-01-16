import sys

initial = [int(num) for num in input().split(" ")]
list1 = []
list2 = []
even = []
odd = []
condition = False
while condition == False:
    string = input().split()
    if string[0] == "exchange":
        number = int(string[1])
        if 0 <= int(string[1]) < int(len(initial)):
            list1 = initial[0:number + 1]
            list2 = initial[number + 1:]
            initial.clear()
            initial.extend(list2)
            initial.extend(list1)
            list1.clear()
            list2.clear()
        else:
            print("Invalid index")

    if string[0] == "max":
        maximum = -sys.maxsize
        max_saver = -sys.maxsize
        if string[1] == "even":
            for i in range(0, len(initial)):
                if int(initial[i]) % 2 == 0 and int(initial[i]) >= maximum:
                    maximum = int(initial[i])
                    max_saver = i
            if maximum != -sys.maxsize:
                print(max_saver)
            if maximum == -sys.maxsize:
                print("No matches")

        if string[1] == "odd":
            for i in range(0, len(initial)):
                if int(initial[i]) % 2 != 0 and int(initial[i]) >= maximum:
                    maximum = int(initial[i])
                    max_saver = i
            if maximum != -sys.maxsize:
                print(max_saver)
            if maximum == -sys.maxsize:
                print("No matches")

    if string[0] == "min":
        minimum = sys.maxsize
        min_saver = sys.maxsize
        if string[1] == "even":
            for i in range(0, len(initial)):
                if int(initial[i]) % 2 == 0 and int(initial[i]) <= minimum:
                    minimum = int(initial[i])
                    min_saver = i
            if minimum != sys.maxsize:
                print(min_saver)
            if minimum == sys.maxsize:
                print("No matches")

        if string[1] == "odd":
            for i in range(0, len(initial)):
                if int(initial[i]) % 2 != 0 and int(initial[i]) <= minimum:
                    minimum = int(initial[i])
                    min_saver = i
            if minimum != sys.maxsize:
                print(min_saver)
            if minimum == sys.maxsize:
                print("No matches")

    if string[0] == "first":
        counter = 0
        if string[2] == "even":
            while counter != int(string[1]):
                if int(string[1]) <= len(initial):
                    for i in range(0, len(initial)):
                        if counter == int(string[1]):
                            break
                        if initial[i] % 2 == 0:
                            even.append(initial[i])
                            counter += 1

                    if counter < int(string[1]):
                        print(even)
                        even.clear()
                        break
                else:
                    print("Invalid count")
                    break
            if counter == int(string[1]):
                print(even)
                even.clear()
        if string[2] == "odd":
            while counter != int(string[1]):
                if int(string[1]) <= len(initial):
                    for i in range(0, len(initial)):
                        if counter == int(string[1]):
                            break
                        if initial[i] % 2 != 0:
                            odd.append(initial[i])
                            counter += 1
                    if counter < int(string[1]):
                        print(odd)
                        odd.clear()
                        break
                else:
                    print("Invalid count")
                    break
            if counter == int(string[1]):
                print(odd)
                odd.clear()

    if string[0] == "last":
        counter = 0
        initial.reverse()
        if string[2] == "even":
            while counter != int(string[1]):
                if int(string[1]) <= len(initial):
                    for i in range(0, len(initial)):
                        if counter == int(string[1]):
                            break
                        if initial[i] % 2 == 0:
                            even.append(initial[i])
                            counter += 1
                    if counter < int(string[1]):
                        initial.reverse()
                        even.reverse()
                        print(even)
                        even.clear()
                        break
                else:
                    print("Invalid count")
                    break
            if counter == int(string[1]):
                initial.reverse()
                even.reverse()
                print(even)
                even.clear()
        if string[2] == "odd":
            while counter != int(string[1]):
                if int(string[1]) <= len(initial):
                    for i in range(0, len(initial)):
                        if counter == int(string[1]):
                            break
                        if initial[i] % 2 != 0:
                            odd.append(initial[i])
                            counter += 1
                    if counter < int(string[1]):
                        initial.reverse()
                        odd.reverse()
                        print(odd)
                        odd.clear()
                        break
                else:
                    print("Invalid count")
                    break
            if counter == int(string[1]):
                initial.reverse()
                odd.reverse()
                print(odd)
                odd.clear()

    if string[0] == "end":
        print(initial)
        condition = True
        break