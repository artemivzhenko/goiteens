substring = "Suspendisse vitae euismod elit, eget faucibus est."
multiply_string = f"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit.{substring}
Donec interdum maximus lectus at laoreet.
\tInteger vulputate at justo nec fermentum.
Praesent dignissim lobortis ex ac sodales. 
Interdum et malesuada fames ac ante ipsum primis in faucibus. 
Vestibulum viverra justo diam, eget viverra ex volutpat ac. 
Suspendisse placerat tellus efficitur diam hendrerit, in suscipit tellus tempor. 
Nam in egestas sem.
""".in
print(multiply_string)

print(multiply_string)
print(str([12, 123]))
print(str(90))
print(str(True))

if substring in multiply_string:
    print("substring in multiply_string")

for letter in substring:
    print(letter, end="\t")

m_list = [1, 2, 3, 1]


def crap(*args, **kwargs):
    return args

crap([1, 23,5235 ,36,4 ,64,3,5,43,54],
     c=12, b=55, j=1234)


with open("test.txt", "w") as file:
    print(substring, substring, substring, substring, sep="-----------\n", file=file)


changed_substring = substring[0: 11]
changed_substring[0] += "L"
print(changed_substring)


# \n — переклад рядка
# \f — переклад сторінки
# \r — повернення каретки
# \t — горизонтальна табуляція
# \v — вертикальна табуляція

from collections import Counter

print(sorted("asfdsadf"))


def my_function(x: int) -> int:
    sum = x * 10
    return sum

#
#
#
# # Integer, Float, String, Boolean
#
# my_string = ["a","b","c","defg"]
#
# my_string.append("hklmnop")
#
# print(my_string)
#
#
#


























