# Opening the file in reading mode - variable name : read_file
with open('text.txt', 'r') as read_file:

    # Reading the text and make a copy in text
    text = read_file.readlines()
    # Symbols that must be replaced in 'text' with '@'
    replacing_symbols = ["-", ",", ".", "!", "?"]

    # For loop with size of step [2] , going through only the even lines, as per condition of the task
    for line_index in range(0, len(text), 2):

        for symbol in replacing_symbols:

            # replacing every symbol in the text with '@'
            text[line_index] = text[line_index].replace(symbol, '@')

        # Printing the text line before going out of the loop, using the same line_index
        # text at index[line_index] unpacked , split by ' '  and printed with reverse order
        print(*text[line_index].split()[::-1])
