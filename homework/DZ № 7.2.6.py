def elements_below_average(lst):
    average = sum(lst) / len(lst)
    return [x for x in lst if x < average]

numbers = [10, 20, 30, 40, 50]
below_average = elements_below_average(numbers)
print("Елементы, которые меньше от среднего значенния списка:", below_average)
