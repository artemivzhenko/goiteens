elements = [1, 2, 2, 3, 4, 4, 5]

unique_elements = []
indices = []

for index, value in enumerate(elements):
    if value not in unique_elements:
        unique_elements.append(value)
        indices.append(index)

print(f"Уникальные элементы: {unique_elements}")
print(f"Индексы первых вхождений: {indices}")
