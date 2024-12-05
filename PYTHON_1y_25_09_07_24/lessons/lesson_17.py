# my_list = [1,2,3,4,5,6,7,8,9,10,11,1,2,3,4,5,6,7,8,9]
#
# print(my_list[2:17:3])
#
# print(my_list[:17])
#
# print(my_list[7:])
#
# print(my_list[:])
#
# print(my_list[::-1])
#
# print(my_list[::3])
#
# start = 7
# end = 18
# step = 2
#
# print(my_list[start:end:step])
#
#
# my_set = {12, 234, 345, 456, 45, 234, 124, 123, 4, 234, 21, 21, 21, 21, 234, 4}
# print(my_set)
# print(set(my_list))
#
# my_set.add(12344)
# print(my_set)
# my_set.remove(12344)
# print(my_set)
# my_set.discard(214312341234)
#
# my_letter_set = set("Hello World")
# print(my_letter_set)
# my_second_letter_set = set("Hi Wictor")
# print(my_second_letter_set)
# print(my_letter_set & my_second_letter_set)
# print(my_letter_set | my_second_letter_set)


my_list = [1, 2, 3, 4, 5]
my_dictionary = {
    "1": 1,
    "2": 2,
    "3": 3,
}
try:
    print(my_list[0])
    print(my_dictionary["bsdfjvb"])
except IndexError:
    print("We got IndexError Exception")
except KeyError:
    print("We got KeyError Exception")
except Exception as exc:
    print(f"Something went wrong error: {type(exc)} {exc}")
else:
    print("We didn't get exception")
finally:
    print("It is finally block")
