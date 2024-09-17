favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Fight Club"]

while True:
    print("\nМеню:")
    print("1. Удалить фильм из списка")
    print("2. Добавить фильм в список")
    print("3. Вставить фильм на указанную позицию")
    print("4. Найти индекс фильма")
    print("5. Подсчитать количество вхождений фильма")
    print("6. Отсортировать список")
    print("7. Развернуть копию списка")
    print("8. Показать оригинальный и развёрнутый списки")
    print("9. Выйти")

    choice = input("Выберите действие (1-9): ")

    if choice == "1":
        movie_to_remove = input("Введите название фильма, который нужно удалить: ")
        if movie_to_remove in favorite_movies:
            favorite_movies.remove(movie_to_remove)
            print(f"Фильм '{movie_to_remove}' удалён из списка.")
        else:
            print(f"Фильма '{movie_to_remove}' нет в списке.")

    elif choice == "2":
        movie_to_add = input("Введите название фильма, который хотите добавить в список: ")
        favorite_movies.append(movie_to_add)
        print(f"Фильм '{movie_to_add}' добавлен в список.")

    elif choice == "3":
        movie_to_insert = input("Введите название фильма для вставки: ")
        position_to_insert = int(input("Введите номер позиции для вставки (0 - первая позиция): "))
        favorite_movies.insert(position_to_insert, movie_to_insert)
        print(f"Фильм '{movie_to_insert}' вставлен на позицию {position_to_insert}.")

    elif choice == "4":
        movie_to_find = input("Введите название фильма для поиска индекса: ")
        if movie_to_find in favorite_movies:
            movie_index = favorite_movies.index(movie_to_find)
            print(f"Индекс первого вхождения фильма '{movie_to_find}' в списке: {movie_index}.")
        else:
            print(f"Фильма '{movie_to_find}' нет в списке.")

    elif choice == "5":
        movie_to_count = input("Введите название фильма для подсчёта: ")
        count_of_movie = favorite_movies.count(movie_to_count)
        print(f"Фильм '{movie_to_count}' появляется в списке {count_of_movie} раз(а).")

    elif choice == "6":
        favorite_movies.sort()
        print("Список после сортировки:", favorite_movies)

    elif choice == "7":
        sorted_favorite_movies = favorite_movies.copy()
        sorted_favorite_movies.reverse()
        print("Копия списка после разворота:", sorted_favorite_movies)

    elif choice == "8":
        print("Оригинальный отсортированный список:", favorite_movies)
        print("Развёрнутая копия списка:", sorted_favorite_movies)

    elif choice == "9":
        print("Выход из программы.")
        break

    else:
        print("Некорректный выбор. Пожалуйста, выберите действие от 1 до 9.")
