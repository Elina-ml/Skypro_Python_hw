class User:
    def __init__(self, name, surname):
        self.first_name = name
        self.last_name = surname

    def say_name(self):
        print("Моё имя:", self.first_name)

    def say_surname(self):
        print("Моя фамилия:", self.last_name)

    def say_full_name(self):
        print("Моё полное имя:", self.last_name, self.first_name)
