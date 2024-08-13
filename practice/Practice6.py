#Завершіть функцію, яка повертає день тижня відповідно до вхідного номера:
#1 повертає “Неділя”
#2 повертає “Понеділок”
#3 повертає “Вівторок”
#4 повертає “Середа”
#5 повертає “П’ятниця”
#6 повертає “Субота”
#7 повертає  "Неділя"
#Інакше повертає “Неправильно, будь ласка, введіть число від 1 до 7”.

my_first_list: list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for number in range(7):
    user_number =  input("Enter your number")
    user_number_int=int(user_number)
    print(my_first_list[user_number_int-1])

