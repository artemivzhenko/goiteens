
def subtract(x, y):
    return x - y

def enough():

    cap = int(input("Ведите количество мест в автобусе (без водителя): "))
    on = int(input("Ведите количество людей в автобусе (без водителя): "))
    wait = int(input("Ведите количество людей ожедающих автобуса: "))
    available_space = cap - on
    if available_space >= wait:
        print("на остановке осталось —————— 0 человек")
    else:
        print(f"{wait} - {available_space} = {subtract(wait, available_space)}" + " —————— осталось человек на остановке")

enough()