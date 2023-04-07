movie_name = input()
days = int(input())
tickets = int(input())
price = float(input())
money_for_theater = int(input())


total_sum = (days * tickets * price) * ((100 - money_for_theater)/100)
print(f"The profit from the movie {movie_name} is {total_sum:.2f} lv.")
