#Дано список чисел. Використовуйте map для піднесення кожного числа
# до квадрату та filter для відбору тільки тих чисел, що є парними.

my_list= [12,20,30,39,25]
squar= list(map(lambda x: x ** 2 ,my_list))
squar_2= list(filter(lambda x: x %2==0,squar))
print(squar_2)