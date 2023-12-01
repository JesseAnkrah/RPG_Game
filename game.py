import random
import players
import items  
import scenarios




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

# useful print statements i made functions to call easily 
def line_break():
    print("-----------------------------------------")

def possible_paths():
    print("these are all possible paths")

def choose_direction():
    print("choose your direction from the options below!")


# monster object created and assigned to monster variable
monster = players.Monster("Monster", 700, 0, 30)


# different players which means different stats ect.
bimbardo = players.Player("Bimbardo","Mercenaries",150,33,0,100,0,100,5,1)
tortus = players.Player("Tortus","Knights",120,42,0,100,0,130,4,3)
sir_rath = players.Player("Sir-Rath","Nobles",100,50,0,100,0,150,3,5)
night_witch = players.Player("Night-Witch","Witches",80,63,0,100,0,170,0,7)
no_name = players.Player("NO-Name","Assasins",50,100,0,100,0,200,0,10)

char_list = ["Bimbardo","Tortus","Sir-Rath","Night-Witch","NO-Name"]

# function that makes you select a character
def char_select():
    global begin
    global play_char
    global game_start_entrance

    play_char_name = input("what character would you like to select? ")
    
    if play_char_name in char_list:
        print(f"You chose: {play_char_name}")
        line_break()
        if play_char_name == "Bimbardo":
            play_char = bimbardo
            print(play_char)
        elif play_char_name == "Tortus":
            play_char = tortus
            print(play_char)
        elif play_char_name == "Sir-Rath":
            play_char = sir_rath
            print(play_char)
        elif play_char_name == "Night-Witch":
            play_char = night_witch
            print(play_char)
        elif play_char_name == "NO-Name":
            play_char = no_name
            print(play_char)
        
        begin = False
        game_start_entrance = True
    else:
        print("please select a character from the list(watch for caps)")


# how the user selects a character 
# allows multiple chances to select character
if begin == True:
    print("There are many characters to choose from")
    print("take you pick",char_list)
    line_break()
    while begin == True:
        char_select()

# intializing all the methods I will use
play_char.bag()
play_char.choices()
play_char.move()


# map object generation 
entrance = scenarios.Scene.mk_entrance()
palace = scenarios.Scene.mk_palace()
palace_ballroom = scenarios.Scene.mk_palace_ballroom()
dungeon = scenarios.Scene.mk_dungeon()
graveyard = scenarios.Scene.mk_graveyard()
escape_tunnel = scenarios.Scene.mk_escape_tunnel()
lament_ending = scenarios.Scene.mk_lament_ending()


# how item generate will be carried out
# items will not be guaranteed to generate
item_generation_chance = random.randint(0,10)
item_generation = None
# character luck stat affects the item generation chance
if play_char.luck >= 5:
    item_generation_chance = random.randint(3,10)
# numbers 5 or greater will generate items anything less wont 
if item_generation_chance < 5:
    item_generation = True
elif item_generation_chance >= 5:
    item_generation = True

# items objects being made
if item_generation == True:
    print("a mysterious force is at hand!")
    print("go look for items to help you survive")
    book = items.Items.book()
    blade = items.Items.blade()
    holy_water = items.Items.holy_water()
    torch = items.Items.torch()
    health_potion1 = items.Items.health_potion()
    health_potion2 = items.Items.health_potion()
    health_potion3 = items.Items.health_potion()
    holy_blade = items.Items.holy_blade()
    lament_puzzle1 = items.Items.lament_puzzle()
    lament_puzzle2 = items.Items.lament_puzzle()
    lament_puzzle3 = items.Items.lament_puzzle()
    completed_lament = items.Items.completed_lament()
# item objects being stored in different locations
    palace.present_items.extend([health_potion1,lament_puzzle1,holy_water])
    palace_ballroom.present_items.extend([blade,book])
    dungeon.present_items.extend([lament_puzzle2,health_potion2,torch])
    graveyard.present_items.extend([holy_blade,lament_puzzle3,health_potion3])

elif item_generation == False:
    print("Make it out quick!")
    print("for you shall surely perish otherwise")


# used to be useful will prob delete at a later time
# changed the way I track player location
player_location_list = [entrance.present_players, palace.present_players,
                        palace_ballroom.present_players,dungeon.present_players,
                        graveyard.present_players]


def check_bag():
    line_break()
    print("these are the all the items in your bag")
    for item in play_char.loot: # just prints all the items in your bag
        print([item.name],end="")
    print()
    line_break()

    print("these are the useable items in your bag!")
    print("if you want to use an item just type its name")
    print("or you can exit your bag by pressing enter")
    for item in play_char.loot: #prints the usable items in your bag   
        if item.type == "utility":
            print([item.name],end="")
    print()

    play_char_input = input("choose item or exit: ").lower()

    for item in play_char.loot: #checks list of loot to match and use the item you typed
        if play_char_input == item.name and item.type == "utility":
            item.durability -= 1
            play_char.health += item.health
            print(play_char.health)
            print(item.durability)
            if item.durability < 1:
                print(play_char.loot)
                print(item.name)
                play_char.loot.remove(item)
                print(play_char.loot)
                


