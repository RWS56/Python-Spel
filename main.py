import time
import random
from os import system
import sys
import asciiart
from asciiart import *

class Player():
    """
    En klass för spelaren\n
    Innehållande funktioner:\n
    
    addToInventory(self, item)\n
    removeFromInventory(self, indexPlusOne)\n
    showInventory(self)\n
    ShowInventorykista (specifikt för kista() funktionen)\n
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
        
    def bonus(self, status, itemPosInInventory):
        item: Item = self.inventory[itemPosInInventory]
        if status == True:
            self.strength += item.strengthBonus
            self.hp += item.defenseBonus
            self.strength += item.healthBonus
        elif status == False:
            self.strength -= item.strengthBonus
            self.hp -= item.defenseBonus
            self.strength -= item.healthBonus
        
    
    def addToInventory(self, item):
        if len(self.inventory) >= 5:
            animatedPrint("Ditt förråd är fullt...")
        else:
            self.inventory.append(item)
            animatedPrint(f"{item.itemName} är tillagt i ditt förråd!")
    
    def removeFromInventory(self, indexPlusOne):
        if len(self.inventory) == 0:
            animatedPrint("Du har inga items att ta bort :(")
        else:
            animatedPrint(f"Du tog bort{self.inventory[indexPlusOne - 1].itemName}!\n Tryck valfri tangent för att gå tillbaka.") #La till så att man ser vad som blev borttagget ur inventory
            input()
            self.bonus(False, indexPlusOne - 1)
            self.inventory.pop(int(indexPlusOne) - 1)
            self.showInventory()
    
    def showInventory(self, deleteitems = True,):
        clearConsole()
        if deleteitems == True:
            if len(self.inventory) == 0:
                animatedPrint("Du har inga items :(")
                animatedPrint("Tryck på valfri tangent för att gå tillbaka.")
                input()
                spel(self)
            else:
                animatedPrint("Förråd:")
                i = 1
                for item in self.inventory:
                    animatedPrint(f"[{i}]{item.itemName} ", False) #Eventuellt sätt newLine till false
                    i += 1
                animatedPrint("\n1. Gå tillbaka\n2. Se Item\n")
                animatedPrint("Ditt val: ", False)
                var = input()
                clearConsole()
                if var == "1":
                    spel(self)
                elif var == "2":
                    for item in self.inventory:
                        animatedPrint(f"[{i}]{item.itemName}\n", False) #Eventuellt sätt newLine till false
                    i += 1
                    animatedPrint(f"Vilket Item (1 till {len(self.inventory)}): ", False)
                    var = int(input())
                    clearConsole()
                    föremål : Item = self.inventory[var-1]
                    self.showInventory(False)
                    animatedPrint("\n1. Radera \n2. Visa egenskaper\n3. Pårusta/Avrusta:", False)
                    val = input()
                    if val == "1":
                        self.removeFromInventory(var)
                    elif val == "2":
                        föremål.displayItem()
                        animatedPrint("Klicka på retur för att fortsätta \n", False)
                        input("")
                        clearConsole()
                        self.showInventory()
                    elif val == "3":
                        if föremål.equipped == True:
                            föremål.equipped = False
                            animatedPrint(f"{föremål.itemName} är avrustad.")
                            self.bonus(False, var-1)
                        elif föremål.equipped == False:
                            föremål.equipped = True
                            animatedPrint(f"{föremål.itemName} är pårustad.")
                            self.bonus(True, var-1)
        else:
            if len(self.inventory) == 0:
                animatedPrint("Du har inga items :(")
            else:
                animatedPrint("Förråd:")
                i = 1
                for item in self.inventory:
                    animatedPrint(f"[{i}]{item.itemName} ", False) #Eventuellt sätt newLine till false
                    i += 1
            
    def showStats(self):
        animatedPrint(f"[Current Player] {self.playerName}")
        animatedPrint(f"[HP] {self.hp} [STR] {self.strength} [LVL] {self.level}")
        animatedPrint("Klicka på enter för att gå tillbaka", False)
        input()
        spel(self)
    
    def takeDamage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            animatedPrint("Ditt HP blev till 0!")
            lose()
        else:
            animatedPrint(f"Du tog {damage} skada...")
            animatedPrint(f"Du har {self.hp} hp kvar...")
    
    def Levelup(self, level):
        animatedPrint(f"Du gick upp i level (+{level})")
        
        self.level += level
        if self.level >= 10:
            win()
            
    def trap(self):
        animatedPrint("Ånej! En fälla!!! ඞඞඞඞඞඞඞඞඞඞඞඞඞඞ")
        time.sleep(0.5)
        trapDamage = random.randint(1+self.level, 7*(1+self.level))
        self.takeDamage(trapDamage)
        animatedPrint("Klicka på enter för att fortsätta")
        input()
        spel(self)
    
    def kista(self):
        generateditem: Item = generateItem()
        animatedPrint(f"Du hittade {generateditem.itemName}! Vill du behålla den?")
        animatedPrint("y/n ", newLine=False)
        var = input()
        if var == "y":
            if len(self.inventory) < 5:
                self.addToInventory(generateditem)
            else:
                animatedPrint("Ditt Inventory är fullt! Vill du kasta bort ett Item?", newLine=False)
                var = input()
                if var == "Nej":
                    animatedPrint("Välj bort ett Item att kasta: ", newLine=False)
                    self.showInventory(deleteitems=False)
                    var = input()
                    self.removeFromInventory(var)           
        elif var == "n":
            pass
        
        spel(self)
            
        
    def monster(self): #Skapar ett monster med xyz damage och tillkallar takedamage
        clearConsole()
        animatedPrint("Du stöter på ett monster!")
        print(sus)
        monsterstrength = random.randint(3, 10)
        if monsterstrength > self.strength:
            self.takeDamage(monsterstrength)
        elif monsterstrength < self.strength:
            animatedPrint("Du dödade monstret!")
            time.sleep(1)
            levelsToUp = round((monsterstrength**2)/(4*monsterstrength))
            self.Levelup(levelsToUp)
            animatedPrint("Klicka på retur för att fortsätta ", False)
            input("")
        else:
            animatedPrint("Du och monstret var lika starka så ingenting hände!")
            
        spel(self)
        
class Item():
    """
    En klass för att hantera items.\n
    Varje item har ett namn, beskrivning, strengthBonus, healthBonus och defenseBonus.\n
    """
    
    def __init__(self, itemName, itemDescription, strengthBonus, healthBonus, defenseBonus, equipped):
        self.itemName = itemName
        self.itemDescription = itemDescription
        self.strengthBonus = strengthBonus
        self.healthBonus = healthBonus
        self.defenseBonus = defenseBonus
        self.equipped = equipped
        
    def displayItem(self):
        animatedPrint(f"{self.itemName}: {self.itemDescription}, [STR]{self.strengthBonus}, [HP]{self.healthBonus}, [DEF]{self.defenseBonus}")

def animatedPrint(string: str, newLine = True, sleepTime = 0.03):
    """
    Skriver ut inparametern strings enskilda bokstäver med en tidsenhets mellanrum\n
    New line bestämmer hurvida texten skall sluta med att en ny rad(\\n) ska printas. Är default True.\n
    Sleeptime är den tid som går mellan varje enskild bokstavs utskrivning
    
    ඞඞඞඞඞNOTERA!!!! Att newline skall vara false om en input skall tas direkt efteråt.ඞඞඞඞඞ
    """
    for char in string:
        print(char, end="", flush=True)
        #sys.stdout.write(char) ###Gammla <<<<
        #sys.stdout.flush()
        time.sleep(sleepTime)
    if newLine:
        print()

def clearConsole():
    """
    Städar upp lite skräp i konsolrutan
    """
    system("cls || clear") # Notera att endast cls antagligen behövs

def lose():
    print(f"Du förlorade!\n {asciiart.sus}\n Vill du spela igen?\n Ja/Nej")
    animatedPrint("Ditt val: ", newLine = False)
    while True:
        val = input()
        try:
            if val == "ja":
                start()
            elif val == "nej":
                exit()
        except TypeError as error:
            animatedPrint("Inte ett giltigt val!")
        
def win():
    clearConsole()
    animatedPrint("Du vann!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    animatedPrint("Klicka på retur för att återgå till menyn ", False)
    input("")
    start()
    
    
    
def showCredits():
    clearConsole()
    animatedPrint("Skapat av: Sarah, Ruben, Ye")
    animatedPrint("Tryck valfri tangent för att återvända")
    input()
    start()

def generateItem():
    itemModifier = ["EJ tillräcklig", "Lagom", "Tillräckligt", "Pristin"]
    itemNames = ["svärd", "sköld", "hjälm", "kängor", "kniv", "pilbåge", "gevär", "handgranat", "spjut"] #kanske lägg till hp potion
    selectedItem = random.randint(0, len(itemNames) - 1)
    selectedModifier = random.randint(0, len(itemModifier) - 1)
    itemName = f"{itemModifier[selectedModifier]} {itemNames[selectedItem]}"

    item = Item(itemName, None, random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), False)
    return item

def room(currentPlayer: Player):
    clearConsole()
    animatedPrint("Tre dörrar, 1, 2, 3,")
    animatedPrint("Välj en: " , False)
    input("")
    clearConsole()
    var = random.randint(0, 2) 
    if var == 0:
        currentPlayer.kista()
        pass
    elif var == 1:
        currentPlayer.monster()
        pass
    elif var == 2:
        currentPlayer.trap()
        pass
    else:
        animatedPrint("Hoppsan! Något gick fel!")
        spel(currentPlayer)
        pass
    
def spel(currentPlayer: Player):
    clearConsole()
    animatedPrint("1. Förråd")
    animatedPrint("2. Statistik")
    animatedPrint("3. Utforska")
    animatedPrint("Ditt val: ", False)
    var = input()
    if var == "1":
        currentPlayer.showInventory()
        animatedPrint("1. Stäng inventory\n2. Välj föremål", False)
        var = input()
        if var == "1":
            spel(currentPlayer)
        elif var == "2":
            #animatedPrint(self.inventory)
            currentPlayer.showInventory(deleteitems=True)          
    elif var == "2":
        currentPlayer.showStats()
    elif var == "3":
        animatedPrint("Du utforskar labyrinten...")
        time.sleep(1)
        #Lägg till ASCII konst för dörrar
        room(currentPlayer)
    else:
        spel(currentPlayer)

#Början av spelet
def start():
    clearConsole()
    animatedPrint("""1. Starta äventyret\n2. Credits\n3. Avsluta äventyret""")
    animatedPrint("Ditt val: ", False)
    var = input()
    try:
        if var == "1":
            spel(spelare)
        elif var == "2":
            showCredits()
        elif var == "3":
            exit()
        else:
            start()
    except TypeError as error:
        print("Inte ett giltigt val!")

#testspelare (avmarkea kommentar för att testa)        
spelare = Player("MArre Lomme", 0, 15, 0)

start()