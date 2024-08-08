# BOOLEAN

first_boolean: bool = True
second_boolean: bool = False
third_boolean: bool = False


print("A and B =", first_boolean and second_boolean)                   # Logical AND
print("A or B =", first_boolean or second_boolean or third_boolean)    # Logical OR
print("Not A =", not second_boolean)                                   # Logical NOT

result = (first_boolean or second_boolean) and not (first_boolean and second_boolean)
print("Result of (A or B) and not (A and B) =", result)

a_int: int = int(first_boolean)
b_int: int = int(second_boolean)
print("Integer value of A:", a_int)
print("Integer value of B:", b_int)

is_greater: bool = 5 > 3
print("Is 5 greater than 3?", is_greater)

is_equal: bool = (3 + 4) == 7
print("Is 3 + 4 equal to 7?", is_equal)

a = not first_boolean
b = not second_boolean
print("New value of A (after negation):", a)
print("New value of B (after negation):", b)


practice_boolean: bool = 5 * 10 == 74
print(practice_boolean)
practice_boolean_2: bool = "Pavlo" != "Ivan"
print(practice_boolean_2)
practice_boolean_3: bool = "Andrii" == "Petro"
print(practice_boolean_3)
