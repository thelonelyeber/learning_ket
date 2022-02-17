com = input('Что вы хотите найти (площать/периметр): ').lower()

a = float(input('Введите первую сторону: '))
b = float(input('Введите вторую сторону: '))
c = float(input('Введите третью сторону: '))

if com == 'площадь':
    square = a * b * c
    print(f'Площадь данного треугольника будет равна {square}')
elif com == 'периметр':
    perimeter = a + b + c
    print(f'Периметр данного треугольника будет равен {perimeter}')
else:
    print('Я вас не понимаю')
