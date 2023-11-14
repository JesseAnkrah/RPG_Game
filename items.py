# this will have all the items that are available to the player

class Items():
    def __init__(self,name,type,durability):
        self.name = name
        self.type = type
        self.durability = durability

    def book():
        return Items("strange_book","book",99999)
    def blade():
        return Items("blade","weapon",12)
    def holy_water():
        return Items("holy water","unkown",1)
    def torch():
        return Items("torch","utility",99999)
    def health_potion():
        return Items("health potion","utility",1)
    def holy_blade():
        return Items("holy blade","weapon",99999)
    def lament_puzzle():
        return Items("lament","puzzle piece",1)
    def completed_lament():
        return Items("completed lament","completed puzzle",1)
    def lament_puzzle_piece_found():
        print("you have found one part of the lament puzzle!")
    def item_here_hint():
        print("There is an item somewhere here!!!")

