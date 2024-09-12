class Store:
    def __init__(self):
        self.products = {}
        self.sold_products = []

    def show_products(self):
        if not self.products:
            print("Нет доступных товаров.")
        else:
            print("Доступные продукты:")
            for category, items in self.products.items():
                print(f"Категория '{category}':")
                for item in items:
    1                print(f" - {item}")

    def supply_products(self):
        category = input("Введите категорию товара: ")
        new_products = input("Введите названия новых товаров, разделенные запятыми: ").split(", ")
        if category in self.products:
            self.products[category].extend(new_products)
        else:
            self.products[category] = new_products
        print("Продукция в комплекте.")

    def sell_product(self):
        category = input("Введите категорию товара: ")
        product_name = input("Введите название товара, который будет продаваться: ")
        if category in self.products and product_name in self.products[category]:
            self.products[category].remove(product_name)
            self.sold_products.append(product_name)
            print(f"Продукт '{product_name}' продавать.")
        else:
            print(f"Продукт '{product_name}' не найдено в категории '{category}'.")

    def replace_sold_product(self):
        category = input("Введите категорию товара: ")
        new_product = input("Введите название нового товара: ")
        if category in self.products:
            self.products[category].append(new_product)
        else:
            self.products[category] = [new_product]
        print(f"Продукт '{new_product}'добавлено в категорию '{category}'.")

    def show_sold_products(self):
        if not self.sold_products:
            print("Сегодня не продается ни одной продукции.")
        else:
            print("Реализуемая продукция на сегодняшний день:")
            for product in self.sold_products:
                print(product)

    def show_sales_history(self):
        if not self.sold_products:
            print("Нет истории продаж.")
        else:
            print("История продаж (в обратном порядке):")
            for product in reversed(self.sold_products):
                print(product)

    def menu(self):
        while True:
            print("\nМеню:")
            print("1.Показать все доступные товары")
            print("2. Поставка новых продуктов")
            print("3. Продать товар")
            print("4. Замена проданного товара на новый")
            print("5. Покажите проданные товары уже сегодня")
            print("6. Показать историю продаж")
            print("7. Выход")

            choice = input("Выберите действие (1-7): ")

            if choice == "1":
                self.show_products()
            elif choice == "2":
                self.supply_products()
            elif choice == "3":
                self.sell_product()
            elif choice == "4":
                self.replace_sold_product()
            elif choice == "5":
                self.show_sold_products()
            elif choice == "6":
                self.show_sales_history()
            elif choice == "7":
                print("Выход из программы.")
                break
            else:
                print("Неправильный выбор. Пожалуйста, повторите попытку.")

store = Store()
store.menu()
