class Pets():
    size = 0
    hunger = 0

    def hungry(self):
        if self.hunger > 5:
            print("I not't hungry")
        else:
            print("I'm hungry")
            print("*eating*")
            self.hunger = 10
            print("Now I'm not hungry")



