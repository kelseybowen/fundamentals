class Ninja:
    
    def __init__(self, first_name, last_name, treats, pet_food, pets):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet(pets[1])
    
    def walk(self):
        self.pet.play()
        print(f"Playing with {self.pet.name}")
        return self
    
    def feed(self):
        self.pet.eat()
        print(f"Feeding {self.pet.name}")
        return self
    
    def bathe(self):
        self.pet.noise()
        print(f"Bathing {self.pet.name}")
        return self
    
class Pet:
    
    def __init__(self, pets, health=20, energy=20):
        self.name = pets["name"]
        self.type = pets["type"]
        self.tricks = pets["tricks"]
        self.health = health
        self.energy = energy
        self.sound = pets["noise"]
    
    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    
    def play(self):
        self.health += 5
        return self
    
    def noise(self):
        print(self.sound)
        return self


pets = [
    {
        "name": "Fido",
        "type": "dog",
        "tricks": "sit",
        "noise": "BARK"
    },
    {
        "name": "Mittens",
        "type": "cat",
        "tricks": "balance",
        "noise": "MEOW"
    }
]

kelsey = Ninja("kelsey", "bowen", "yum", "pellets", pets)
print(kelsey.walk().feed().bathe())

