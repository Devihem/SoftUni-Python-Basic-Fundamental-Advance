cast_name = input()
score = float(input())
judges = int(input())
current_score = score
for i in range(0, judges):
    judge_name = input()
    judge_score = float(input())
    current_score += ((judge_score * len(judge_name))/2)
    if current_score > 1250.5:
        print(f"Congratulations, {cast_name} got a nominee for leading role with {current_score:.1f}!")
        break
else:
    print(f"Sorry, {cast_name} you need {1250.5 - current_score:.1f} more!")
