start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

if start > end:
    print("Начало диапазона должно быть меньше или равно концу диапазона.")
else:
    total_sum = sum(range(start, end + 1))

    print(f"Сумма всех чисел в диапазоне от {start} до {end} равна {total_sum}.")
