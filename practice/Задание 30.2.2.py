import itertools

def password_generator(length):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for combination in itertools.product(chars, repeat=length):
        yield ''.join(combination)

length = 4
gen = password_generator(length)
for password in gen:
    print(password)
