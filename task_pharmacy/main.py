from class_pharmacy import Pharmacy

pharmacy_list = list()
while True:
    com = input('Введите команду: ')

    if com == 'create':
        name = input('Введите название добавляемой аптеки: ')
        phar = Pharmacy(name)
        pharmacy_list.append(phar)

    elif com == 'add pill':
        i = 1
        print('В какую аптеку вы хотите добавить лекарство (выберите номер)')
        for phar in pharmacy_list:
            print(f'{i}) {phar.data["name"]}')
            i += 1
        num = int(input('Я выбираю - ')) - 1
        print('Отлично! А теперь введите название препарата и его цену')
        name = input('Название: ')
        cost = input('Стоимость: ')
        pharmacy_list[num].add_pill(name, cost)

    elif com == 'full info':
        i = 1
        print('Выберите аптеку, чью полную информацию вы хотите посмотреть')
        for phar in pharmacy_list:
            print(f'{i}) {phar.data["name"]}')
            i += 1
        num = int(input('Я выбираю - ')) - 1
        pharmacy_list[num].full_info()

    elif com == 'total cost':
        i = 1
        print('Выберите аптеку, сумму стоимости лекарств которой вы хотите получить')
        for phar in pharmacy_list:
            print(f'{i}) {phar.data["name"]}')
            i += 1
        num = int(input('Я выбираю - ')) - 1
        pharmacy_list[num].total_cost()

    elif com == 'max cost':
        i = 1
        print('Выберите аптеку в которой вы хотите узнать максимальную цену лекартва')
        for phar in pharmacy_list:
            print(f'{i}) {phar.data["name"]}')
            i += 1
        num = int(input('Я выбираю - ')) - 1
        pharmacy_list[num].max_cost()

    elif com == 'help':
        print('Вот список команд:'
              '    create - Добавить в список аптеку'
              '    add pill - Добавить лекарство в аптеку'
              '    total cost - Узнать сумму стоимости всех лекарств'
              '    max cost - Узнать максимальну цену лекартсва в аптеке'
              '    full info - Получить полную информацию об аптеке')

    elif com == 'exit':
        break
