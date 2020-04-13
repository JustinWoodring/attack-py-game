from random import randint


#Variables
kill = "false"
popused = 0
popused2 = 0
#Squirrel-----------
Squirrelcap = 1
Squirrelpopused = 5
Squirrelfoodcost = 200
Squirrelfoodprovided = 50
Squirrelgoldprovided = 50
Squirrelwoodprovided = 50
Squirrelattack = 1000
Foodeatenbysquirrel = 50
#Settler------------
Settlerpopused = 1
Settlerfoodcost = 200
Settlercap = 10
Settlerfoodprovided = 10
Settlergoldprovided = 10
Settlerwoodprovided = 10
Foodeatenbysettler = 5
Settlerattack = 5
#House--------------
Housepopprovided = 5
Housecap = 40
Housewoodcost = 300
Housegoldcost = 100
#Farm---------------
Farmcap = 5
Farmfoodprovided = 10
Farmfoodcost = 100
Farmwoodcost = 200


#Objects
#Units
class Person(object):
    pass


class Settler(Person):

    def __init__(self):
        ## ??
        self.name = SettlerNames[len(SettlerList)]

        #Settler has properties.
        self.work = "nothing"
        self.health = 185
        #Add Settler to the list.
        SettlerList.append(self.name)
        SettlerObjectList.append(self)
        global popused
        popused = popused + Settlerpopused

    def assignmethod(self, work):
        self.work = work

    def changehealth(self, health):
        self.health = health


class Settler2(Person):

    def __init__(self):
        ## ??
        self.name = SettlerNames2[len(SettlerList2)]

        #Settler has properties.
        self.work = "nothing"
        self.health = 185
        #Add Settler to the list.
        SettlerList2.append(self.name)
        SettlerObjectList2.append(self)
        global popused2
        popused2 = popused2 + Settlerpopused

    def assignmethod(self, work):
        self.work = work

    def changehealth(self, health):
        self.health = health


class Squirrel(Person):

    def __init__(self):
        ## ??
        self.name = SquirrelNames[len(SquirrelList)]

        #Settler has properties.
        self.work = "nothing"
        self.health = 500
        #Add Settler to the list.
        SquirrelList.append(self.name)
        SquirrelObjectList.append(self)
        global popused
        popused = popused + Squirrelpopused

    def assignmethod(self, work):
        self.work = work

    def changehealth(self, health):
        self.health = health


class Squirrel2(Person):

    def __init__(self):
        ## ??
        self.name = SquirrelNames2[len(SquirrelList2)]

        #Settler has properties.
        self.work = "nothing"
        self.health = 500
        #Add Settler to the list.
        SquirrelList2.append(self.name)
        SquirrelObjectList2.append(self)
        global popused2
        popused2 = popused2 + Squirrelpopused

    def assignmethod(self, work):
        self.work = work

    def changehealth(self, health):
        self.health = health


#Buildings
class Building(object):
    pass


class House(Building):
    def __init__(self):
        ##??
        self.name = HouseNames[len(HouseList)]

        #House has-properties.
        self.health = 400
        #Add House to the list.
        HouseList.append(self.name)
        HouseObjectList.append(self)

    def changehealth(self, health):
        self.health = health


class House2(Building):
    def __init__(self):
        ##??
        self.name = HouseNames2[len(HouseList2)]

        #House has-properties.
        self.health = 400
        #Add House to the list.
        HouseList2.append(self.name)
        HouseObjectList2.append(self)

    def changehealth(self, health):
        self.health = health


class Farm(Building):
    def __init__(self):
        ##??
        self.name = FarmNames[len(FarmList)]

        #Farm has-properties.
        self.health = 200
        #Add Farm to the list.
        FarmList.append(self.name)
        FarmObjectList.append(self)

    def changehealth(self, health):
        self.health = health


class Farm2(Building):
    def __init__(self):
        ##??
        self.name = FarmNames2[len(FarmList2)]

        #Farm has-properties.
        self.health = 200
        #Add Farm to the list.
        FarmList2.append(self.name)
        FarmObjectList2.append(self)

    def changehealth(self, health):
        self.health = health

