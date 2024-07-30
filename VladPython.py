##Напишіть програму, яка просить користувача ввести
##спочатку улюбленого актора. Наступний запит - улюблений фільм, в якому знімався даний актор. Потім вивести
##на екран повідомлення у форматі:
##“This beautiful actor - … was filmed in this film … .” (Вписати актора та фільм)
user_like_actor = input("Введіть вашого улюбленого актора -->\n")
user_like_film = input("Введіть ваш улюблений фільм -->\n")

print("This beautiful actor " + user_like_actor + " was filmed in this film " + user_like_film)