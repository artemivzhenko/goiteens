price_per_kg = float(input("Введите цену за 1 кг конфет: "))

weight = 1.2
while weight <= 2.0:
    cost = price_per_kg * weight
    print(f"Стоимость {weight:.1f} кг конфет: {cost} у.е.")
    weight += 0.2