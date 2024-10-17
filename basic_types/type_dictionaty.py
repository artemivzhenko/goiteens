my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[4])

# Ключом словника може бути незмінювані типи даних (shting, boolean, integer, float)
my_dictionary = {
    "name": "Yura",
    "age": 14,
    "location": "Kyiv",
    "is_man": True,
}
print(my_dictionary["is_man"])
for key in my_dictionary.keys():
    print(f"key in dictionary {key}")

for value in my_dictionary.values():
    print(f"value in dictionary {value}")

for key, value in my_dictionary.items():
    print(f"key in dictionary {key}, value in dictionary {value}")

