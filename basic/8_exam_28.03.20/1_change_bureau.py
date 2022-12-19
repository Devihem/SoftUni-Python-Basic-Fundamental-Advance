inp_btc = int(input())
inp_ioan = float(input())
tax = float(input())

btc = 1168
dollar = 1.76
evro = 1.95

btc_to_leva = inp_btc * btc
dollar_inp = ioan_to_dollar = inp_ioan * 0.15
dollar_to_leva = dollar_inp * dollar
total_leva = btc_to_leva + dollar_to_leva
total_evro = (total_leva / 1.95) * (1-tax/100)

print(f"{total_evro:.2f}")