# how monster attacks will be generated
# currently rigged to True. was for testing which it's good 
def monster_attack_func():
    monster_attack_chance = random.randint(8,10)
    monster_attack = False
    # if monster attack chance is 8 or above
    # the monster will attack
    if monster_attack_chance >= 8:
        monster_attack = True
    elif monster_attack_chance <= 7:
        monster_attack = False
    return monster_attack #returns a boolean to be used later

# monster attack sequence
def monster_attack_true():
    line_break()
    print("a monster a has appeared!")
    print([play_char.options[2]])
    play_char_input = input("you must fight!: ").lower()

    if play_char_input == "fight":
        # checks if player has any items on them at all 
        if len(play_char.loot) > 0:
            line_break()
            print("you can select an item to use during your fight or choose not to")
            play_char_input = input("type \"yes\" to use an item or type \"no\" to use your fist: ").lower()
            line_break()

            if play_char_input == "no":
                play_char.health -= monster.strength
                monster.health -= play_char.strength
                line_break()
                print(f"you have {play_char.health} hp left. the monster has {monster.health} hp left")
            
            elif play_char_input == "yes":
                weapon_found = False #tracks if weapons are found in loot
                for item in play_char.loot: #loops through the list to find objects with the type weapon
                    if item.type == "weapon":
                        print([item.name,item.damage])
                        weapon_found = True #flips to true if weapon is found
            
                if weapon_found: #allows the user player to pick which weapon to use if any
                    play_char_input = input("choose your weapon!: ").lower()
                
                    for item in play_char.loot: # this is what matches the input to the weapon also does the dmg calc
                        if item.type == "weapon" and play_char_input == item.name.lower():
                            print(f"you used {item.name} on the monster")
                            play_char_attack_with_item = item.damage + play_char.strength
                            monster.health -= play_char_attack_with_item
                            play_char.health -= monster.strength
                            print(f"you have {play_char.health} hp left. the monster has {monster.health} hp left.")
                            break
                    else: # every else statement is just incase you type wrong the program doesn't skip dmg calc
                        print("invalid input. your fist shall be used")
                        play_char.health -= monster.strength
                        monster.health -= play_char.strength
                        line_break()
                        print(f"you have {play_char.health} hp left. the monster has {monster.health} hp left.")

                elif weapon_found is False:
                    print("there are no weapons inside your inventory!")
                    print("you must use your hands to fight!")
                    play_char.health -= monster.strength
                    monster.health -= play_char.strength
                    line_break()
                    print(f"you have {play_char.health} hp left. the monster has {monster.health} hp left.")

            else:
                print("invalid input. your fist shall be used")
                play_char.health -= monster.strength
                monster.health -= play_char.strength
                line_break()
                print(f"you have {play_char.health} hp left. the monster has {monster.health} hp left.") 

        else:
            print("you must use your hands to fight!")
            play_char.health -= monster.strength
            monster.health -= play_char.strength
            line_break()
            print(f"you have {play_char.health} hp left. the monster has {monster.health} hp left.")

    else:
        print("invalid input. your fist shall be used")
        play_char.health -= monster.strength
        monster.health -= play_char.strength
        line_break()
        print(f"you have {play_char.health} hp left. the monster has {monster.health} hp left.")
       

# attaches boolean true or false to monster_attack_result
# will be used to force the character to fight
monster_attack_result = monster_attack_func()

if game_start_entrance == True:
    play_char.loot.extend([torch,health_potion1,health_potion2,blade])
    entrance.present_players.append(play_char)
    monster_attack_func
    if monster_attack_result:
        monster_attack_true()

while game_start_entrance == True:
    # takes input to display either the path your allowed to go
    # the option to move or check your bag
    # prints the scene options such as "forward" "back" ect.
    line_break()
    print(entrance.location)
    print("what will you do")
    print([play_char.options[0],play_char.options[1]])
    play_char_input = input("choose what to do: ").lower()
    if play_char_input == "move":
        line_break()
        possible_paths()
        print(entrance.paths)
        choose_direction()
        print([play_char.directions[1]])
        line_break()
        game_start_entrance = False
        play_char_input = input("choose where to move: ").lower()
        if play_char_input == "forward":
            game_start_palace = True
            entrance.present_players.remove(play_char)
    elif play_char_input == "check bag":
        check_bag()
    elif play_char_input == "fight":
        print("why did you type fight????")
        print("stick to the script")
    
 

if game_start_palace == True:
    player_location = palace.present_players
    palace.present_players.append(play_char)
    monster_attack_func()

# player_location = None

# def change_scene(location):
#     if game_start_palace == True:
#         player_location = location.present_players
#         location.present_players.append(play_char)
#         return player_location, play_hp
#         monster_attack_func()

# x, y = change_scene()

# check the item generation i turned it to always true for testing purposes
# gave player holy blade and blade for testing purposes fix it 
# comment up the monster attack true function 
# fix the monster attack func to reduce item durability
# make sure to seperate the function to make it more readable
# fix error where items dont show up in bag after the fight sequence in the begining 
# when using play_char.loot
# use a function that changes the player location to diff scenes
# make function to check items in bag should be chopped down version of monster attack for loop