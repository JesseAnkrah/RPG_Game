# this file will hold all the scenarios that will be used in the main file

# ":" is used to type cast and "=" is used for default values
#the "assert" keyword is used as a validator for the data you put inside
# ex: assert x >= 0, f"{x} is not greater than or equal to zero!!"
class Scene():
    def __init__(self,location, paths):
        self.location = location
        self.paths = paths

    def mk_dungeon():
        return Scene("Dungeon",["left, forward, right, back"])
    def mk_palace():
        return Scene("Palace",["left, forward, right, back"])
    def mk_graveyard():
        return Scene("Graveyard",["left, forward, right, back"])
    def mk_escape_tunnel():
        return Scene("Graveyard",["left, forward, right, back"])

# dungeon = Scene.mk_dungeon()
# print(dungeon.location)



