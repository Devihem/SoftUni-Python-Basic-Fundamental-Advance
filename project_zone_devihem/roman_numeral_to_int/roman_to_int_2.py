# Reverse - With Last Number

numeral = "MCMXLVIII"

r_num_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, }
last_el = numeral[-1]
result = 0

for el in numeral[::-1]:

    if r_num_dict[last_el] > r_num_dict[el]:
        result -= r_num_dict[el]
    else:
        result += r_num_dict[el]

    last_el = el

print(result)
