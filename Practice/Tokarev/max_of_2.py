def max_of_int(a, b):
    if a > b:
        print(f'Максимальное число из введенных a: {a}')
        return a
    else:
        print(f'Максимальное число из введенных b: {b}')
        return b


print(f'Максимальное число из введенных: {max_of_int(1, 7)}')
