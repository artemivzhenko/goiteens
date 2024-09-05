def sum_of_elements(lst):
    return sum(lst)

my_list = [1, 2, 3, 4, 5]
print(f"Sum of list elements: {sum_of_elements(my_list)}")






def product_of_elements(lst):
    product = 1
    for num in lst:
        product *= num
    return product

my_list = [1, 2, 3, 4, 5]
print(f"Product of list elements: {product_of_elements(my_list)}")






def is_list_empty(lst):
    return len(lst) == 0

my_list = []
if is_list_empty(my_list):
    print("The list is empty")
else:
    print("The list is not empty")


