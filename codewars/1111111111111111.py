def closing_in_sum(number):
    number_str = str(number)
    length = len(number_str)
    total_sum = 0

    for i in range(length // 2):
        pair = int(number_str[i] + number_str[-(i + 1)])
        total_sum += pair

    if length % 2 == 1:
        total_sum += int(number_str[length // 2])

    return total_sum

# Пасхалка