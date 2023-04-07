events_list = ["coding", "dog", "cat", "movie"]
coffees_added = 0
total_coffees = 0

while True:
    events = input()
    if events == "END":
        break

    if events.isupper():
        coffees_added = 2
    elif events.islower():
        coffees_added = 1

    if events.lower() in events_list:
        total_coffees += coffees_added

if total_coffees < 6:
    print(total_coffees)
else:
    print("You need extra sleep")
