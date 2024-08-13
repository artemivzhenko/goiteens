number_str = input("Введіть число в діапазоні 1-999: ")
length = len(number_str)
number = int(number_str)

par = "Парне" if number % 2 == 0 else "Непарне"

if length == 1:
    length_count = "однозначне"
elif length == 2:
    length_count = "двозначне"
else:
    length_count = "тризначне"

message = par + " " + length_count + " число"
print(message)