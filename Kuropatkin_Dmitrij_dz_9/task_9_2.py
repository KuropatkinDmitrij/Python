class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass(self, weight=25, thickness=9):
        return f"{self._length} м. длина * " \
               f" {self._width} м. ширина * " \
               f" {weight} вес в кг * " \
               f" {thickness} толщина в см= " \
               f" {(self._length * self._width * weight * thickness) / 1000} тонн "


new_road = Road(15000, 100)
print(new_road.get_mass())
