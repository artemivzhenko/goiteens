def  calculate_statistics(numbers):
    if not numbers:
        return None, None, None
    average = sum(numbers) / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)

    return average, minimum, maximum


numbers = [2,5,1,8,3]
averega ,minimum, maximum = calculate_statistics(numbers)
print(f"Середнє значення: {averega}, Мінімальне значення: {minimum}, Максимальне значення: {maximum}")