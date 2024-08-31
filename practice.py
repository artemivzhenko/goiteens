# 1. Написати код який буде просити ім'я користувача до поки він його не напише

#
# user_name = "Artem"
# user_input = ""
# while user_name != user_input:
#     user_input = input("Put your name ->\n")
#     if user_name != user_input:
#         print("It is not your name")
#     else:
#         print("Yes, it is your name")
#
#
# while True:
#     user_input = input("Put your name ->\n")
#     user_name = "Artem"
#     if user_name == user_input:
#         break


# 7. Дано слово “Цивілізація”. За допомогою циклу порахувати скільки літер “і” містить в собі це слово.
# 8. Зробити попередню програму більш універсальною — Запитувати у користувача слово та літеру для пошуку.
# 9. Використати блок “else” щоб вивести повідомлення “Завершено” після успішного виходу з циклу (довільний)

#
# word = input("Put your word ->\n")
# my_liter = input("Put your liter ->\n")
# my_liter_count = 0
# for liter in word:
#     if liter == my_liter:
#         my_liter_count += 1
#         break
# else:
#     print("My loop end successful")
# print(my_liter_count)

def year_days(year):
    count_of_days = 365
    if year % 4 == 0:
        count_of_days = 366
    result = f"{year} has {count_of_days} days"
    return result


message = year_days(2000)
print(message)

