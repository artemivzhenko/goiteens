students = [
    ["Alice", [85, 90, 88]],
    ["Bob", [78, 81, 85]],
    ["Charlie", [92, 87, 85]],
    ["Diana", [89, 92, 94]],
    ["Edward", [76, 80, 79]]
]

def add_grade():
    name = input("Введите имя студента для добавления оценки: ")
    grade = int(input("Введите новую оценку: "))
    available_students = [student[0] for student in students]
    if name not in available_students:
        print(f"Студент с именем {name} не найден. Доступные студенты: {', '.join(available_students)}")
        return
    for student in students:
        if student[0] == name:
            student[1].append(grade)
            print(f"Оценка {grade} добавлена для студента {name}.")
            return

def find_average():
    name = input("Введите имя студента для нахождения средней оценки: ")
    available_students = [student[0] for student in students]
    if name not in available_students:
        print(f"Студент с именем {name} не найден. Доступные студенты: {', '.join(available_students)}")
        return
    for student in students:
        if student[0] == name:
            grades = student[1]
            average = sum(grades) / len(grades)
            print(f"Средняя оценка студента {name}: {average:.2f}")
            return

def list_above_threshold():
    threshold = float(input("Введите пороговое значение средней оценки: "))
    print("Список студентов с средней оценкой выше порогового значения:")
    for student in students:
        grades = student[1]
        average = sum(grades) / len(grades)
        if average > threshold:
            print(f"{student[0]} - Средняя оценка: {average:.2f}")

def remove_grade():
    name = input("Введите имя студента для удаления оценки: ")
    index = int(input("Введите индекс оценки для удаления: "))
    available_students = [student[0] for student in students]
    if name not in available_students:
        print(f"Студент с именем {name} не найден. Доступные студенты: {', '.join(available_students)}")
        return
    for student in students:
        if student[0] == name:
            if 0 <= index < len(student[1]):
                removed_grade = student[1].pop(index)
                print(f"Оценка {removed_grade} удалена для студента {name}.")
                return
            else:
                print("Неправильный индекс.")
                return

def menu():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить оценку")
        print("2. Найти среднюю оценку")
        print("3. Вывести список студентов с средней оценкой выше порогового значения")
        print("4. Удалить оценку")
        print("5. Выход")

        choice = input("Введите номер действия: ")
        if choice == '1':
            add_grade()
        elif choice == '2':
            find_average()
        elif choice == '3':
            list_above_threshold()
        elif choice == '4':
            remove_grade()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Пожалуйста, попробуйте снова.")

menu()
