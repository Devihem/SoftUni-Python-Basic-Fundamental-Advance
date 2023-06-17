import os


def gather_credits(maximum_points_needed, *args):
    points_current = 0
    courses_dict = {}

    for course, points in args:

        if points_current >= maximum_points_needed:
            break

        if course not in courses_dict.keys():
            points_current += points
            courses_dict[course] = [points]

        if points_current >= maximum_points_needed:
            break

    final_print = []

    if points_current >= maximum_points_needed:
        final_print.append(f"Enrollment finished! Maximum credits: {points_current}.")
        final_print.append(f"Courses: {', '.join([key for key in sorted(courses_dict.keys(),key=lambda k: k[0])])}")

    else:
        final_print.append(
            f"You need to enroll in more courses! You have to gather {maximum_points_needed - points_current} credits more.")

    return os.linesep.join(final_print)

print(gather_credits(
    80,
    ("",0),
))

print()
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print()
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))