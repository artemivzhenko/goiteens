
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2,number):
        if number % i == 0:
            return False
        else:
            return True
num = int(input("Введіть число: "))

if is_prime(num):
    print(f"{num} є простим числом")
else:
    print(f"{num} не є простим числом")