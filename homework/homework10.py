favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Fight Club"]
print(f"Всі фільми які є в списку:{favorite_movies}")
user_inp_1=input("Введіть назви фільму який потрібно видалити:")
favorite_movies.remove(user_inp_1)
user_inp_2= input("Введіть назву фільму який ви хочете додати:")
favorite_movies.append(user_inp_2)
print(f"Всі фільми які є в списку:{favorite_movies}")
user_inp_3= int(input("Введіть число позиції куди ви хочете додати фільм:"))
user_inp_4= input(f"Введіть фільм який ви хочете додати на позицію {user_inp_3}:")
favorite_movies.insert(user_inp_3,user_inp_4)
user_inp_5=input("Введіть назву фільму в якого ви хочете дізнатися індекс:")
print(favorite_movies.index(user_inp_5))
user_inp_6= input("Введіть назву фільму в якогови хочете перевірити скільки разів він з'являвся у списку:")
user_6= 0
for item in favorite_movies:
    if item == user_inp_6:
        user_6 += 1
print(user_6)
favorite_movies.sort()
sorted_movies = favorite_movies.copy()
print(favorite_movies)
print(sorted_movies)




