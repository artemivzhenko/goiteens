word= input("Введіть слово:")
word_1= input("Введіть літеру:")
sum=0
for item in word:
    if item == word_1:
       sum=sum + len(item)

print("Слово",word,"містить",sum,"літери",word_1)

#hw
# 10 задач з код ворса і доробити завдання в тг