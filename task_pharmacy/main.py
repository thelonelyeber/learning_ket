from class_pharmacy import Pharmacy

# flag = True
# while flag:
#     command = input('Введите что вы хотите сделать: ').lower()
#     if command == 'help':
#         print('Все комманды:\n'
#               'help - вывод всех команд\n'
#               'addphar - добаить в список свою аптеку\n'
#               'addpill - добавить лекарство в аптеку\n'
#               'info - вывести информацию аптеки\n'
#               'highprice - вывести самое дорогое лекарство \n'
#               'allprice - вывести все цены на лекарства \n')
#     elif command == 'addphar':
#         pass
#     elif command == "addpill":
#         pass
#     elif command == "info":
#         pass
#     elif command == "highprice":
#         pass
#     elif command == "allprice":
#         pass


"""Создание объектов класса в list()"""
"""Для редактирования попробовать сделать поиск названия аптеки и получить его номер в списке
в следствие чего использовать его для добавления измененного объекта и удаления старого"""

while True:
    all_phar = []
    command = input('Введите команду: ')
    if command == "create":
        name = input("Введите название аптеки: ")
        phar = Pharmacy(name)
        print(phar._name)
        all_phar.append(phar._name)
    elif command == "exit":
        print(all_phar)
        break