##############################################################################
#Lists
##############################################################################

#Make lists relevant to their object lists.
#Object List holds the data by which we can assign a handle so that
#we can modify parts of the referenced object.

#Names so that each objects instance has a unique identifier.

#Units

#Settler
SettlerList = []
SettlerObjectList = []
SettlerNames = ['John', 'Elizabeth', 'Benjamin', 'Virginia', 'Smith', 'Mary',
'Thomas', 'Anne', 'Henry', 'Jane', 'Nicholas', 'Isabel', 'Matthew', 'Grace',
'Peter', 'Charles', 'James', 'George', 'Edward', 'Claire', 'Constance', 'Abby']

SettlerList2 = []
SettlerObjectList2 = []
SettlerNames2 = ['0', '1', '2', '3', '4', '5',
'6', '7', '8', '9', '10', '11', '12', '13',
'14', '15', '16', '17', '18', '19', '20', '21']

#Squirrel
SquirrelList = []
SquirrelObjectList = []
SquirrelNames = ['Skuwearielle', 'Squial']

SquirrelList2 = []
SquirrelObjectList2 = []
SquirrelNames2 = ['1', '2']

#Buildings

#House
HouseList = []
HouseObjectList = []
HouseNames = ['House1', 'House2', 'House3', 'House4', 'House5', 'House6',
'House8', 'House9', 'House10', 'House11', 'House12', 'House13', 'House14',
'House15', 'House16', 'House17', 'House18', 'House19', 'House20', 'House21',
'House22', 'House23', 'House24', 'House25', 'House26', 'House26', 'House27',
'House28', 'House29', 'House30', 'House31', 'House32', 'House33', 'House34',
'House35', 'House36', 'House37', 'House38', 'House39', 'House40']

HouseList2 = []
HouseObjectList2 = []
HouseNames2 = ['House1', 'House2', 'House3', 'House4', 'House5', 'House6',
'House8', 'House9', 'House10', 'House11', 'House12', 'House13', 'House14',
'House15', 'House16', 'House17', 'House18', 'House19', 'House20', 'House21',
'House22', 'House23', 'House24', 'House25', 'House26', 'House26', 'House27',
'House28', 'House29', 'House30', 'House31', 'House32', 'House33', 'House34',
'House35', 'House36', 'House37', 'House38', 'House39', 'House40']

#Farm
FarmList = []
FarmObjectList = []
FarmNames = ['Farm1', 'Farm2', 'Farm3', 'Farm4', 'Farm5']

FarmList2 = []
FarmObjectList2 = []
FarmNames2 = ['Farm1', 'Farm2', 'Farm3', 'Farm4', 'Farm5']

##############################################################################
#Setup
##############################################################################
maker = "Booglejr"
license = "   MIT License   "


def end2():
    global food2
    global wood2
    global gold2
    global Farmfoodprovided
    global Settlerfoodprovided
    global Settlerwoodprovided
    global Settlergoldprovided
    global Foodeatenbysettler
    global Squirrelwoodprovided
    global Squirrelfoodprovided
    global Squirrelgoldprovided
    global Foodeatenbysquirrel
    food_eaten = 0
    i = 0
    i2 = 0
    for x in range(0, len(SettlerList2)):
        name = SettlerList2[i]
        if name in SettlerList2:
            a = SettlerObjectList2[SettlerList2.index(name)]
            if a.work == "wood":
                woodgather = 0
                woodgather = woodgather + Settlerwoodprovided
                wood2 = wood2 + woodgather
            elif a.work == "food":
                foodgather = 0
                foodgather = foodgather + Settlerfoodprovided
                food2 = food2 + foodgather
            elif a.work == "gold":
                goldgather = 0
                goldgather = goldgather + Settlergoldprovided
                gold2 = gold2 + goldgather
            else:
                pass
            food_eaten = food_eaten + Foodeatenbysettler
        else:
            pass
        i = i + 1
    for x in range(0, len(SquirrelList2)):
        name = SquirrelList2[i2]
        if name in SquirrelList2:
            a = SquirrelObjectList2[SquirrelList2.index(name)]
            if a.work == "wood":
                woodgather = 0
                woodgather = woodgather + Squirrelwoodprovided
                wood2 = wood2 + woodgather
            elif a.work == "food":
                foodgather = 0
                foodgather = foodgather + Squirrelfoodprovided
                food2 = food2 + foodgather
            elif a.work == "gold":
                goldgather = 0
                goldgather = goldgather + Squirrelgoldprovided
                gold2 = gold2 + goldgather
            else:
                pass
            food_eaten = food_eaten + Foodeatenbysquirrel
        else:
            pass
        i2 = i2 + 1
    #Calculate new values.
    food2 = food2 - food_eaten
    food2 = food2 + len(FarmList2) * Farmfoodprovided


