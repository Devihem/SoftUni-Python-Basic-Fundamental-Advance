def symbol_counter(half_ticket: str, key_symbols=('@', '#', '$', '^')):
    max_symbol_streak = 0
    symbol_streak = 0
    for char in half_ticket:
        if char == half_ticket[5]:
            symbol_streak += 1
        else:
            symbol_streak = 0

        if symbol_streak > max_symbol_streak:
            max_symbol_streak = symbol_streak
    return max_symbol_streak


tickets = [value.strip() for value in input().split(",")]
winning_symbols = ['@', '#', '$', '^']


for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
        continue
    half_1 = ticket[0:10]
    half_2 = ticket[10:]
    half_1_streak = symbol_counter(half_1)
    half_2_streak = symbol_counter(half_2)

    if half_1 == half_2 and half_1.count(half_2[0]) == 10 and half_1[5] in winning_symbols:
        print(f'ticket "{ticket}" - 10{half_2[0]} Jackpot!')
    elif (half_1_streak >= 6 and half_2_streak >= 6) and half_2[5] == half_1[5] and half_2[5] in winning_symbols:
        if half_2_streak > half_1_streak:
            max_same = half_1_streak
        else:
            max_same = half_2_streak
        print(f'ticket "{ticket}" - {max_same}{half_2[5]}')
    else:
        print(f'ticket "{ticket}" - no match')
