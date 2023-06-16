import os


def students_credits(*args):
    diyan_dict = {}

    total_score = 0
    for data in args:
        course, score, max_points, diyan_points = data.split('-')
        coefficient_multiplayer = int(diyan_points) / int(max_points)
        final_credits = int(score) * coefficient_multiplayer
        total_score += final_credits
        diyan_dict[course] = [round(final_credits, 1)]

    if total_score >= 240:
        statement = [f"Diyan gets a diploma with {total_score :.1f} credits."]
    else:
        statement = [f"Diyan needs {240 - total_score :.1f} credits more for a diploma."]

    final_list = sorted(diyan_dict.items(), key=lambda k: k[1], reverse=True)

    final_list_reformated = [f"{x[0]} - {x[1][0]}" for x in final_list]

    statement.extend(final_list_reformated)

    final_final_print = statement

    return os.linesep.join(final_final_print)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print()
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
print()
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
