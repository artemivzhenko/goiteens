def summing_list():
    list1 = [1, 2, 3, 6, 7, 8, 5, 33, 6, 7, 7, 9, 22, 60, 8]

    list_sum = 0

    for i in list1:
        list_sum += i

    print(list_sum)

def multi_list():
    list2 = [2,5,6]

    list_multi = 1

    for i in list2:
        list_multi=list_multi*i
    print(list_multi)

def space_list(list):
    if not list:
        print("Список порожній")
    else:
        print("Список не порожній")

list3 = []
space_list(list3)
