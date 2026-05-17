def multi_criteria_sort(students):
    students.sort(
        key=lambda student: (
            -student["grade"],
            -student["attendance"],
            student["name"]
        )
    )
    return students
students = [
    {"name": "Alice", "grade": 85, "attendance": 90},
    {"name": "Bob", "grade": 85, "attendance": 95},
    {"name": "Charlie", "grade": 90, "attendance": 80}
]

print(multi_criteria_sort(students))