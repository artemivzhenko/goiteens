number_list= ["неділя","понеділок", "вівторок", "середа", "четвер","п'ятниця", "субота"]
for number in range(5):
    num= input("введіть число")
    num_int= int(num)
    print(number_list[num_int -1])