def separation(text: str, width: int, separator: str):
    a, lst = 0, list(text)
    for i in range(1, len(text)):
        if i % width == 0:
            if a == 0: lst.insert(i, separator)
            if a > 0: lst.insert(i + a, separator)
            a += 1
    return ''.join(lst)
