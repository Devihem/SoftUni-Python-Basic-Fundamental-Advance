cake_size_1 = int(input())
cake_size_2 = int(input())

left_pieces = cake_size_1*cake_size_2

while left_pieces > 0:
    tooked_pieces = input()
    if tooked_pieces == "STOP":
        print(f"{left_pieces} pieces are left.")
        break
    else:
        tooked_pieces = int(tooked_pieces)
        left_pieces = left_pieces - tooked_pieces
else:
    print(f"No more cake left! You need {-left_pieces} pieces more.")