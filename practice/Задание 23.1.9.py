
student_scores = {}
while True:
    name = input("Введите имя ученика: ")
    scores = list(map(int, input("Введите оценки через пробел: ").split()))
    student_scores[name] = sum(scores) / len(scores)
    if input("Добавить ещё одного ученика? (да/нет): ").lower() != "да":
        break
print(student_scores)