def enemyturn():
########################
#Assigning Duties
########################
    i = 0
    i2 = 0
    for x in range(0, len(SettlerList2)):
        name = SettlerList2[i]
        if name in SettlerList2:
            a = SettlerObjectList2[SettlerList2.index(name)]
            if a.work == "nothing":
                val = randint(0, 100)
                if 50 >= val:
                    a.assignmethod("food")
                elif 75 >= val:
                    a.assignmethod("wood")
                elif 100 >= val:
                    a.assignmethod("gold")
                else:
                    pass
            else:
                pass
        else:
            pass
        i = i + 1
    for x in range(0, len(SquirrelList2)):
        name = SquirrelList2[i2]
        if name in SquirrelList2:
            a = SquirrelObjectList[SquirrelList2.index(name)]
            if a.work == "nothing":
                val = randint(0, 100)
                if 50 >= val:
                    a.assignmethod("food")
                elif 75 >= val:
                    a.assignmethod("wood")
                elif 100 >= val:
                    a.assignmethod("gold")
                else:
                    pass
            else:
                pass
        else:
            pass
        i2 = i2 + 1
########################
#Creating Settlers.
########################
    global food2
    global wood2
    global gold2
    if 56 == randint(0, 100):
        if len(SquirrelList2) < Squirrelcap:
            if food2 >= Squirrelfoodcost:
                if popused2 < len(HouseList2) * Housepopprovided:
                    food2 = food2 - Squirrelfoodcost
                    Squirrel()
                    end2()
                else:
                    House2()
                    end2()
            else:
                if len(SettlerList2) < Settlercap:
                    if food2 >= Settlerfoodcost:
                        if popused2 < len(HouseList2) * Housepopprovided:
                            food2 = food2 - Settlerfoodcost
                            Settler2()
                            end2()
                        else:
                            House2()
                            end2()
                    else:
                        pass
                else:
                    pass
        else:
            if len(SettlerList2) < Settlercap:
                if food2 >= Settlerfoodcost:
                    if popused2 < len(HouseList2) * Housepopprovided:
                        food2 = food2 - Settlerfoodcost
                        Settler2()
                        end2()
                    else:
                        House2()
                        end2()
                else:
                    pass
            else:
                pass
    elif len(SettlerList2) < Settlercap:
        if food2 >= Settlerfoodcost:
            if popused2 < len(HouseList2) * Housepopprovided:
                food2 = food2 - Settlerfoodcost
                Settler2()
                end2()
            else:
                House2()
                end2()
        else:
            pass
    else:
        pass
    print("enemy")
########################
#Creating Farms.
########################
    if len(FarmList) < Farmcap:
        if wood2 >= Farmwoodcost:
            if food2 >= Farmfoodcost:
                wood2 = wood2 - Farmwoodcost
                food2 = food2 - Farmfoodcost
                Farm2()
                end2()
            else:
                pass
        else:
            pass
    else:
        pass
    end2()


def help():
    print("\033[1;33m                                   ")
    print("?,               to bring up this help menu.")
    print("resign,          to quit game.")
    print("building list,   to bring up a list of available buildings.")
    print("unit list,       to bring up a list of available units.")
    print("stats,           to bring up a list stats.")
    print("settler,         to bring up settlers and current assignments.")
    print("train,           to train units.")
    print("build,           to select and construct available buildings.")
    print("assign,          to assign a settler to collect resources.")
    print("[enter],       to end the user's turn.\033[1;m" +
    " *Certain actions such as moving or attacking a unit will cause this.")


