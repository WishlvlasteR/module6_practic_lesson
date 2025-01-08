class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        """Инициализация фигуры."""
        self.__color = list(color)  # Сохраняем цвет фигуры
        if len(sides) == self.sides_count:
            self.__sides = list(sides)  # Если стороны заданы корректно, сохраняем их
        else:
            self.__sides = [1] * self.sides_count  # Если сторон недостаточно, заполняем единицами
        self.filled = False  # Параметр, определяющий заполнена ли фигура

    def get_color(self):
        """Возвращает цвет фигуры в формате RGB."""
        return self.__color

    def __is_valid_color(self, r, g, b):
        """Проверяет корректность цвета (в диапазоне от 0 до 255)."""
        return isinstance(r, int) and 0 <= r <= 255 and \
            isinstance(g, int) and 0 <= g <= 255 and \
            isinstance(b, int) and 0 <= b <= 255

    def set_color(self, r, g, b):
        """Устанавливает новый цвет, если он корректный."""
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        """Проверяет корректность сторон."""
        if len(new_sides) != self.sides_count:
            return False
        for side in new_sides:
            if not isinstance(side, (int, float)) or side <= 0:
                return False
        return True

    def get_sides(self):
        """Возвращает список сторон фигуры."""
        return self.__sides

    def __len__(self):
        """Возвращает периметр фигуры (сумма всех сторон)."""
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        """Устанавливает новые стороны, если они корректные."""
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        """Инициализация круга."""
        super().__init__(color, *sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        """Рассчитывает радиус круга по длине окружности."""
        circumference = self.get_sides()[0]  # Длина окружности — это единственная сторона
        return circumference / (2 * 3.14159)  # Используем приближенное значение pi

    def get_square(self):
        """Возвращает площадь круга."""
        return 3.14159 * (self.__radius ** 2)  # Площадь круга = π * r^2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        """Рассчитывает площадь треугольника по формуле Герона."""
        a, b, c = self.get_sides()
        s = sum(self.get_sides()) / 2  # Полупериметр
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Площадь по формуле Герона


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        """Инициализация куба."""
        if len(sides) == 1:
            sides = [sides[0]] * self.sides_count  # Если задана одна сторона, делаем все 12 одинаковыми
        super().__init__(color, *sides)

    def get_volume(self):
        """Возвращает объем куба (сторона в кубе)."""
        side = self.get_sides()[0]  # Сторона куба — это первая сторона
        return side ** 3  # Объем куба = сторона^3


# Проверочный код
if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, сторона окружности)
    cube1 = Cube((222, 35, 130), 6)  # (Цвет, сторона куба)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())

    cube1.set_color(300, 70, 15)  # Не изменится, так как значения некорректные
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится, так как это некорректно для куба
    print(cube1.get_sides())

    circle1.set_sides(15)  # Изменится, так как это корректно для круга
    print(circle1.get_sides())

    # Проверка периметра (для круга это длина окружности):
    print(len(circle1))

    # Проверка объема куба:
    print(cube1.get_volume())

    # Проверка площади круга:
    print(circle1.get_square())

    # Проверка площади треугольника:
    triangle = Triangle((100, 200, 150), 3, 4, 5)  # (Цвет, 3 стороны треугольника)
    print(triangle.get_square())
