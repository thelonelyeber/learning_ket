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

    def red_brand(self):
        self.brand = str(input('Введите имя: '))

    def __repr__(self):
        return f'Номер: {self.number}; Мощность: {self.power}; Стоимость: {self.cost}; Марка: {self.brand}; ' \
               f'Пробег: {self.mileage}; Прохождение техосмотра: {self.tech_inspection} '


class Aircraft(Transport):
    def __init__(self, power, cost, number, brand, max_flight_altitude):
        super().__init__(power, cost, number, brand)
        self.max_flight_altitude = max_flight_altitude  # Максимальная высота полета


car_list = list()
i = 0

# auto = Automobile(520, 2500000, 7388, 'Marusya', 90, True)
# print(auto)
# car_list.append(auto)
#
# print(f'Марка машины - {car_list[0].brand}\n'
#       f'Стоимость - {car_list[0].cost}')
#
# car_list[0].red_name()
# print(car_list[0].brand)

while True:
    com = input('Введите комманду: ')
    if com == '1':
        power = input('Введите мощность машины: ')
        cost = input('Введите стоимость: ')
        number = input('Введите номер машины: ')
        brand = input('Введите марку машины: ')
        mileage = input('Введите пробег: ')
        tech_inspection = input('Пройден ли техосмотр (y/n): ')
        if tech_inspection == 'y':
            tech_inspection = True
        elif tech_inspection == 'n':
            tech_inspection = False
        else:
            print('Используйте англ раскладку и введите "y" для подтверждения или "n" в ином случае!')
        auto = Automobile(power, cost, number, brand, mileage, tech_inspection)
        car_list.append(auto)
        i += 1
    elif com == '2':  # Вывод всех машин
        count = 1
        for car in car_list:
            print(f'{count}) {car}')
            count += 1
    elif com == 'exit':
        break
