# STRING

summary: str = "Hello " + "World"
print(summary)
summary += "!!!!!!!!"
print(summary)


multiple = "Multiple " * 5
print(multiple)
multiple *= 2
print(multiple)

summary: str = summary.replace("Hello", "Goodbye")
print(summary)


print(summary.islower())
print(summary.isupper())


upper_s = summary.upper()
print(upper_s)
print(upper_s.isupper())
lower_s = summary.lower()
print(lower_s)
print(lower_s.islower())

capitalized = lower_s.capitalize()
print(capitalized)
