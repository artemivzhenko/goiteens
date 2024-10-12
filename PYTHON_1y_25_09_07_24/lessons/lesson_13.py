my_string = "Hello, world!"

# # region Basic string functions
# print(my_string.lower() + " -> ",
#       "lower() метод lower() повертає копію рядка з усіма символами, перетвореними на малі літери.")
#
# print(my_string.upper() + " -> ",
#       "метод upper() повертає копію рядка з усіма символами, перетвореними на верхній регістр (великі літери).")
#
# my_string = "Hello, world!  Hello, world".lower()
#
# print(my_string.capitalize() + "  -> ",
#       "capitalize() — метод capitalize() повертає копію рядка з першим символом у верхньому регістрі, а решта — у нижньому регістрі.")
#
# print(my_string.title() + " -> ",
#       "метод title() повертає копію рядка, у якому перша літера кожного слова перетворюється у верхній регістр, а решта літер — у нижній.")
#
# print(my_string.swapcase() + " -> ",
#       "метод swapcase() повертає копію рядка з символами верхнього регістру, перетвореними на малі та навпаки.")
#
# # endregion
#
# # region other methods
# index = int((len(my_string)-1)/2)
#
#
# print(my_string.find("world"),
#       "Метод find() шукає перше входження заданого підрядка sub і повертає його індекс. Якщо заданий підрядок не знайдено, то повертається -1.")
#
#
# print(my_string.rfind("world"),
#       "Метод rfind() шукає останнє входження заданого підрядка sub і повертає його індекс. Якщо заданий підрядок не знайдено, то повертається -1.")
#
# my_string_for_split = "Hello, world!Hello, world!Hello, world!Hello, world!Hello, world!Hello, world!Hello, world!Hello, world!Hello, world!"
#
# my_split_list = my_string_for_split.split("!")
#
# print(my_split_list)
#
# print("=====".join(my_split_list))
#
# my_replace_string = my_string.replace("hello", "goodbye")
# print(my_replace_string)
#
#
# my_map = {
#     ord("щ"): "d",
#     ord("ш"): "q"
# }
#
# translate_string = "щщщщщшшшщщщ".translate(my_map)
# print(translate_string)
#
# my_f_example_string = f"{my_replace_string} + it is my_f_example_string"
#
# print(my_f_example_string)
#
# my_name = "Artem"
#
# my_position_format = "Мене звати %s. Мені %s років" % (my_name, 30)
#
# my_position_format_2 = "Мене звати {0}. Мені {1} років"
#
# my_position_format_2 = my_position_format_2.format(my_name, 30)
#
# print(my_position_format_2)
#
# print(my_string.strip("hello"))
# # endregion
#

float_value = 89.66431

print("value {:0.3}".format(float_value))

round_float_value = round(float_value, 3)
print(f"round value {round_float_value}")

print('"{}" "{:+}" "{:-}" "{: }"'.format(1, 2, -3, 4))

# Створіть програму, яка перевіряє чи рядок включає в собі лише цифри.

# Створіть програму, яка приймає рядок, та повертає рядок, з якого було видалено всі пробіли.



my_string = "sfvds444"


