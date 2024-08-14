num= int(input("Введіть число:"))

num_ver= "Число в діапазоні" if num > 10 else "Число поза діапазоном"
num_ver_2= num_ver if num < 20 else "Число поза діапазоном"
print(num_ver_2)
