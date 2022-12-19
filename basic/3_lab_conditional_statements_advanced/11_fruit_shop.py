fruit = input()
day = input()
quantity = float(input())
price = "error"

if day == "Saturday" or day == "Sunday":
    banana = 2.70
    apple = 1.25
    orange = 0.90
    grapefruit = 1.60
    kiwi = 3
    pineapple = 5.60
    grapes = 4.20

    if fruit == "banana":
        price = banana*quantity
    elif fruit == "apple":
        price = apple*quantity
    elif fruit == "orange":
        price = orange*quantity
    elif fruit == "grapefruit":
        price = grapefruit*quantity
    elif fruit == "kiwi":
        price = kiwi*quantity
    elif fruit == "pineapple":
        price = pineapple*quantity
    elif fruit == "grapes":
        price = grapes*quantity

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    banana = 2.50
    apple = 1.20
    orange = 0.85
    grapefruit = 1.45
    kiwi = 2.70
    pineapple = 5.50
    grapes = 3.85

    if fruit == "banana":
        price = banana * quantity
    elif fruit == "apple":
        price = apple * quantity
    elif fruit == "orange":
        price = orange * quantity
    elif fruit == "grapefruit":
        price = grapefruit * quantity
    elif fruit == "kiwi":
        price = kiwi * quantity
    elif fruit == "pineapple":
        price = pineapple * quantity
    elif fruit == "grapes":
        price = grapes * quantity

if price != "error":
    print(f"{price:.2f}")
else:
    print(price)
