class Cat:

    def __init__(self, name, type, tricks, noise, purr_volume = 2):
        super().__init__(name, type, type, tricks, noise)
        self.purr_volume = purr_volume
    def pet_belly(self):
        self.pet.purr_volume += 2
        return self