def unitlist():
    print("\033[1;33m")
    print("1,               Settler (" + str(Settlerfoodcost) + " food).")
    print("\033[1;m")


def buildinglist():
    print("\033[1;33m")
    print("1,               House (" + str(Housewoodcost) + " wood, " +
    str(Housegoldcost) + " gold).")
    print("2,               Farm (" + str(Farmfoodcost) + " food, " +
    str(Farmwoodcost) + " wood).")
    print("\033[1;m")

def end():
    #Set basic variables for calculations.
    global food
    global wood
    global gold
    global Farmfoodprovided
    global Settlerfoodprovided
    global Settlerwoodprovided
    global Settlergoldprovided
    global Foodeatenbysettler
    global Squirrelwoodprovided
    global Squirrelfoodprovided
    global Squirrelgoldprovided
    global Foodeatenbysquirrel
    food_eaten = 0
    i = 0
    i2 = 0
    for x in range(0, len(SettlerList)):
        name = SettlerList[i]
        if name in SettlerList:
            a = SettlerObjectList[SettlerList.index(name)]
            if a.work == "wood":
                woodgather = 0
                woodgather = woodgather + Settlerwoodprovided
                wood = wood + woodgather
            elif a.work == "food":
                foodgather = 0
                foodgather = foodgather + Settlerfoodprovided
                food = food + foodgather
            elif a.work == "gold":
                goldgather = 0
                goldgather = goldgather + Settlergoldprovided
                gold = gold + goldgather
            else:
                pass
            food_eaten = food_eaten + Foodeatenbysettler
        else:
            pass
        i = i + 1
    for x in range(0, len(SquirrelList)):
        name = SquirrelList[i2]
        if name in SquirrelList:
            a = SquirrelObjectList[SquirrelList.index(name)]
            if a.work == "wood":
                woodgather = 0
                woodgather = woodgather + Squirrelwoodprovided
                wood = wood + woodgather
            elif a.work == "food":
                foodgather = 0
                foodgather = foodgather + Squirrelfoodprovided
                food = food + foodgather
            elif a.work == "gold":
                goldgather = 0
                goldgather = goldgather + Squirrelgoldprovided
                gold = gold + goldgather
            else:
                pass
            food_eaten = food_eaten + Foodeatenbysquirrel
        else:
            pass
        i2 = i2 + 1
    #Calculate new values.
    food = food - food_eaten
    food = food + len(FarmList) * Farmfoodprovided
    enemyturn()


##############################################################################
#Stats
##############################################################################
def settlerstat():
    print("\033[1;32m")
    v = len(SettlerList) + len(SquirrelList)
    print("You have currently {} settlers.".format(v))
    i = 0
    i2 = 0
    for x in range(0, len(SettlerList)):
        name = SettlerList[i]
        if name in SettlerList:
            a = SettlerObjectList[SettlerList.index(name)]
            if a.health <= 50:
                color = "\033[1;31m"
            elif a.health >= 50:
                color = "\033[1;32m"
            else:
                pass
            white = "\033[1;m"
            print(white)
            print("|" + a.name + ":")
            print("|--------------------------------------------|")
            print("|    " + color + "Health: " + white + str(a.health))
            print("|    " + a.name + " is gathering " + a.work)
            print("|____________________________________________|")
        else:
            pass
        i = i + 1
    for x in range(0, len(SquirrelList)):
        name = SquirrelList[i2]
        if name in SquirrelList:
            a = SquirrelObjectList[SquirrelList.index(name)]
            if a.health <= 50:
                color = "\033[1;31m"
            elif a.health >= 50:
                color = "\033[1;32m"
            else:
                pass
            white = "\033[1;m"
            print(white)
            print("|" + a.name + ":")
            print("|--------------------------------------------|")
            print("|    " + color + "Health: " + white + str(a.health))
            print("|    " + a.name + " is gathering " + a.work)
            print("|____________________________________________|")
        else:
            pass
        i2 = i2 + 1
    print("\033[1;m")


