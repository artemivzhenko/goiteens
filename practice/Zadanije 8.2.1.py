artifacts = ["Компас", "Пружина", "Слизь", "Колобок", "Грави"]

for i in range(5):
    new_artifact = input(f"Введите название нового артефакта ({i+1}/5): ")
    artifacts.append(new_artifact)

artifacts.sort()

print("Отсортированный список артефактов:")
for artifact in artifacts:
    print(artifact)