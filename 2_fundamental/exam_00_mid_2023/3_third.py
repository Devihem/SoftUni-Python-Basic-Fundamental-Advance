books = input().split("&")

while True:

    command = input().split(" | ")
    if command[0] == "Done":
        break
    elif command[0] == "Add Book":
        if command[1] in books:
            continue
        else:
            books.insert(0, command[1])
    elif command[0] == "Take Book":
        if command[1] in books:
            books.remove(command[1])
    elif command[0] == "Swap Books":
        if command[1] in books and command[2] in books:
            book_index_1 = books.index(command[1])
            book_index_2 = books.index(command[2])
            books[book_index_1], books[book_index_2] = books[book_index_2], books[book_index_1]
    elif command[0] == "Insert Book":
        if command[1] in books:
            continue
        else:
            books.append(command[1])
    elif command[0] == "Check Book":
        if int(command[1]) < len(books):
            print(books[int(command[1])])

print(', '.join(books))
