def square_numbers(*args):
    return [num ** 2 for num in args]
print(square_numbers(1, 2, 3, 4))
print(square_numbers(5, 6))




score = 0
def increase_score():
    global score
    score += 1
def decrease_score():
    global score
    score -= 1
def reset_score():
    global score
    score = 0
increase_score()
print("Рахунок після збільшення:", score)
decrease_score()
print("Рахунок після зменшення:", score)
reset_score()
print("Рахунок після скидання:", score)


