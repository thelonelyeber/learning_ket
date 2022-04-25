from class_task import Automobile, Aircraft

cars_list = list()
airplanes_list = list()

while True:
    com = input('Введите комманду: ')
    if com == '1':  # Добавление машины
        power = input('Введите мощность: ')
        cost = input('Введите стоимость: ')
        number = input('Введите номер: ')
        brand = input('Введите марку: ')
        mileage = input('Введите пробег: ')
        tech_inspection = input('Пройден ли техосмотр (y/n): ')
        while True:
            if tech_inspection == 'y':
                tech_inspection = True
                break
            elif tech_inspection == 'n':
                tech_inspection = False
                break
            elif tech_inspection == '*':
                tech_inspection = None
                break
            else:
                print('Используйте англ раскладку и введите "y" для подтверждения или "n" в ином случае!\n'
                      'Если вы не знаете или не хотите указывать то введите "*"')
                tech_inspection = input('Пройден ли техосмотр (y/n): ')
        auto = Automobile(power, cost, number, brand, mileage, tech_inspection)
        cars_list.append(auto)
    elif com == '2':  # Вывод полной информации обо всех машинах и самолетах
        count = 1
        if len(cars_list) > 0:
            print('Машины:')
            for car in cars_list:
                print(f'{count}) {car}')
                count += 1
        count = 1
        if len(airplanes_list) > 0:
            print('Самолеты:')
            for airplane in airplanes_list:
                print(f'{count}) {airplane}')
                count += 1
        if len(airplanes_list) == 0 and len(cars_list) == 0:
            print('Вы не ввели никаких данных о машинах и самолетах')
    elif com == '3':  # Добавление самолета
        power = input('Введите мощность: ')
        cost = input('Введите стоимость: ')
        number = input('Введите номер: ')
        brand = input('Введите марку: ')
        max_flight_altitude = input('Введите максимальную высоту полета: ')
        air = Aircraft(power, cost, number, brand, max_flight_altitude)
        airplanes_list.append(air)
    elif com == '4':  # Проверить, прошел ли владелец самой дорогой машины техосмотр
        pass
    elif com == '5':  # Подсчитать налог с регистрации всех машин
        pass
    elif com == '6':  # Подсчитать налог с регистрации всез самолетов
        pass
    elif com == '7':  # Определить мощность, стоимость и марку самого дорогого самолета
        pass
    elif com == 'exit':
        break
