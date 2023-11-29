import time
import random
from os import system
level10 = False
import asciiart
from asciiart import *

class player():
    """
    En klass för spelaren\n
    Innehållande funktioner:\n
    
    addToInventory(self, item)\n
    removeFromInventory(self, indexPlusOne)\n
    showInventory(self)\n
    takeDamage(self, damage)\n
    Levelup(self, level)\n
    trap(self)\n
    kista(self)\n
    monster(self)\n
    """
    #Lägg till monster kill count??!?!?!?!?
    
    def __init__(self, playerName, strength, hp, level):
        self.playerName = playerName
        self.strength = strength
        self.hp = hp
        self.level = level
        self.inventory = []
    
    def addToInventory(self, item):
        if len(self.inventory) >= 5:
            AnimatePrint("Ditt inventory är fullt...")
        else:
            self.inventory.append(item)
            AnimatePrint(f"{item.itemName} är tillagt i ditt inventarie!")
    
    def removeFromInventory(self, indexPlusOne):
        if len(self.inventory) == 0:
            AnimatePrint("Du har inga items att ta bort :(")
        else:
            self.inventory.pop(indexPlusOne - 1)
    
    def showInventory(self):
        if len(self.inventory) == 0:
            AnimatePrint("Du har inga items :(")
        else:
            AnimatePrint("Inventory:")
            i = 1
            for item in self.inventory:
                AnimatePrint(f"[{i}]{item.itemName}") #Eventuellt sätt newLine till false
                i += 1
    
    def takeDamage(self, damage):
        AnimatePrint(f"Du tog {damage} skada...")
        AnimatePrint(f"Du har {self.hp} hp kvar...")
        self.hp -= damage
        if self.hp <= 0:
            AnimatePrint("Ditt HP blev till 0!")
            lose()
    
    def Levelup(self, level):
        self.level += level
        if self.level >= 10:
            win()
            
    def trap(self):
        AnimatePrint("Ånej! En fälla!!! ඞඞඞඞඞඞඞඞඞඞඞඞඞඞ")
        trapDamage = random.randint(1+self.level, 7*(1+self.level))
        self.hp -= trapDamage
        AnimatePrint(f"Du tog {trapDamage} skada!")
    
    def kista(self):
        generateditem = generateItem()
        item_name = generateditem.itemName
        self.addToInventory(self, generateditem)
        AnimatePrint(f"Du hittade {generateditem.itemName}! Vill du behålla den?")
        AnimatePrint("Ja/Nej", newLine=False)
        var = input()
        if var == "Ja":
            if len(self.inventory) < 5:
                self.addToInventory(self, generateditem)
            else:
                AnimatePrint("Ditt Inventory är fullt! Vill du kasta bort ett Item?", newLine=False)
                var = input()
                if var == "Nej":
                    AnimatePrint("Välj bort ett Item att kasta:")
                    self.showInventory()
                    var = input()
                    self.removeFromInventory(var)
                      
        elif var == "Nej":
            pass
        
    def monster(self): #Skapar ett monster med xyz damage och tillkallar takedamage
        clearConsole()
        AnimatePrint("Du stöter på ett monster!\n ඞ")
        monsterstrength = random.int(4, 10)
        self.takeDamage(monsterstrength)
        
class Item():
    """
    En klass för att hantera items.\n
    Varje item har ett namn, beskrivning, strengthBonus, healthBonus och defenseBonus.\n
    """
    
    def __init__(self, itemName, itemDescription, strengthBonus, healthBonus, defenseBonus):
        self.itemName = itemName
        self.itemDescription = itemDescription
        self.strengthBonus = strengthBonus
        self.healthBonus = healthBonus
        self.defenseBonus = defenseBonus

def AnimatePrint(string: str, newLine = True, sleepTime = 0.03):
    """
    Skriver ut inparametern strings enskilda bokstäver med en tidsenhets mellanrum\n
    New line bestämmer hurvida texten skall sluta med att en ny rad(\\n) ska printas. Är default True.\n
    Sleeptime är den tid som går mellan varje enskild bokstavs utskrivning
    
    ඞඞඞඞඞNOTERA!!!! Att newline skall vara false om en input skall tas direkt efteråt.ඞඞඞඞඞ
    """
    for char in string:
        print(char, end="")
        time.sleep(sleepTime)
    if newLine:
        print()

def clearConsole():
    """
    Städar upp lite skräp i konsolrutan
    """
    system("cls || clear") # Notera att endast cls antagligen behövs

def lose():
    AnimatePrint(f"Du förlorade!\n {sus}\n Vill du spela igen?\n Ja/Nej")
    AnimatePrint("Ditt val: ", newLine = False)
    while True:
        val = input()
        try:
            if val == "ja":
                start()
            elif val == "nej":
                exit()
        except TypeError as error:
            AnimatePrint("Inte ett giltigt val!")
        
def win():
    clearConsole()
    AnimatePrint("Du vann!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
def showCredits():
    AnimatePrint("Skapad av: Sarah, Ruben, Ye")




def generateItem():
    itemNames = ["svärd", "sköld", "hjälm", "kängor", "kniv", "pilbåge", "gevär", "handgranat", "spjut"]
    selectedItem = random.randint(0, len(itemNames))
    itemName = itemNames[selectedItem]

    item = Item(itemName, None, random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
    return item

def room():
    AnimatePrint("Tre dörrar, 1, 2, 3,")
    AnimatePrint("Välj en:" , False)
    var = random.randint(0, 2)
    rooms = []
    
def spel():
    
    AnimatePrint("1. Förråd")
    AnimatePrint("2. Statistik")
    AnimatePrint("3. Utforska")
    AnimatePrint("Ditt val: ", False)
    var = input()
    if var == "1":
        #player.showInventory(player1)
        AnimatePrint("1. Stäng inventory\n2. Välj föremål 1 till 5")
        var = input()
        if var == "1":
            spel()
        elif var == "2":
            #AnimatePrint(self.inventory)
            AnimatePrint()
                     
    elif var == "2":
        AnimatePrint()
    elif var == "3":
        AnimatePrint("Du utforskar labyrinten...")
        time.sleep(100)
        AnimatePrint("Du påkommer tre dörrar. Vilken dörr väljer du?")
        #Lägg till ASCII konst för dörrar
        var = input("Ditt val: ", False)
        room()
    else:
        pass§
    
#Början av spelet
def start():
    clearConsole()
    AnimatePrint("""1. Starta äventyret\n2. Credits\n3. Avsluta äventyret""")
    AnimatePrint("Ditt val: ", False)
    var = input()
    try:
        if var == "1":
            spel()
        elif var == "2":
            showCredits()
        elif var == "3":
            exit()
    except TypeError as error:
        print("Inte ett giltigt val!")

#testspelare (avmarkea kommentar för att testa)        
#spelare = player("hej", 1, 1, 0)        

#Startkommando för att sätta igång spelet (OBS MÅSTE ALLTID VARA SIST I KODEN!!!!!!)        
#start()

#rubensTestSpelare = player("Hej", 1, 1, 0)
#rubensTestSpelare.addToInventory(Item("Svärd1", 1, 1, 1, 1))
#rubensTestSpelare.addToInventory(Item("Svärd2", 1, 1, 1, 1))
#rubensTestSpelare.addToInventory(Item("Svärd7", 1, 1, 1, 1))
#rubensTestSpelare.addToInventory(Item("Svärd32", 1, 1, 1, 1))
#rubensTestSpelare.addToInventory(Item("Svärd27", 1, 1, 1, 1))
#rubensTestSpelare.showInventory()