def actionstat():
    punused = len(HouseList) * Housepopprovided
    v = len(SettlerList) + len(SquirrelList)
    print("\033[1;32m")
    print("You have {}/{} settlers".format(v, Settlercap))
    print("You have {} food, {} wood, {} gold.".format(food, wood, gold))
    print("Population: {}PU/{}PS.".format(popused, punused))
    print("Houses: {}/{}".format(len(HouseList), Housecap))
    print("Farm: {}/{}".format(len(FarmList), Farmcap))
    print("\033[1;m")
    punused2 = len(HouseList2) * Housepopprovided
    v2 = len(SettlerList2) + len(SquirrelList2)
    print("\033[1;32m")
    print("You have {}/{} settlers".format(v2, Settlercap))
    print("You have {} food, {} wood, {} gold.".format(food2, wood2, gold2))
    print("Population: {}PU/{}PS.".format(popused2, punused2))
    print("Houses: {}/{}".format(len(HouseList2), Housecap))
    print("Farm: {}/{}".format(len(FarmList2), Farmcap))
    print("\033[1;m")
    actionmove = input("(? for available moves)> ")
    #Game control
    if actionmove == "?":
        return help()
    elif actionmove == "resign":
        global kill
        kill = "true"
        print("Bye! See you soon!")
    elif actionmove == "":
        return end()
    elif actionmove == "unit list":
        return unitlist()
    elif actionmove == "building list":
        return buildinglist()
    #Stats
    elif actionmove == "settler":
        return settlerstat()
    #Moves
    elif actionmove == "assign":
        return assign()
    elif actionmove == "train":
        return train()
    elif actionmove == "build":
        return build()
    #Else
    else:
        print("Command not understood. Listing available commands.")
        return help()


##############################################################################
#Actions
##############################################################################
def assign():
    i = 0
    i2 = 0
    for x in range(0, len(SettlerList)):
        name = SettlerList[i]
        if name in SettlerList:
            a = SettlerObjectList[SettlerList.index(name)]
            print("\033[1;33m" +
            a.name + " is gathering " + a.work +
            "\033[1;m")
        else:
            pass
        i = i + 1
    for x in range(0, len(SquirrelList)):
        name = SquirrelList[i2]
        if name in SquirrelList:
            a = SquirrelObjectList[SquirrelList.index(name)]
            print("\033[1;33m" +
            a.name + " is gathering " + a.work +
            "\033[1;m")
        else:
            pass
        i2 = i2 + 1
    name = input("(Please type settler name.)>")
    work = input("(food, wood, or gold?)>")
    if name in SettlerList:
        if work == "wood" or "food" or "gold":
            a = SettlerObjectList[SettlerList.index(name)]
            a.assignmethod(work)
        else:
            print(work + " is not a recognized resource.")
    elif name in SquirrelList:
        if work == "wood" or "food" or "gold":
            a = SquirrelObjectList[SquirrelList.index(name)]
            a.assignmethod(work)
        else:
            print(work + " is not a recognized resource.")
    else:
        print("Could not locate " + name)


def train():
    global food
    global gold
    global wood
    global popuse
    number = input("(Please type unit number, to view the list type ?)>")
    if number == "1":
        if 56 == randint(0, 100):
            if len(SquirrelList) < Squirrelcap:
                if food >= Squirrelfoodcost:
                    if popused < len(HouseList) * Housepopprovided:
                        food = food - Squirrelfoodcost
                        Squirrel()
                        end()
                    else:
                        if len(SettlerList) < Settlercap:
                            if food >= Settlerfoodcost:
                                if popused < len(HouseList) * Housepopprovided:
                                    food = food - Settlerfoodcost
                                    Settler()
                                    end()
                                else:
                                    print("Not enough population support!")
                            else:
                                print("Not enough food!")
                        else:
                            print("Max settlers reached!")
                else:
                    if len(SettlerList) < Settlercap:
                        if food >= Settlerfoodcost:
                            if popused < len(HouseList) * Housepopprovided:
                                food = food - Settlerfoodcost
                                Settler()
                                end()
                            else:
                                print("Not enough population support!")
                        else:
                            print("Not enough food!")
                    else:
                        print("Max settlers reached!")
            else:
                if len(SettlerList) < Settlercap:
                    if food >= Settlerfoodcost:
                        if popused < len(HouseList) * Housepopprovided:
                            food = food - Settlerfoodcost
                            Settler()
                            end()
                        else:
                            print("Not enough population support!")
                    else:
                        print("Not enough food!")
                else:
                    print("Max settlers reached!")
        elif len(SettlerList) < Settlercap:
            if food >= Settlerfoodcost:
                if popused < len(HouseList) * Housepopprovided:
                    food = food - Settlerfoodcost
                    Settler()
                    end()
                else:
                    print("Not enough population support!")
            else:
                print("Not enough food!")
        else:
            print("Max settlers reached!")
    elif number == "?":
        return unitlist()
    else:
        print("Not understood!")


