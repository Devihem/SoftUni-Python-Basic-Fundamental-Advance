# Forward with last number
numeral = "MCMXLVIII"
r_num_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, }

last_number = r_num_dict[numeral[0]]
result = 0

for symbol in numeral:
    current_number = r_num_dict[symbol]
    if last_number < current_number:
        result -= last_number * 2
    result += current_number
    last_number = current_number

print(result)
