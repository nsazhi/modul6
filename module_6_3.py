class Horse:
    x_distance = 0
    sound = 'Frrr'

    def __init__(self):
        super().__init__()

    def run(self, dx, dy):
        self.x_distance += dx
        super().fly(dy)


class Eagle:
    y_distance = 0

    def __init__(self):
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        super().run(dx, dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
