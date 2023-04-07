days = 1
starting_point = 5364
end_point = 8848
current_point = starting_point
while True:
    status = input()
    if status == "END":
        break
    if status == "Yes":
        days += 1
    if status == "No":
        pass
    climbed_length = int(input())
    if days > 5:
        break
    current_point += climbed_length
    if current_point >= end_point:
        print(f"Goal reached for {days} days!")
        break


if current_point < end_point:
    print("Failed!")
    print(f"{current_point}")
