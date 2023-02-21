x = {'Tanya': {'Algorithms': '380', 'Part One Interview': '220', 'C# Fundamentals': '250', 'JS Fundamentals': '400'},
     'Nikola': {'C# Fundamentals': '200', 'Algorithms': '380'}}

for keyz in x:
    dict_sorted = sorted(x[keyz], key=x[keyz].get, reverse=True)
    print(dict_sorted)
    for r in dict_sorted:
        print(r, x[keyz][r])
