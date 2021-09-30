class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Автомобиль: {self.name} (цвет машины {self.color}) '
              f'Полицейское авто - {self.is_police}')

    def go(self):
        print(f'{self.name}: Машина поехала!')

    def stop(self):
        print(f'{self.name}: Машина остановилась!')

    def turn(self, direction):
        print(f'{self.name}: Поворот {"направо" if direction == 0 else "налево"}.')

    def show_speed(self):
        return f'{self.name}: Скорость {self.speed}.'


class TownCar(Car):  # обычные городские авто
    def show_speed(self):
        return f'{self.name}: Скорость авто: {self.speed}' \
               f'Превышение скорости' \
            if self.speed > 60 else f'{self.name}: Скорость авто {self.speed}'


class WorkCar(Car):  # такси и доставка
    def show_speed(self):
        return f'{self.name}: Скорость авто: {self.speed} ' \
               f'Превышение скорости!' \
            if self.speed > 40 else f'{self.name}: Скорость авто {self.speed}'


class SportCar(Car):  # спорткары
    pass


class PoliceCar(Car):  # Полицейские авто
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police = PoliceCar("45-й экипаж", "бело-синий", 120)
police.go()
print(police.show_speed())
police.turn(0)
police.stop()
print()

taxi = WorkCar("Yandex", "желтое", 45)
taxi.go()
print(taxi.show_speed())
taxi.turn(0)
taxi.stop()
print()

ferrari = SportCar("Ferrari 360 Modena", "красный", 350)
ferrari.go()
print(ferrari.show_speed())
ferrari.turn(1)
ferrari.stop()
print()

my_auto = TownCar("Toyota Camry", "черный", 77)
my_auto.go()
print(my_auto.show_speed())
my_auto.turn(0)
my_auto.stop()
print()
