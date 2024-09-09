from collections import Counter

def count_unique_elements(lst):
    element_counts = Counter(lst)
    unique_elements = [elem for elem, count in element_counts.items() if count == 1]
    return len(unique_elements)

lst = [1, 2, 3, 4, 2, 3, 5, 6, 7, 8, 8, 9, 10]
unique_count = count_unique_elements(lst)
print(f"Количество уникальных элементов: {unique_count}")

