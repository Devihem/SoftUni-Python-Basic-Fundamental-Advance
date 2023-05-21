def negative_numbers(numbers):
    neg_sum = 0
    for numb in numbers:
        if numb < 0:
            neg_sum += numb
    print(neg_sum)
    return neg_sum


def positive_numbers(numbers):
    pos_sum = 0
    for numb in numbers:
        if numb > 0:
            pos_sum += numb
    print(pos_sum)
    return pos_sum


all_numbers = [int(x) for x in input().split()]
negative_sum = negative_numbers(all_numbers)
positive_sum = positive_numbers(all_numbers)

if abs(negative_sum) > positive_sum:
    print(f"The negatives are stronger than the positives")
elif abs(negative_sum) < positive_sum:
    print(f"The positives are stronger than the negatives")