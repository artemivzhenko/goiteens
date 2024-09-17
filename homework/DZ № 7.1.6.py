def unique_elements_with_indices(lst):
    seen = {}
    for index, element in enumerate(lst):
        if element not in seen:
            seen[element] = index
    return seen

my_list = ['apple', 'banana', 'apple', 'cherry', 'banana', 'date', 'cherry']

result = unique_elements_with_indices(my_list)

for element, index in result.items():
    print(f"Элемент: {element}, Первый индекс: {index}")
