count= 0
list_1=[
    ["Андрій","Олег"],
    ["Віктор","Андрій"],
    ["Іван","Петро"]
]
for list_index ,inside_list in enumerate(list_1):
    for item_index,item in enumerate(inside_list):
        print(f"список {list_index} ,номер ім'я{item_index} , імя {item}")
        if item == "Андрій":
            count += 1

print(f"Кількість імен Андрій: {count}")

