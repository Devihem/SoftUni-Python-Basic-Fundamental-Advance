tab_open = int(input())
salary = int(input())

website = ""
fine = 0

for i in range(0, tab_open):
    website = input()
    if website == "Facebook":
        fine += 150
    elif website == "Instagram":
        fine += 100
    elif website == "Reddit":
        fine += 50

if salary <= fine:
    print("You have lost your salary.")
else:
    print(salary-fine)



