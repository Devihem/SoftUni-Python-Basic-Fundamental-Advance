standard_counter = 0
student_counter = 0
kid_counter = 0
all_total_tickets = 0
all_total_kid_tickets = 0
all_total_standard_tickets = 0
all_total_student_tickets = 0

cinema_working = True

while cinema_working:
    movie_name = input()
    if movie_name == "Finish":
        cinema_working = False
        break
    cinema_seats = int(input())
    for i in range(1, cinema_seats+1):
        type_of_ticket = input()
        if type_of_ticket == "End":
            break
        if type_of_ticket == "standard":
            standard_counter += 1
        elif type_of_ticket == "student":
            student_counter += 1
        elif type_of_ticket == "kid":
            kid_counter += 1
    total_tickets = kid_counter + standard_counter + student_counter
    all_total_tickets += total_tickets
    all_total_kid_tickets += kid_counter
    all_total_standard_tickets += standard_counter
    all_total_student_tickets += student_counter
    print(f"{movie_name} - {(total_tickets/cinema_seats)*100:.2f}% full.")
    standard_counter = 0
    student_counter = 0
    kid_counter = 0

print(f"Total tickets: {all_total_tickets}")
print(f"{(all_total_student_tickets/all_total_tickets)*100:.2f}% student tickets.")
print(f"{(all_total_standard_tickets/all_total_tickets)*100:.2f}% standard tickets.")
print(f"{(all_total_kid_tickets/all_total_tickets)*100:.2f}% kids tickets.")

