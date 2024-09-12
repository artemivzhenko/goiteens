products = ["Яблука", "Хліб", "Молоко", "Сир", "Картопля", "Яйця", "Куряче філе"]
[print(f"Мій магазин має товар {product}") for product in products]
products.append(input("Введіть товар для додавання->\n"))
products.remove(input("Введіть товар для видалення->\n"))
old_product = input("Введіть товар для заміни->\n")
products.insert(products.index(old_product), input("Введіть новий товар для заміни->\n"))
products.remove(old_product)
[print(f"Історія продуктів {product}") for product in products[::-1]]