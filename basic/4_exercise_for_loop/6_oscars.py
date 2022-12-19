name = input()
academy_points = float(input())
number_judges_loops = int(input())

judge_end_sum = 0
total_score = 0

for i in range(0, number_judges_loops):
    name_of_judge = input()
    judge_points = float(input())
    judge_end_sum = judge_end_sum + (len(name_of_judge) * judge_points)/2
    total_score = academy_points + judge_end_sum
    if total_score > 1250.5:
        break

if total_score > 1250.5:
    print(f"Congratulations, {name} got a nominee for leading role with {total_score:.1f}!")
elif total_score < 1250.5:
    print(f"Sorry, {name} you need {1250.5 - total_score:.1f} more!")
