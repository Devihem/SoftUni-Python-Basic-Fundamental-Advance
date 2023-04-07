students_loop = int(input())

a_mark = 0
b_mark = 0
c_mark = 0
d_mark = 0
total_score = 0

for i in range(0, students_loop):
    score = float(input())
    total_score += score
    if 2 <= score < 3:
        d_mark += 1
    elif 3 <= score < 4:
        c_mark += 1
    elif 4 <= score < 5:
        b_mark += 1
    elif score >= 5:
        a_mark += 1

print(f"Top students: {(a_mark/students_loop)*100:.2f}%")
print(f"Between 4.00 and 4.99: {(b_mark/students_loop)*100:.2f}%")
print(f"Between 3.00 and 3.99: {(c_mark/students_loop)*100:.2f}%")
print(f"Fail: {(d_mark/students_loop)*100:.2f}%")
print(f"Average: {total_score/students_loop:.2f}")
