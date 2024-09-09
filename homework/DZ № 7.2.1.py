def count_unique_elements(lst):
    unique_elements = set(lst)
    return len(unique_elements)

my_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
result = count_unique_elements(my_list)
print("Количество уникальних елементов:", result)
