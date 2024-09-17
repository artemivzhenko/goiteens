word= "Цивілізація"
sum=0
for item in word:
    if item == "і":
       sum=sum + len(item)

print("Слово цивілізація містить",sum,"літери","і")