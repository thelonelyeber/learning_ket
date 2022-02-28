from random import randint


class Man:
    def __init__(self):
        self.name_man = 'name'
        self.is_alife = True
        self.age = randint(15, 51)
        self.health = randint(10, 101)
        self.created = False

    def create_man(self, name):
        self.name_man = name
        self.created = True

    def talk(self):
        if self.created:
            if self.is_alife:
                random_talk = randint(1, 4)

                if self.health > 50:
                    health_replica = "Да я здоров как бык!"
                else:
                    health_replica = f"Со здоровьем у меня хреново, дожить бы до {self.age + 10}"

                replicas = {
                    1: f"Привет, меня зовут {self.name_man}, рад познакомиться!",
                    2: f"Мне {self.age}. А тебе?",
                    3: health_replica
                }
                print(replicas[random_talk])
            else:
                print(f'{self.name_man} очень занят в загромном мире и не может ответить вам...')
        else:
            print('Вы еще не создали человека')

    def go(self):
        if self.created:
            if self.is_alife:
                if self.health > 40:
                    print(f"{self.name_man} мирно прогуливается по городу :)")
                else:
                    print(f"{self.name_man} болен и не может гулять по городу :(")
            else:
                print(f"К сожалению, {self.name_man}, мертв, он не может идти гулять")
        else:
            print('Вы еще не создали человека')

    def is_alive(self):
        if self.created:
            return self.is_alife
        else:
            print('Вы еще не создали человека')

    def kill(self):
        if self.created:
            self.is_alife = False
            print(f"Вы убили {self.name_man}...")
        else:
            print('Вы еще не создали человека')
