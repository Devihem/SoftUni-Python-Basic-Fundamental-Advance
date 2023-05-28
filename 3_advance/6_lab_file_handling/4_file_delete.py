import os
try:
    os.remove('my_first_file')
except FileNotFoundError:
    print('File already deleted!')