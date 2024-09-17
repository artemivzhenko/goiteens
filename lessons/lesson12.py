product=["гречка","рис","картопля","буряк","морква","яблуко","цибуля"]
print(f"Мій товар{product}")
user_input= input("Введіть назву нового товару:")
new_product=[user_input]
product.extend(new_product)
print(f"Мій товар{product}")
user_input_2= input("Введіть товар який ви хочете купити:")
product.remove(user_input_2)
print(f"Мій товар{product}")
user_input_3=input("Введіть товар який ви хочете замінити новий:")
user_input_4= input("Введіть товар на який ви хочете замінити замість старого:")
product.insert(product.index(user_input_3),user_input_4)
product.remove(user_input_3)
print(f"Історія продажів{product[::-1]}")



