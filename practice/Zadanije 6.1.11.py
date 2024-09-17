price_per_kg_1 = float(input("Введите цену за 1 кг конфет: "))

for i in range(1, 11):
    cost_1 = price_per_kg_1 * i
    print(f"Стоимость {i} кг конфет: {cost} у.е.")