import random 
# there will be items that boost hidden stats only
# track location of 'monster'
# monster will pop up randomly and chase you for a random amount of 'tiles'
# or turns which ever one
# you can fight back 
# stats will constantly be adjusting in the background
# stats will be displayed every 5 tiles moved or turns 
# will prob need some sort of counter variable multiple at that
# will keep a timer or clock in the background 
# this will be in charge of monster attacks along with randomint method
# the longer the time spent in the castle the more likely you die
# all players will find a clock to start 





# asks the user if they want to begin and only takes yes or no
# if neither is input it will continue to ask the user until one is input

begin = False
while begin == False:
    start = input("would you like to play this game?(yes/no): ").lower()
    if start == "yes":
        print("lets begin")
        begin = True
    elif start == "no":
        print("goodbye!")
        begin = None



# player stats, conditions, and info
class player:
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
        return f"{self.name} is afflitated with the {self.affil},\n{self.health}:health, {self.stamina}:stamina, {self.strength}:strength,and {self.armour}:armour"
    
    def move(self):
        directions = ["left","forward","right","back"]
    


# different players which means different stats ect.
bimbardo = player("Bimbardo","Mercenaries",150,33,0,100,0,100,5,0)
tortus = player("Tortus","Knights",120,42,0,100,0,130,4,0)
sir_rath = player("Sir-Rath","Nobles",100,50,0,100,0,150,3,0)
night_witch = player("Night-Witch","Witches",80,63,0,100,0,170,0,0)
no_name = player("NO-Name","Assasins",50,100,0,100,0,200,0,0)

char_list = ["Bimbardo","Tortus","Sir-Rath","Night-Witch","NO-Name"]

# function that makes you select a character
# matches character name to correct variable so that you can call the class
def char_select():
    global begin
    play_char = input("what character would you like to select? ")
    if play_char in char_list:
        print(f"You chose: {play_char}")
        if play_char == "Bimbardo":
            play_char = bimbardo
        elif play_char == "Tortus":
            play_char = tortus
        elif play_char == "Sir-Rath":
            play_char = sir_rath
        elif play_char == "Night-Witch":
            play_char = night_witch
        elif play_char == "NO-Name":
            play_char = no_name
        print(play_char)
        begin = None
    else:
        print("please select a character from the list(watch for caps)")

if begin == True:
    print("There are many characters to choose from")
    print("take you pick",char_list)
    while begin == True:
        char_select()

print()
