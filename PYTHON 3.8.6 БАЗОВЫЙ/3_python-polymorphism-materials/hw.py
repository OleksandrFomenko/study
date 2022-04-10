class User:
    def __init__(self, age, name, user_type):
        self.age = age
        self.name = name
        self.user_type = user_type

    def access_database(self):
        if self.user_type == "superuser":
            print("access granted")
        else:
            print("access denied")


class SuperUser(User):
    pass


u = User(40, 'Alex', 'superuser')
su = SuperUser(41, 'Tatyana', "user")
u.access_database()
su.access_database()
