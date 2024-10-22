def fix_code(isbn):
    for i in range(10):
        temp_isbn = isbn.replace('?', str(i))
        total = sum((10 - j) * (10 if char == 'X' else int(char)) for j, char in enumerate(temp_isbn))
        if total % 11 == 0:
            return str(i)

    temp_isbn = isbn.replace('?', 'X')
    total = sum((10 - j) * (10 if char == 'X' else int(char)) for j, char in enumerate(temp_isbn))
    if total % 11 == 0:
        return 'X'