def build():
    global food
    global gold
    global wood
    number = input("(Please type building number, to view the list type ?)>")
    if number == "1":
        if len(HouseList) < Housecap:
            if wood >= Housewoodcost:
                if gold >= Housegoldcost:
                    wood = wood - Housewoodcost
                    gold = gold - Housegoldcost
                    House()
                    end()
                else:
                    print("Not enough gold!")
            else:
                print("Not enough wood!")
        else:
            print("Max houses reached!")
    elif number == "2":
        if len(FarmList) < Farmcap:
            if wood >= Farmwoodcost:
                if food >= Farmfoodcost:
                    wood = wood - Farmwoodcost
                    food = food - Farmfoodcost
                    Farm()
                    end()
                else:
                    print("Not enough food!")
            else:
                print("Not enough wood!")
        else:
            print("Max farms reached")
    elif number == "?":
        return buildinglist()
    else:
        print("Not understood!")


##############################################################################
#Start the game system.
##############################################################################
print("\033[1;31m")
print("      ____     __________ __________     ____        ______  __    __")
print("     / __ \    \___  ___/ \___  ___/    / __ \      / _____| | |  / /")
print("    / /  \ \      |  |       |  |      / /  \ \    / /       | |_/ /")
print("   / /____\ \     |  |       |  |     / /____\ \  | |        |    /")
print("  / ________ \    |  |       |  |    / ________ \ | |        | __ \ ")
print(" / /        \ \   |  |       |  |   / /        \ \ \ \_____  | | \ \ ")
print("/_/          \_\  |__|       |__|  /_/          \_\ \______| |_|  \_\ ")
print("                                                                     ")
print("                            Game Designed                            ")
print("                                 And                                 ")
print("                            Programmed By                            ")
print("                                                                     ")
print("                               " + maker + "                         ")
print("                                                                     ")
print("                              This Game                              ")
print("                        Is Shared Accordingly                        ")
print("                              Using The                              ")
print("                          " + license + "                          ")
print("\033[1;m")

level = input("(Easy, Medium, Hard?)> [Easy] ")
name = input("Your name?>")
if level == "" or level == "Easy" or level == "easy":
    wood = 500
    food = 500
    gold = 500
    wood2 = 300
    food2 = 300
    gold2 = 300
    Settler()
    Settler()
    Settler()
    Settler2()
    Settler2()
    Settler2()
    House()
    House2()
elif level == "Medium" or level == "medium":
    wood = 300
    food = 300
    gold = 300
    wood2 = 300
    food2 = 300
    gold2 = 300
    Settler()
    Settler()
    Settler2()
    Settler2()
    House()
    House2()
elif level == "Hard" or level == "hard":
    wood = 100
    food = 100
    gold = 100
    wood = 300
    food = 300
    gold = 300
    Settler()
    Settler()
    Settler2()
    Settler2()
    House()
    House2()
else:
    wood = 500
    food = 500
    gold = 500
    wood2 = 300
    food2 = 300
    gold2 = 300
    Settler()
    Settler()
    Settler()
    Settler2()
    Settler2()
    Settler2()
    House()
    House2()
actionstat()

while kill == "false":
    if food < -50:
        kill = "true"
    actionstat()
