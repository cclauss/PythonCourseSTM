# Задание 2
def print_max_of_2(a: int, b: int):
    print(a if a > b else b)


def get_max_of_2(a: int, b: int) -> int:
    return a if a > b else b


print(get_max_of_2(1, 12))
print_max_of_2(21, 34)
