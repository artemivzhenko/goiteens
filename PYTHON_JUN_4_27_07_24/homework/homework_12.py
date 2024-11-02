my_friends_number = {
    "Maks": "+380 67 788 4701",
    "Dominik": "+380 63 370 6183",
    "Maryan": "+1 586 665 7654"
}
films = {
    "Venom 1": "Рубен Флейшер 2018",
    "Venom 2": "Рубен Флейшер 2021",
    "Venom 3": "Рубен Флейшер 2024",
}
adres = {
    "Maks": "Lviv, Vernadskogo 28",
    "Dominik": "Kyiv, Boyarka 12 ",
    "Maryan": "Michengan, Detroit 15"
}


films_name = input("Введіть назву фільму:\n ")
friend_name = input("Введіть ім'я друга:\n ")
friend_adres = input("Введіть ім'я друга:\n ")


if films_name in films:
    print(f"{films_name}: {films[films_name]}")
else:
    print(f"Немає фільма {films_name} в списку")


if friend_name in my_friends_number:
    print(f"{friend_name}: {my_friends_number[friend_name]}")
else:
    print(f"Немає номера для {friend_name}")


if friend_adres in adres:
    print(f"{friend_adres}: {adres[friend_adres]}")
else:
    print(f"Немає номера для {friend_adres}")