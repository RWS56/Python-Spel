import time
import random
level10 = False

class player():
    def __init__(self, strength, hp, inventory, level):
        self.strength = 3
        self.hp = 3
        self.inventory = []
        self.level = 0

class Item():
    def __init__(self, itemName, itemDescription, strengthBonus, healthBonus, defenseBonus):
        self.itemName = itemName
        self.itemDescription = itemDescription
        self.strengthBonus = strengthBonus
        self.healthBonus = healthBonus
        self.defenseBonus = defenseBonus

def AnimatePrint(string: str):
    for char in string:
        print(char, end="")
        time.sleep(0.03)

def inventory():
    print("""
    1. Stäng inventory
    2. Val av föremål     
    """)
    val1 = input("Val: ")
    if val1 == "1":
        spel()
    elif val1 == "2":
       print("")
       val_av_föremål = input() 


def showCredits():
    pass

def start():
    print("1. Starta äventyret")
    print("2. Credits")
    print("3. Avsluta äventyret")
    var = input("Ditt val:")
    if var == "1":
        spel()
    elif var == "2":
        credit()
    elif var == "3":
        exit()
    else:
        print("Inte ett giltigt val!")
start()

def monster():
    monsterstrength = rand.int(4, 10)
    return monsterstrength

def kista():
    itemname = ["svärd", "sköld", "hjälm", "kängor", "kniv", "pilbåge", "gevär", "handgranat"]
    itemselect = rand.int(0, 7)
    itemname[itemselect]

    strength_bonus = rand.int(1, 10)

    
    
def fälla():
    pass



def room():
    var = rand.int(1, 3)
    if var == 1:
        pass
    elif var == 2:
        pass
    elif var == 3:
        pass
    else:
        pass

def AnimatePrint(string: str):
    for char in string:
        print(char, end=" ")
        time.sleep(40)


def spel():
    while level10 == False:
        print("1. Förråd")
        print("2. Statistic")
        print("3. Utforska")
        var = input("Ditt val:")
        if var == "1":
            inventory()
        elif var == "2":
            pass
        elif var == "3":
            print("Du utforskar labyrinten...")
            time.sleep(100)
            print("Du påkommer tre dörrar. Vilken dörr väljer du?")
            #Lägg till ASCII konst för dörrar
            var = input("Ditt val: ")
            room()
        else:
            pass