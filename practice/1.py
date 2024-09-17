products = ["Хлеб", "Вода", "Чай"]
[print(f"Moj towar w magazine {product}") for product in products]
products.append(input("wwedite towar dla pribawlenija: "))
products.remove(input("wwedite towar dla udalenia: "))
old_product = input("wwedite towar dla zameny: ")
products.insert(products.index(old_product), input("wwedite nowyj towar dla zameny: "))
products.remove(old_product)
[print(f"istorija prod {product}")for product in products[::-1]]