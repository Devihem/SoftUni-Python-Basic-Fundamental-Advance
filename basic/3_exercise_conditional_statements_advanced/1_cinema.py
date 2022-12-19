movie_price_type = input()
theater_rows = int(input())
theater_columns = int(input())
income = 0
cinema_capacity = theater_rows*theater_columns

if movie_price_type == "Premiere":
    income = cinema_capacity * 12
elif movie_price_type == "Normal":
    income = cinema_capacity * 7.50
elif movie_price_type == "Discount":
    income = cinema_capacity * 5
print(f"{income:.2f} leva")
