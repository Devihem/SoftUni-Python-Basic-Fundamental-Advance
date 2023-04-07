import random
import string

all_letters = string.ascii_letters
symbols = string.punctuation
digits = string.digits

all_string_symbols = all_letters+symbols+digits
length = 12

password = "".join(random.sample(all_string_symbols, length))
print(password)