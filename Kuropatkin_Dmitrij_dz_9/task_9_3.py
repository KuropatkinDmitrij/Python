class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_name(self):
        return f"{self.name} {self.surname}"

    def get_mooney(self):
        return f"{sum(self._income.values())} $"


driver = Position("Michael", "Schumacher", "Champion", 25466666452, 5564852)
print(driver.get_name())
print(driver.position)
print(driver.get_mooney())
