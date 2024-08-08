record= input("введіть вираз:")
print(record)
record_list= record.split(",")
sym1= record_list[0]
num2= int(record_list[1])
num3= int(record_list[2])



if sym1 == "+":
    print(num2 + num3)
elif sym1 == "-":
    print(num2 - num3)
elif sym1 == "/":
    print(num2 / num3)
elif sym1 == "*":
    print(num2 * num3)