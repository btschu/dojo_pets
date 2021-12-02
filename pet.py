from ninja import *

class Pet:

    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 100
        self. health = 100
        self.noises = noise
    def sleep(self):
        self.energy += 25
        return self
    def eat(self, ninja):
        self.energy += 5
        self.health += 10
        print(f"{self.name} ate {ninja.pet_food}! Energy = {self.energy}, Health = {self.health}")
        return self
    def play(self):
        self.health += 5
        self.energy -= 10
        print(f"{self.name} had a bath. Energy = {self.energy}, Health = {self.health}")
        return self
    def noise(self):
        print(self.noises) # moo, woof, etc
        return self

oscar = Pet("Oscar", "Cat", "Sleep", "Meow")
gizmo = Pet ("Gizmo", "Dog", "Roll Over", "Woof")
george = Pet("George", "Monkey", "Very Curious", "Oo Oo Ah Ah")
dumbo = Pet("Dumbo", "Elephant", "Flying", "Trumpetting")

brandon = Ninja("Brandon", "Schumacher", oscar, ["Friskies", "Kibbles", "Beggin' Strips"], "Purina")
brandon.feed().bathe().walk()