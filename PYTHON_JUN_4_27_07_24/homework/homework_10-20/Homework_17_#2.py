
score = 0

def increase_score():
    global score
    score += 1
    print(f"Рахунок збільшено: {score}")

def decrease_score():
    global score
    score -= 1
    print(f"Рахунок зменшено: {score}")

def reset_score():
    global score
    score = 0
    print(f"Рахунок скинуто: {score}")


print("Початковий рахунок:", score)
increase_score()
increase_score()
decrease_score()
reset_score()
