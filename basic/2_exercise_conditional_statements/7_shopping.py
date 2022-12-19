peter_budjet = float(input())
video_cards_pcs = int(input())
processors_pcs = int(input())
ram_pcs = int(input())

video_cards_price = 250
processors_price = (video_cards_price*video_cards_pcs)*0.35
ram_price = (video_cards_price*video_cards_pcs)*0.10

total_price = video_cards_price*video_cards_pcs+processors_price*processors_pcs+ram_price*ram_pcs

if video_cards_pcs > processors_pcs:
    total_price=total_price*0.85

deff = abs(peter_budjet-total_price)

if peter_budjet >= total_price:
    print(f"You have {deff:.2f} leva left!")
elif total_price > peter_budjet:
    print(f"Not enough money! You need {deff:.2f} leva more!")
