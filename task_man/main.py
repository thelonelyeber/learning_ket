import class_man

infinity = True
man = class_man.Man()

while infinity:
    user_command = input("Введите комманду: ").lower()
    if user_command == "exit":
        infinity = False
    elif user_command == "help":
        print(f'Список комманд:\n'
              '---\n'
              'create man : создает человека\n'
              'kill man : вы убьете вашего человека\n'
              'talk : человека скажет что-нибудь\n'
              'go : отправляет человека гулять\n'
              'is alife: возвращает значение жизни человека (True - жив/ False - мертв)'
              '---')
    elif user_command == 'create man':
        name = input('Введите имя: ')
        man.create_man(name)
    elif user_command == 'kill man':
        man.kill()
    elif user_command == 'talk':
        man.talk()
    elif user_command == 'go':
        man.go()
    elif user_command == 'is alife':
        is_alife = man.is_alife
        print(is_alife)
    else:
        print("Ваша команда не определена, пожалуйста повторите снова\n"
              "Для вывода списка команд введите команду 'help'\n"
              "Для завершения программы введиет команду 'exit'")
