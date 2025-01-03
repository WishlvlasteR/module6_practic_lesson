class Animal:
    """Класс описания животных с атрибутами класса"""
    _DEGREE_OF_DANGER = 0
    live = True
    sound = None

    def __init__(self, speed):
        """Инициализация объекта класса Animal."""
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        """Перемещает животное с учетом скорости."""
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] = self._cords[0] + dx * self.speed
            self._cords[1] = self._cords[1] + dy * self.speed
            self._cords[2] = self._cords[2] + dz * self.speed

    def get_cords(self):
        """Выводит текущие координаты животного."""
        print(f'X:{self._cords[0]} Y:{self._cords[1]} Z:{self._cords[2]}')

    def attack(self):
        """Определяет поведение при атаке в зависимости от степени опасности."""
        if self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")
        else:
            print("Sorry, i'm peaceful :)")

    def speak(self):
        """Выводит звук животного."""
        print(self.sound)


class Bird(Animal):
    """Класс птиц наследуется от животных с дополнительным атрибутом"""
    beak = True

    def lay_eggs(self):
        """Откладывает яйца рендомно от 1 до 4."""
        from random import randint
        print(f'Here are(is) {randint(1, 4)} eggs for you')


class AquaticAnimal(Animal):
    """Класс Aqua с переопределением атрибута опасности, наследуется от животных"""
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        """Ныряет, изменяя координату z."""
        self._cords[2] = self._cords[2] - abs(dz) * (self.speed / 2)


class PoisonousAnimal(Animal):
    """Класс ядовитых животных с переопределением атрибута опасности, наследуется от животных"""
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    """Класс Утконос с переопределением звука, наследуется от птиц, ядовитых животных и животных"""
    sound = "Click-click-click"


db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
