import time
import random
from os import system
level10 = False

class player():
    def __init__(self, strength, hp, inventory, level):
        self.strength = strength
        self.hp = hp
        self.inventory = []
        self.level = level

class Item():
    """Ja tack"""
    def __init__(self, itemName, itemDescription, strengthBonus, healthBonus, defenseBonus):
        self.itemName = itemName
        self.itemDescription = itemDescription
        self.strengthBonus = strengthBonus
        self.healthBonus = healthBonus
        self.defenseBonus = defenseBonus

def AnimatePrint(string: str):
    """Skriver ut bokstäver med en tidsenhets mellanrum"""
    for char in string:
        print(char, end="")
        time.sleep(.03)
    print()

def clearConsole():
    system("cls || clear")

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
    AnimatePrint("""1. Starta äventyret\n2. Credits\n3. Avsluta äventyret""")
    var = input("Ditt val:")
    if var == "1":
        spel()
    elif var == "2":
        showCredits()
    elif var == "3":
        exit()
    else:
        print("Inte ett giltigt val!")
start()

def monster():
    monsterstrength = random.int(4, 10)
    return monsterstrength

def kista():
    itemNames = ["svärd", "sköld", "hjälm", "kängor", "kniv", "pilbåge", "gevär", "handgranat"]
    selectedItem = random.randint(0, len(itemNames))
    itemName = itemNames[selectedItem]

    item = Item(itemName, None, random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
    
def fälla():
    pass

def room():
    var = random.int(1, 3)
    if var == 1:
        pass
    elif var == 2:
        pass
    elif var == 3:
        pass
    else:
        pass

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