myltiply = lambda x: x * 10

print(myltiply(45))


my_list = [23, 54, 78, 38, 91]
my_list_x2 = map(lambda x: x * 2, my_list)


my_list_x4 = [x * 2 for x in my_list_x2]
print(my_list_x4)
