class Cat:
    def __init__(self, size, color, cat_type):
        self.size = size
        self.color = color
        self.cat_type = cat_type

    def set_size(self):
        if self.cat_type == "indoor":
            self.size = "small"
        else:
            self.size = "undifined"


class Tiger(Cat):
    def set_size(self):
        if self.cat_type == "wild":
            self.size = "big"
        else:
            self.size = "undifined"


cat = Cat('big', 'white', 'indoor')
print(cat.size)
cat.set_size()
print(cat.size)
tiger = Tiger('small', 'white', 'wild')
tiger.set_size()
print(tiger.size)
