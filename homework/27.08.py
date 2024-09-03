while True:
    name = input("Enter name: ")
    if name.strip():
        print(f"Hello, {name}!")
        break
    else:
        print("The name cannot be empty. Try again.")




start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

total_sum = sum(range(start, end + 1))

print(f"The sum of all numbers from {start} to {end} is equal to {total_sum}.")





number = int(input("Enter a number for the multiplication table: "))
multiplication_table = [number * i for i in range(1, 11)]
print(" ".join(map(str, multiplication_table)))





for i in range(-10, 0):
    print(i)





a = 1

while a <= 15:
    print(a)
    a += 1





lst = ["Dima", "Yaroslav", "Zhenya", "Sasha", "Andrii", "Max"]
for name in lst:
    print(f"Hello {name}!")





word = "Цивілізація"
count = 0
for letter in word:
    if letter == "і":
        count += 1

print(f'The number of letters "i" in the word "{word}": {count}')




word = input("Enter the word: ")
letter_to_find = input("Enter a letter to search: ")
count = 0
for letter in word:
    if letter == letter_to_find:
        count += 1

print(f'Number of letters "{letter_to_find}" in the word "{word}": {count}')






for number in range(1, 11):
    print(number)
    if number == 5:
        print("Number 5 found!")
        break
else:
    print("Number 5 not foundо.")

print("Finished")






n = int(input("Enter number: "))
for i in range(1, n + 1):
    print(f"The cube of the number {i} is equal to {i**3}")





price_per_kg = float(input("Enter the price for 1 kg of candy: "))
print("Quantity (kg) | Cost (UAH)")
print("---------------------------")
for kg in range(1, 11):
    total_price = price_per_kg * kg
    print(f"{kg:<15} | {total_price:.2f}")





price_per_kg = float(input("Enter the price for 1 kg of candy: "))
print("Quantity (kg) | Cost (UAH)")
print("---------------------------")
for kg in range(12, 21):
    weight = kg / 10.0
    total_price = price_per_kg * weight
    print(f"{weight:<15} | {total_price:.2f}")





for number in range(0, 101):
    if number % 2 == 0:
        print(number)





start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
for number in range(start, end + 1):
    if number % 2 != 0:
        print(number)








print(0)
n = int(input("Enter a number to calculate the factorial: "))
if n < 0:
    print("The factorial for negative numbers is not defined.")
else:
    factorial = 1
    current = n
    while current > 1:
        factorial *= current
        current -= 1
    print(f"The factorial of the number {n} is equal to {factorial}")





a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
c = int(input("Enter a number c: "))
if c == 0:
    print("The number c cannot be zero.")
else:
    count = 0
    if a > b:
        a, b = b, a
    for number in range(a, b + 1):
        if number % c == 0:
            count += 1
    print(f"The number of numbers between {a} and {b} that are divisible by {c}: {count}")









