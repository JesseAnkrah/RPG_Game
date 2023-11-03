import random
import items
import scenarios
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
# each movement or check bag causes a timer or counter to increase
# movements are 1 full point but checking bag would be .25 points
# each point increase causes a random number to spawn 
# the number is used to determine if an event such as monster attack will occur



# asks the user if they want to begin and only takes yes or no
# if neither is input it will continue to ask the user until one is input
begin = False
while begin == False:
    start = str(input("would you like to play this game?(yes/no): ")).lower()
    if start == "yes":
        print("lets begin")
        print("-----------------------------------------")
        begin = True
    elif start == "no":
        print("goodbye!")
        exit()

def line_break():
    print("-----------------------------------------")

def choose_path():
    print("choose your path from the options below!")

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

# different players which means different stats ect.
bimbardo = Player("Bimbardo","Mercenaries",150,33,0,100,0,100,5,0)
tortus = Player("Tortus","Knights",120,42,0,100,0,130,4,0)
sir_rath = Player("Sir-Rath","Nobles",100,50,0,100,0,150,3,0)
night_witch = Player("Night-Witch","Witches",80,63,0,100,0,170,0,0)
no_name = Player("NO-Name","Assasins",50,100,0,100,0,200,0,0)

char_list = ["Bimbardo","Tortus","Sir-Rath","Night-Witch","NO-Name"]

# function that makes you select a character
# matches character name to correct object
def char_select():
    global begin
    global play_char
    global game_start_entrance

    play_char = input("what character would you like to select? ")
    
    if play_char in char_list:
        print(f"You chose: {play_char}")
        line_break()
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
        game_start_entrance = True
    else:
        print("please select a character from the list(watch for caps)")

if begin == True:
    print("There are many characters to choose from")
    print("take you pick",char_list)
    line_break()
    while begin == True:
        char_select()

# function to start the game off
# takes input to displat either the path your allowed to go
# the option to fight
# or check your bag for items
# prints the scene options such as "forward" "back" ect.
def entrance_sequence():
    line_break()
    entrance = scenarios.Scene.mk_entrance()
    print(entrance.location)
    print("what will you do")
    play_char.choices()
    print(play_char.options)
    play_char_input = str(input("choose what to do: ")).lower()
    if play_char_input == "move":
        print(scenarios.Scene.mk_entrance().paths)
        choose_path()
        play_char.move()
        print([play_char.directions[1]])
        line_break()
        global game_start_entrance
        global game_start_palace 
        game_start_palace = False
        game_start_entrance = False
        play_char_input == str(input("choose what to do: ")).lower()
        if play_char_input == "forward":
            game_start_palace = True
    elif play_char_input == "check bag":
        play_char.bag()
        print(play_char.loot)
    elif play_char_input == "fight":
        print("there is no one here...")

# def entrance_sequence_forward():
#     if game_start_entrance == "move"

# allows user  to check bag without ending the game 
# can continue to ask
while game_start_entrance == True:
    entrance_sequence()

if game_start_palace == True:
    print("enter next stage")



# clock = items.Items.clock()


# location = scenarios.entrance


# print(location.location,location.paths)
# play_char.choices()
# print(play_char.options)

# next_move = input("")

# play_char.bag()

# play_char.loot.append(clock)
# print(play_char.loot[0].durability)
