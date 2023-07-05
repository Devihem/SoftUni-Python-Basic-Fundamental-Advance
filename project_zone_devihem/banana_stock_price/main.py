data_dict_price = {
    "Kaufland": 3.50,
    "Billa": 3.60,
    "Metro": 3.40,
    "Lidl": 3.70
}

result = sum(data_dict_price.values()) / len(data_dict_price.values())

print(""
      " _"
      "\n//\\"
      "\nV  \\"
      "\n \\  \\_"
      "\n  \\,'.`-."
      "\n   |\\ `. `.     "
      "\n   ( \\  `. `-.                        _,.-:\\"
      "\n    \\ \\   `.  `-._             __..--' ,-';/"
      "\n     \\ `.   `-.   `-..___..---'   _.--' ,'/"
      "\n      `. `.    `-._        __..--'    ,' /"
      "\n        `. `-_     ``--..''       _.-' ,'"
      "\n          `-_ `-.___        __,--'   ,'"
      "\n             `-.__  `----\"\"\"    __.-'"
      "\n                  `--..____..--'"
      "\n")

print(f'Current Price  - {result} лв/кг')
