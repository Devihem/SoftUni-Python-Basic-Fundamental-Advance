movies = [[1901 , "A"],[1900 , "Z"],[1900 , "A"],[1900 , "B"],[12200 , "A"]]

result = sorted(movies, key=lambda k: (-k[0], k[1]))
result = [movie.details() for movie in result]
result = [] if not result else result
