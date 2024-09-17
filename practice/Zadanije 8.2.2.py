students = [
    ["Александр", "Чехов"],
    ["Максим", "Крылов"],
    ["Вова", "Вист"],
    ["Сидорович", "Сидоренко"],
    ["Александр", "Дегтярев"]
]

count_andrey = sum(1 for student in students if student[0] == "Андрей")

print("Список студентов:")
for index, student in enumerate(students, start=1):
    print(f"Список {index}, Ученик {index}, Имя ученика {student[0]}")

print(f"\nКоличество студентов с именем «Андрей»: {count_andrey}")