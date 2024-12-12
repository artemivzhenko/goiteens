
people = {"Боб": 19, "Антонио": 65, "Грета": 47, "Фрэнклин": 73}
oldest_person = max(people, key=people.get)
print(f"Самый старший человек: {oldest_person}, возраст: {people[oldest_person]}")
