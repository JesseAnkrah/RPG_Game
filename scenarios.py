# this file will hold all the scenarios that will be used in the main file

# ":" is used to type cast and "=" is used for default values
#the "assert" keyword is used as a validator for the data you put inside
# ex: assert x >= 0, f"{x} is not greater than or equal to zero!!"
class Scene():
    def __init__(self,location, paths):
        self.location = location
        self.paths = paths

    def mk_entrance():
        return Scene("outside the castle door", {"forward": "enter the castle!"})
    def mk_dungeon():
        return Scene("Dungeon",{"left": "explore the left cellar",
                                "forward": "hidden trapdoor",
                                "right": "explore the right cellar",
                                "back": "return to the palace"})
    def mk_palace():
        return Scene("Palace",{"left": "enter the palace ballroom",
                                "forward": "enter the dungeon",
                                "right": "enter palace dining room",
                                "back": "return to the entrance"})
    def mk_palace_ballroom():
        return Scene("palace ballroom",{"left": "explore the left side of the ballroom",
                                        "forward": "enter graveyard",
                                        "right": "explore the right side of the ballroom",
                                        "back": "return to palace entrance"})
    def mk_graveyard():
        return Scene("Graveyard",{"left": "enter the morgue",
                                  "forward": "escape tunnel",
                                  "right": "explore the graveyard",
                                  "back": "return to the palace ballroom"})
    def mk_escape_tunnel():
        return Scene("Graveyard",{"forward": "you move closer to the light",
                                  "forward": "you move even closer to the light",
                                  "forward": "The light is moving towards you!",
                                  "forward": "you are engulfed in the light you cannot escape!"})
    def mk_lament_ending():
        return Scene("heaven or hell",{"up": "you are being transported to hell",
                                       "down": "you are being transported to heaven"})
    
# dungeon = Scene.mk_dungeon()
# print(dungeon.location)



