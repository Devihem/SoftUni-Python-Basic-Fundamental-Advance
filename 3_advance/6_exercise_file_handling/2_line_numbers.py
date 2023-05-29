from string import punctuation

# Opening the file in read mode - variable name : read_file
with open('text.txt', 'r') as read_file:
    # Reading the text and make a copy in text
    text = read_file.readlines()

# Opening and creating the file in write mode - variable name : output_file
with open('output.txt', 'w') as output_file:
    # Using the index to iterate over text and count the lines
    for line_index in range(len(text)):
        # checking for all letters with .isalpha
        # checking for all punctuation with in "punctuation" -> library 'string'
        total_symbols = [x for x in text[line_index] if x.isalpha()]
        total_punctuations = [x for x in text[line_index] if x in punctuation]

        # Write the data in the output file  in format [Line[row-index] [text][letter-count][punctuation-count]
        output_file.write(f'Line {line_index + 1}:'
                          f' {text[line_index][:-1]}'
                          f' ({len(total_symbols)})({len(total_punctuations)})\n')
