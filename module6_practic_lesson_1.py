class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        """Инициализация атрибутов: alive, fed, name"""
        self.name = name

    def eat(self, food):
        """Метод для поедания"""
        if isinstance(food, Plant) and food.edible:
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
        else:
            print(f'{self.name} не стал есть {self.fed}')
            self.alive = False


class Plant:
    """Инициализация атрибутов: edible, name"""
    edible = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    """Млекопитающее, наследует все поведение от Animal"""
    pass


class Predator(Animal):
    """Хищник, наследует все поведение от Animal"""
    pass


class Flower(Plant):
    """Цветок, съедобность по умолчанию False"""
    pass


class Fruit(Plant):
    """Фрукт, переопределяем атрибут edible"""
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
