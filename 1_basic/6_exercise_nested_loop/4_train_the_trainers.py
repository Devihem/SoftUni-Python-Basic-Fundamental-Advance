judges = int(input())
total_average_score = 0
total_score = 0
presentation_count = 0

loop_system = True
while loop_system:
    presentation_name = input()
    if presentation_name == "Finish":
        loop_system = False
        print(f"Student's final assessment is {total_average_score/presentation_count:.2f}.")
        break
    presentation_count += 1
    for score in range(1, judges+1):
        judge_score = float(input())
        total_score += judge_score
    average_score = total_score / judges
    print(f"{presentation_name} - {average_score:.2f}.")
    total_average_score += average_score
    average_score = 0
    total_score = 0
