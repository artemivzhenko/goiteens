def gaslighting(s, y, f):
    return any(a != b and (a in f or b in f) for a, b in zip(s, y))