num= input("введіть число від 1 до 999:")
num_lenght= len(num)
num_int= int(num)
num_p= "парне" if num_int % 2 == 0 else "не парне"

if num_lenght == 1:
    print("Однозначне " + num_p + " число")

if num_lenght == 2:
    print("Двохзначне " + num_p + " число")

if num_lenght == 3:
    print("Трьохзначне " + num_p + " число")

