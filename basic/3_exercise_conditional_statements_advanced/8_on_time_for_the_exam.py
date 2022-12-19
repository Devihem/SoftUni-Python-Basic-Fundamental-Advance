exam_hour = int(input())
exam_minuets = int(input())
arriving_hour = int(input())
arriving_minuets = int(input())

exam_total_mins = exam_minuets + exam_hour * 60
arriving_total_mins = arriving_minuets + arriving_hour * 60
status = "none"

if 0 <= exam_total_mins - arriving_total_mins <= 30:
    status = "On time"
elif exam_total_mins < arriving_total_mins:
    status = "Late"
else:
    status = "early"

diff = abs(exam_total_mins-arriving_total_mins)
hours_clock = diff // 60
minuets_clock = diff % 60

print(status)
if 0 < diff:
    if 0 < exam_total_mins - arriving_total_mins < 60:
        print(f"{diff} minutes before the start")
    elif 60 <= exam_total_mins - arriving_total_mins:
        print(f"{hours_clock}:{minuets_clock:02d} hours before the start")
    elif 1 <= arriving_total_mins-exam_total_mins < 60:
        print(f"{diff} minutes after the start")
    elif 60 <= arriving_total_mins-exam_total_mins:
        print(f"{hours_clock}:{minuets_clock:02d} hours after the start")
