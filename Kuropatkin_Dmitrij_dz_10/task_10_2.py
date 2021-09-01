from abc import ABC, abstractmethod

from typing import Any


class InterClothes(ABC):  # интерфейс
    @property
    @abstractmethod
    def tissue_required(self):
        pass

    @property
    @abstractmethod
    def measuring(self):  # общая размерность одежды
        pass

    @abstractmethod
    def _calc_tissue_required(self):
        pass


class Clothes(InterClothes):
    _clothes = []

    def __init__(self, name: str, measuring: Any):
        self.name = name
        self._measuring = measuring
        self._tissue_required = None

        self._clothes.append(self)

    def _calc_tissue_required(self):
        raise NotImplemented

    @property
    def tissue_required(self) -> float:  # расход ткани
        if not self._tissue_required:
            self._calc_tissue_required()

        return self._tissue_required

    @property
    def measuring(self) -> Any:  # узнать размер
        return self._measuring

    @measuring.setter
    def measuring(self, measuring: Any):  # установить новый размер
        self._measuring = measuring
        self._tissue_required = None

    @property
    def total_tissue_required(self):  # ткани на всю одежду
        return sum([item.tissue_required for item in self._clothes])


class Coat(Clothes):
    def _calc_tissue_required(self):
        self._tissue_required = round(self.measuring / 6.5 + 0.5, 2)

    @property
    def V(self) -> Any:
        return self.measuring

    @V.setter
    def V(self, size: Any):
        self.measuring = size

    def __str__(self):
        return f"Для пошива пальто {self.measuring} размера " \
               f"требуется {self.tissue_required} кв. метров ткани"


class Suit(Clothes):
    def _calc_tissue_required(self):
        self._tissue_required = round(2 * self.measuring * 0.01 + 0.3, 2)

    @property
    def H(self) -> Any:
        return self.measuring

    @H.setter
    def H(self, height: Any):
        self.measuring = height

    def __str__(self):
        return f"Для пошива костюма на рост {self.measuring} см. " \
               f"требуется {self.tissue_required} кв. метров ткани"


if __name__ == '__main__':
    coat = Coat('Пальто новое', 7)
    print(coat)
    coat.V = 8
    print(coat)

    suit = Suit('Костюм новый', 190)
    print(suit)
    suit.H = 195
    print(suit)

print(suit.total_tissue_required)
print(coat.total_tissue_required)




