from collections import deque

foods = deque([int(x) for x in input().split(', ')])
stamina = deque([int(x) for x in input().split(', ')])

all_peaks = {
    80: 'Vihren',
    90: 'Kutelo',
    100: 'Banski Suhodol',
    60: 'Polezhan',
    70: 'Kamenitza'
}
conquered_peaks = []

for day in range(7):

    food = foods.pop()
    stam = stamina.popleft()
    total_sum = food + stam

    if total_sum >= list(all_peaks.keys())[0]:
        mountain_peak = all_peaks.pop(list(all_peaks.keys())[0])
        conquered_peaks.append(mountain_peak)
        if not all_peaks:
            print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
            break
        continue

    continue
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    [print(x) for x in conquered_peaks]

# Final prints:
#  if all list are INTs : {', '.join([str(x) for x in list_name])}
