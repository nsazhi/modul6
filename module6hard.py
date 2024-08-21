from math import pi as pi


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = []
        self.__sides = []
        for i in color:
            if i in range(256):
                self.__color.append(i)
            else:
                self.__color = [0, 0, 0]
                break
        if len(sides) != self.sides_count:
            self.__sides += [1] * self.sides_count
        else:
            self.__sides.extend(sides)
        self.filled = True
        # print(self.__dict__)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, *rgb):
        __is_valid = True
        for i in rgb:
            if i not in range(256):
                __is_valid = False
                break
        return __is_valid

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *args):
        __is_valid = False
        if len(args) == self.sides_count:
            for i in args:
                if isinstance(i, int) and i > 0:
                    __is_valid = True
        return __is_valid

    def set_sides(self, *new_sides):
        if isinstance(self, Cube):
            if len(new_sides) == 1:
                new_sides = new_sides * self.sides_count
        if self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1
    __radius = None

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        __radius = super().__len__() / (2 * pi)
        return round(__radius ** 2 * pi, 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        sides = super().get_sides()
        p = sum(sides) / 2
        s = (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5
        return round(s, 2)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self._Figure__sides = list(sides) * self.sides_count

    def get_volume(self):
        return super().get_sides()[0] ** 3


# # ПРОВЕРКА КРУГА
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
circle2 = Circle((200, 200, 300), 10, 20)  # (Цвет, стороны)

# Проверка создания
print(f'Цвета круга 1: {circle1.get_color()}')
print(f'Стороны круга 1: количество - {circle1.sides_count} , длины - {circle1.get_sides()}')
print(f'Цвета круга 2: {circle2.get_color()}')
print(f'Стороны круга 2: количество - {circle2.sides_count} , длины - {circle2.get_sides()}')

# Проверка изменения цвета
circle1.set_color(55, 66, 77)
print(circle1.get_color())
circle2.set_color(465, 205, 745)
print(circle2.get_color())

# Проверка изменения сторон
circle1.set_sides(15)
print(circle1.get_sides())
circle2.set_sides(15, 44)
print(circle2.get_sides())

# Проверка периметра:
print(len(circle1))
print(len(circle2))

# Проверка площади
print(circle1.get_square())
print(circle2.get_square())

# # ПРОВЕРКА ТРЕУГОЛЬНИКА
triangle1 = Triangle((200, 200, 100), 10, 20, 20)
triangle2 = Triangle((300, 200, 100), 15, 20)

# Проверка создания
print(f'Цвета треугольника 1: {triangle1.get_color()}')
print(f'Стороны треугольника 1: количество - {triangle1.sides_count} , длины - {triangle1.get_sides()}')
print(f'Цвета треугольника 2: {triangle2.get_color()}')
print(f'Стороны треугольника 2: количество - {triangle2.sides_count} , длины - {triangle2.get_sides()}')

# Проверка изменения цвета
triangle1.set_color(55, 66, 77)
print(triangle1.get_color())
triangle2.set_color(465, 205, 745)
print(triangle2.get_color())

# Проверка изменения сторон
triangle1.set_sides(45, 55, 50)
print(triangle1.get_sides())
triangle2.set_sides(15, 44)
print(triangle2.get_sides())

# Проверка периметра:
print(len(triangle1))
print(len(triangle2))

# Проверка площади
print(triangle1.get_square())
print(triangle2.get_square())

# # ПРОВЕРКА КУБА
cube1 = Cube((200, 200, 100), 10)
cube2 = Cube((300, 200, 100), 15, 20)

# Проверка создания
print(f'Цвета куба 1: {cube1.get_color()}')
print(f'Стороны куба 1: количество - {cube1.sides_count} , длины - {cube1.get_sides()}')
print(f'Цвета куба 2: {cube2.get_color()}')
print(f'Стороны куба 2: количество - {cube2.sides_count} , длины - {cube2.get_sides()}')

# Проверка изменения цвета
cube1.set_color(55, 66, 77)
print(cube1.get_color())
cube2.set_color(465, 205, 745)
print(cube2.get_color())

# Проверка изменения сторон
cube1.set_sides(45, 55)
print(cube1.get_sides())
cube2.set_sides(15)
print(cube2.get_sides())

# Проверка периметра:
print(len(cube1))
print(len(cube2))

# Проверка объема
print(cube1.get_volume())
print(cube2.get_volume())
