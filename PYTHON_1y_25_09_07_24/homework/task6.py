#Створіть змінну, яка містить ваше ім'я та змінну, яка містить ваше
# прізвище. Потім створіть змінну, що об'єднає ці значення у рядок,
# який буде включати обидва слова, розділені тире. Виведіть отриманий
# рядок у нижньому регістрі.

userName = str(input("Enter your name."))
userSecondName = str(input("Enter your second name."))
result = userName + " - " + userSecondName
print(result.upper())