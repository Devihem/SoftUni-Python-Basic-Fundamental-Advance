from pyfiglet import figlet_format


def print_art(text):
    ascii_art = figlet_format(text,graphit)
    return ascii_art


msg = input("What would you like to print? ")
print(print_art(msg))
