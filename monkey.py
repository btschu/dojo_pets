class Monkey:

    def __init__(self, name, type, tricks, noise, location):
        super().__init__(name, type, type, tricks, noise)
        self.location = location
    def freedom(self):
        if self.pet.location == "Zoo":
            print("Let me out of here!")
        else:
            print("I'm free!")
        return self

