class Parallelogram:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def get_area(self):
        return self._width * self._length


class Square(Parallelogram):
    def get_area(self):
        return self._width * self._width


p = Parallelogram(10, 15)
print(p.get_area())

s = Square(20, 20)
print(s.get_area())
