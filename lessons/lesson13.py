car_list=["bmw","mercedes","honda"]
user= input("Введіть п'ять марок автомобілей:")
for item in user:
    car_list.append(item)

car_list.sort()
print(car_list)