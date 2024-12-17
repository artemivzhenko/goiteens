import math
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    sqrt_num = math.sqrt(num)
    log_num = math.log(num)
    exp_num = math.exp(num)
    print(f"Для числа {num}: Квадратний корінь = {sqrt_num}, Натуральний логарифм = {log_num}, Експонента = {exp_num}")


angles_degrees = [0, 30, 45, 60, 90]
for angle in angles_degrees:
    angle_radians = math.radians(angle)
    sin_angle = math.sin(angle_radians)
    cos_angle = math.cos(angle_radians)
    tan_angle = math.tan(angle_radians)
    print(f"Для кута {angle} градусів: Синус = {sin_angle}, Косинус = {cos_angle}, Тангенс = {tan_angle}")


angles_radians = [0, math.pi / 6, math.pi / 4, math.pi / 3, math.pi / 2]
for angle in angles_radians:
    asin_angle = math.degrees(math.asin(angle))
    acos_angle = math.degrees(math.acos(angle))
    atan_angle = math.degrees(math.atan(angle))
    print(f"Для кута {angle} радіан: Арксинус = {asin_angle}, Арккосинус = {acos_angle}, Арктангенс = {atan_angle}")
# З цими завданнями мені допомага сестра, це для того щоб потмі не було запитаннь як я це робив і
# заодно вона мені це трохи пояснила:)