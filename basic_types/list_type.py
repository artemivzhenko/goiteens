my_first_list: list = ["Artem", 183475920, True, 0.2312312]
for item in my_first_list:
    print(item)

print("Artem" in my_first_list)

print("Ivan" in my_first_list)

str_value = "Artem"
list_value = ["A", "r", "my_turtle", "e", "m"]

for i in "Artem":
    print(i)

names = "Artem,Ivan|Vlad|Arina"
print(names)
names_list = names.split("|")
print(names_list)

my_number_list = [10, 29, 40, 50, 60, 23, 34, 35, 12, 43, 36, 99]
summaries = sum(my_number_list)
print(f"Sum of my number list {summaries}")

minimal = min(my_number_list)
print(f"Minimal number in my list {minimal}")

maximum = max(my_number_list)
print(f"Maximum number in my list {maximum}")

length = len(my_number_list)
print(f"Length of my mumber list {length}")

first_three = my_number_list[:3]  # Зріз з 0 по 2й елемент
print(first_three)

second_three = my_number_list[3:6]  # Зріз з 3 по 5й елемент
print(second_three)

reversed_list = my_number_list[::-1]  # Обернений список
print(reversed_list)

last_element = my_number_list[-1]
print(last_element)
