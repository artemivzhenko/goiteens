list1 = [-2, -4, -6, 2, 5]
list2 = [3, 4, 6, 7, 6, -4, 1, -6, 5, -7]

def calculate(num_list):
    positive_sum = sum(num for num in num_list if num > 0)
    negative_diff = sum(num for num in num_list if num < 0)
    return positive_sum, negative_diff

positive_sum1, negative_diff1 = calculate(list1)
print(f"Первый список: сумма положительных чисел = {positive_sum1}, разница отрицательных чисел = {negative_diff1}")

positive_sum2, negative_diff2 = calculate(list2)
print(f"Второй список: сумма положительных чисел = {positive_sum2}, разница отрицательных чисел = {negative_diff2}")


list3 = [positive_sum1 + positive_sum2, negative_diff1 + negative_diff2]
print(f"Третий список: сумма всех положительных чисел = {list3[0]}, разница отрицательных чисел = {list3[1]}")