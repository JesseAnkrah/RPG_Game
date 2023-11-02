# this will have all the items that are available to the player

class Items():
    def __init__(self,name,type,durability):
        self.name = name
        self.type = type
        self.durability = durability

    def clock():
        return Items("clock","utility",99999)
    def blade():
        return Items("blade","weapon",12)
    def holy_water():
        return Items("holy water","unkown",1)
    def torch():
        return Items("torch","utility",99999)



    

# item_present = True

# while item_present:
#     item_select = input("you find something on the floor it seems to be a clock? pick it up (y/n) ")
#     if item_select == "y":
#         print(clock)
#         item_present = None
#     elif item_select == "n":
#         print("you walk past it...")
#         item_present = None
#     else:
#         print("try again only press y/n!")
#         item_present = True
    

        

