# Задание 1 
data: str = ''

print('Введите любые данные. Слово \"exit\" завершит программу.')

while data != 'exit':
    data = input('> ')
    print(f'Echo: {data}')
