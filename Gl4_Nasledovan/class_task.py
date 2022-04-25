class Transport:
    def __init__(self, power, cost, number, brand):
        self.power = power  # Мощность
        self.cost = cost  # Стоимость
        self.number = number  # Номер
        self.brand = brand  # Марка


class Automobile(Transport):
    def __init__(self, power, cost, number, brand, mileage, tech_inspection):
        super().__init__(power, cost, number, brand)
        self.mileage = mileage  # Пробег
        self.tech_inspection = tech_inspection  # Пройден ли техосмотр

    def __repr__(self):
        return f'Номер: {self.number}; Мощность: {self.power}; Стоимость: {self.cost}; Марка: {self.brand}; ' \
               f'Пробег: {self.mileage}; Прохождение техосмотра: {self.tech_inspection} '


class Aircraft(Transport):
    def __init__(self, power, cost, number, brand, max_flight_altitude):
        super().__init__(power, cost, number, brand)
        self.max_flight_altitude = max_flight_altitude  # Максимальная высота полета

    def __repr__(self):
        return


cars_list = list()
airplanes_list = list()

while True:
    com = input('Введите комманду: ')
    if com == '1':  # Создание машины
        power = input('Введите мощность: ')
        cost = input('Введите стоимость: ')
        number = input('Введите номер: ')
        brand = input('Введите марку: ')
        mileage = input('Введите пробег: ')
        tech_inspection = input('Пройден ли техосмотр (y/n): ')
        if tech_inspection == 'y':
            tech_inspection = True
        elif tech_inspection == 'n':
            tech_inspection = False
        else:
            print('Используйте англ раскладку и введите "y" для подтверждения или "n" в ином случае!')
        auto = Automobile(power, cost, number, brand, mileage, tech_inspection)
        cars_list.append(auto)
    elif com == '2':  # Вывод полной информации обо всех машинах и самолетах
        count = 1
        print('Машины:')
        for car in cars_list:
            print(f'{count}) {car}')
            count += 1
        count = 1
        print('Самолеты:')
        for airplane in airplanes_list:
            print(f'{count}) {airplane}')
            count += 1
    elif com == '3':  # Создание самолета
        pass
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
