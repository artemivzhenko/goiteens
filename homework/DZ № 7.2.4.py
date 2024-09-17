def remove_even_elements(lst):
    return [x for x in lst if x % 2 != 0]

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
result = remove_even_elements(my_list)
print("Список после удаления парних елементов:", result)
