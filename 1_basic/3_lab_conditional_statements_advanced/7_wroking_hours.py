time = int(input())
day = input()

time = 10 <= time <= 18
day = day == "Monday" or day == "Tuesday" or day == "Wednesday"\
      or day == "Thursday" or day == "Friday" or day == "Saturday"

if time == True and day == True:
    print("open")
else:
    print("closed")
