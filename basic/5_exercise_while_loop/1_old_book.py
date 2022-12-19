specific_book = input()
books_loop = input()
books_count = 0

while specific_book != books_loop:
    if books_loop == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {books_count} books.")
        break
    books_loop = input()
    books_count += 1

else:
    print(f"You checked {books_count} books and found it.")
