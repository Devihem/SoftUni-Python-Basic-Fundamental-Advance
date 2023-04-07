ticket_student_counter = 0
ticket_standard_counter = 0
ticket_kid_counter = 0
total_tickets_current = 0

while True:
    movie_name = input()

    if movie_name == "Finish":
        break
    free_seats = int(input())

    for i in range(0, free_seats):
        type_of_ticket = input()

        if type_of_ticket == "End":
            break
        if type_of_ticket == "student":
            ticket_student_counter += 1
        elif type_of_ticket == "standard":
            ticket_standard_counter += 1
        elif type_of_ticket == "kid":
            ticket_kid_counter += 1
        total_tickets_current += 1

    print(f"{movie_name} - {total_tickets_current / free_seats * 100:.2f}% full.")
    total_tickets_current = 0

total_tickets = ticket_kid_counter + ticket_student_counter + ticket_standard_counter
print(f"Total tickets: {total_tickets}")
print(f"{ticket_student_counter / total_tickets * 100:.2f}% student tickets.")
print(f"{ticket_standard_counter / total_tickets * 100:.2f}% standard tickets.")
print(f"{ticket_kid_counter / total_tickets * 100:.2f}% kids tickets.")
