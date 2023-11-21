import time
import random
level10 = False

def inventory():
    print("""
    1. Stäng inventory
    2. Val av föremål     
    """)
    val1 = input("Val: ")
    if val1 == "1":
        spel()
    elif val1 == "2":
        


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