from typing import List


class Matrix:
    def __init__(self, matrix_data: List[List]):
        self.__matrix = matrix_data

        matrix_rows = len(self.__matrix)
        self.__matrix_size = frozenset([(matrix_rows, len(row)) for row in self.__matrix])

        if len(self.__matrix_size) != 1:
            raise ValueError("Неправильный размер Матрицы!")

    def __add__(self, other: "Matrix") -> "Matrix":
        if not isinstance(other, Matrix):
            raise TypeError(f"'{other.__class__.__name__}' "
                            f"Носовместимый тип объекта")
        if self.__matrix_size != other.__matrix_size:
            raise ValueError(f"Разница в размерах матриц!")

        result = []

        for item in zip(self.__matrix, other.__matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])

        return Matrix(result)

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])


if __name__ == '__main__':
    matrix_1 = Matrix([[1, 2], [3, 4]])
    print(matrix_1, '\n')

    matrix_2 = Matrix([[10, 20], [30, 40]])
    print(matrix_2, '\n')

    print(matrix_1 + matrix_2)
