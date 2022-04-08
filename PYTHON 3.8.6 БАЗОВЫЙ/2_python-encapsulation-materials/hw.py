class User:
    def __init__(self, name, age):
        self.__age = age
        self.name = name

    @property
    def get_age(self):
        return self.__age

    @get_age.setter
    def set_age(self, value):
        if value > 0:
            self.__age = value
        else:
            print("nagative value")
            self.__age = 0

u1 = User('Alex', 20)
u1.set_age = -10
print(u1.get_age)
