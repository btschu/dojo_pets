import ninja

class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 100
        self. health = 100
        self.noise = noise
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    def play(self):
        self.health += 5
        self.energy -= 10
        return self
    def noise(self):
        print(self.noise) # moo, woof, etc
        return self

oscar = Pet("Oscar", "Cat", "Sleep", "Meow")
gizmo = Pet ("Gizmo", "Dog", "Roll Over", "Woof")
george = Pet("George", "Monkey", "Very Curious", "Oo Oo Ah Ah")
dumbo = Pet("Dumbo", "Elephant", "Flying", "Trumpetting")

brandon = Ninja("Brandon", "Schumacher", "Oscar", ["Friskies", "Kibbles", "Beggin' Strips"], "Purina")

brandon.feed().walk().bathe()
