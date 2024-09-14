
continents = ["Північна Америка", "Південна Америка"]
for i in range(5):
    new_continent = input(f"Введіть назву нового материка ({i+1}/5): ")
    continents.append(new_continent)
continents.sort()
print("Відсортований список материків:")
for continent in continents:
    print(continent)








students = [
    ["Андрій", "Алексій"],
    ["Марія", "Алекян"],
    ["Олександр", "Шевчук"],
    ["Андрій", "Павлинський"],
    ["Ірина", "Владимір"],
    ["Андрій", "Наталья"]
]
andrii_count = 0
for list_index, student in enumerate(students, start=1):
    print(f"№list {list_index}, Name student: {student[0]}")
    if student[0] == "Андрій":
        andrii_count += 1
print(f"\nThe number of students with a name 'Андрій': {andrii_count}")



