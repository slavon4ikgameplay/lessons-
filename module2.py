class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        if self.gender == "Male":
            return f"{self.first_name} {self.last_name} is {self.age} y.o. He is {self.gender}"
        else:
            return f"{self.first_name} {self.last_name} is {self.age} y.o. She is {self.gender}"