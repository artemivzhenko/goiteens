#Створити список материків західної півкулі.
# Користувач 5 разів вводить новий материк, треба доповнити список материками із вводу користувачем.
# Відсортувати материки за алфавітом і вивести на екран

#games_list = ["Minecraft", "Dota", "Deadlock", "Counter Strike"]

#for i in range(5):
    #new_game = input(f"Нова гра в список{i+1}: ")
    #games_list.append(new_game)

#games_list.sort()
#print(games_list)

#Створити список, елементами якого є інші списки, що містять інформацію про ім’я та прізвище студентів.
# Порахувати скільки людей мають ім’я «Андрій». Вивести на екран всі імена у форматі
#№Списку №Учня, Імʼя учня

names = [
    ["Artem", "Ivan", "Petro"],
    ["Andriy", "Arina", "Pavel"],
    ["Alex", "Andriy", "Viktor"],
    ["Andriy", "Ivan", "Petro"],
]

andriy_count = 0

for list_index, inside_list in enumerate(names):
    for item_index,item in enumerate(inside_list) :
        print(f"Список {list_index}, номер імені {item_index}, ім'я {item}")
        if item == "Andriy":
            andriy_count += 1
print(f"Кількість імен Андрій {andriy_count}")

