# holds the player and monster class

# player stats, conditions, and info
class Player:
    def __init__(self,name,affil,health,stamina,fatigue,sanity,hunger,strength,armour,luck):
        self.name = name
        self.affil = affil
        self.health = health
        self.stamina = stamina
        self.fatigue = fatigue
        self.sanity = sanity
        self.hunger = hunger
        self.strength = strength
        self.armour = armour
        self.luck = luck 
    
    # a way to return player stats and display them
    def __str__(self):
        return f"{self.name} is afflitated with the {self.affil},\nthey have {self.health}:health, {self.stamina}:stamina, {self.strength}:strength, and {self.armour}:armour"
    
    def move(self):
        self.directions = ["left","forward","right","back"]

    def bag(self):
        self.loot = []

    def choices(self):
        self.options = ["check bag","move","fight"]

    def current_stats(self):
        print(f"{self.health}:health")
        print(f"{self.stamina}:stamina")
        print(f"{self.sanity}:sanity")
        print(f"{self.hunger}:hunger")
        if self.stamina <= 0:
            print(f"{self.fatigue}:fatigue")



# monster stats, and info
class Monster():
    def __init__(self, name, health, hunger, strength):
        self.name = name
        self.health = health
        self.hunger = hunger
        self.strength = strength