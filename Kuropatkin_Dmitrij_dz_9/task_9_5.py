class Stationery:
    def __init__(self, title="Поехали!"):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title} ")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title} ")


class Marker(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title} ")


tools = Stationery()
tools.draw()

pen = Pen('Синяя шариковая ручка')
pen.draw()

pencil = Pencil('Карандаш ХБ')
pencil.draw()

marker = Marker('Толстый маркер')
marker.draw()
