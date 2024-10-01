shop_list = ["cheese", "meat", "butter", "bread", "carrot", "tomato", "apple"]

for product in shop_list:
    print(f"В магазині є  {product}")

new_product = input("\nЯкий товар ви хочете додати? ")
shop_list.append(new_product)

sell_product = input("\nЯкий товар ви хочете придбати? ")
if sell_product in shop_list:
    shop_list.remove(sell_product)

change_product = input("\nЯкий товар хочете замінити?")
product_index = shop_list.index(change_product)

changing_product = input("\nНа який товар хочете замінити?")
shop_list.insert(product_index,changing_product)

shop_list.remove(change_product)

for product in shop_list[::-1]:
    print(shop_list)