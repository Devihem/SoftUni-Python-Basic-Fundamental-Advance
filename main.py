def roman_to_int(roman):
    roman_numerals = {
        'I': '1', 'V': '5', 'X': '10', 'L': '50',
        'C': '100', 'D': '500', 'M': '1000'
    }

    translation_table = str.maketrans(roman_numerals)
    integer_value = roman.translate(translation_table)

    return int(integer_value)

roman_numeral = 'MCMIX'
integer_value = roman_to_int(roman_numeral)
print(integer_value)  # Output: 1909
