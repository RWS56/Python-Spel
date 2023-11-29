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
            self.inventory.pop(int(indexPlusOne) - 1)
            self.showInventory()
    
    def showInventory(self, deleteitems = True,):
        clearConsole()
        if deleteitems == True:
            if len(self.inventory) == 0:
                animatedPrint("Du har inga items :(")
                animatedPrint("Tryck på valfri tangent för att gå tillbaka.")
                input()
                spel()
            else:
                animatedPrint("Förråd:")
                i = 1
                for item in self.inventory:
                    animatedPrint(f"[{i}]{item.itemName} ", False) #Eventuellt sätt newLine till false
                    i += 1
                animatedPrint("1. Gå tillbaka\n2. Se Item")
                animatedPrint("Ditt val: ", False)
                var = input()
                if var == "1":
                    spel()
                elif var == "2":
                    animatedPrint("Vilket Item (1 till 5):", False)
                    var == int(input())
                    föremål = self.inventory[var-1]
                    animatedPrint("1. Radera \n2. Visa egenskaper:", False)
                    val = input()
                    if val == "1":
                        self.removeFromInventory(var)
                    elif val == "2":
                        animatedPrint(föremål)
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
        animatedPrint(f"[Current Player]{self.playerName}")
        animatedPrint(f"[HP]{self.hp} [STR]{self.strength} [LVL]{self.level}")
        animatedPrint("Klicka på enter för att gå tillbaka", False)
        input()
        spel()
    
    def takeDamage(self, damage):
        animatedPrint(f"Du tog {damage} skada...")
        animatedPrint(f"Du har {self.hp} hp kvar...")
        self.hp -= damage
        if self.hp <= 0:
            animatedPrint("Ditt HP blev till 0!")
            lose()
    
    def Levelup(self, level):
        self.level += level
        if self.level >= 10:
            win()
            
    def trap(self):
        animatedPrint("Ånej! En fälla!!! ඞඞඞඞඞඞඞඞඞඞඞඞඞඞ")
        trapDamage = random.randint(1+self.level, 7*(1+self.level))
        self.hp -= trapDamage
        animatedPrint(f"Du tog {trapDamage} skada!")
        spel()
    
    def kista(self):
        generateditem = generateItem()
        self.addToInventory(self, generateditem)
        animatedPrint(f"Du hittade {generateditem.itemName}! Vill du behålla den?")
        animatedPrint("Ja/Nej", newLine=False)
        var = input()
        if var == "Ja":
            if len(self.inventory) < 5:
                self.addToInventory(self, generateditem)
            else:
                animatedPrint("Ditt Inventory är fullt! Vill du kasta bort ett Item?", newLine=False)
                var = input()
                if var == "Nej":
                    animatedPrint("Välj bort ett Item att kasta: ", newLine=False)
                    self.showInventory(deleteitems=False)
                    var = input()
                    self.removeFromInventory(var)
                      
        elif var == "Nej":
            pass
        
    def monster(self): #Skapar ett monster med xyz damage och tillkallar takedamage
        clearConsole()
        animatedPrint("Du stöter på ett monster!\n ඞ")
        monsterstrength = random.int(3, 10)
        if monsterstrength > self.strength:
            self.takeDamage(monsterstrength)
        elif monsterstrength < self.strength:
            animatedPrint("Du dödade monstret!")
            var = 1
            self.Levelup(var)
        else:
            animatedPrint("Du och monstret var lika starka så ingenting hände!")
        
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

def animatedPrint(string: str, newLine = True, sleepTime = 0.03):
    """
    Skriver ut inparametern strings enskilda bokstäver med en tidsenhets mellanrum\n
    New line bestämmer hurvida texten skall sluta med att en ny rad(\\n) ska printas. Är default True.\n
    Sleeptime är den tid som går mellan varje enskild bokstavs utskrivning
    
    ඞඞඞඞඞNOTERA!!!! Att newline skall vara false om en input skall tas direkt efteråt.ඞඞඞඞඞ
    """
    for char in string:
        #print(char, end="")
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(sleepTime)
    if newLine:
        print()

def clearConsole():
    """
    Städar upp lite skräp i konsolrutan
    """
    system("cls || clear") # Notera att endast cls antagligen behövs

def lose():
    animatedPrint(f"Du förlorade!\n {asciiart.sus}\n Vill du spela igen?\n Ja/Nej")
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
    
def showCredits():
    clearConsole()
    animatedPrint("Skapad av: Sarah, Ruben, Ye")
    animatedPrint("Tryck valfri tangent för att återvända")
    input()
    start()

def generateItem():
    itemModifier = ["EJ tillräcklig", "Lagom", "Tillräckligt", "Pristin"]
    itemNames = ["svärd", "sköld", "hjälm", "kängor", "kniv", "pilbåge", "gevär", "handgranat", "spjut", "Hälsodryck"]
    selectedItem = random.randint(0, len(itemNames))
    selectedModifier = random.randint(0, len[itemModifier])
    itemNameJoin = selectedModifier + selectedItem
    itemName = itemNames[itemNameJoin]

    item = Item(itemName, None, random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
    return item

def room(currentPlayer):
    animatedPrint("Tre dörrar, 1, 2, 3,")
    animatedPrint("Välj en:" , False)
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
        spel()
        pass
    
def spel(currentPlayer: Player):
    
    animatedPrint("1. Förråd")
    animatedPrint("2. Statistik")
    animatedPrint("3. Utforska")
    animatedPrint("Ditt val: ", False)
    var = input()
    if var == "1":
        currentPlayer.showInventory()
        animatedPrint("1. Stäng inventory\n2. Välj föremål")
        var = input()
        if var == "1":
            spel()
        elif var == "2":
            #animatedPrint(self.inventory)
            animatedPrint("Välj föremål 1 till 5", False)
            var = int(input()) - 1
            currentPlayer.showInventory(deleteitems=True)
             
    elif var == "2":
        animatedPrint()
    elif var == "3":
        animatedPrint("Du utforskar labyrinten...")
        time.sleep(1)
        animatedPrint("Du påkommer tre dörrar. Vilken dörr väljer du?")
        #Lägg till ASCII konst för dörrar
        var = input("Ditt val: ", False)
        room(currentPlayer)
    else:
        pass
    
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
    except TypeError as error:
        print("Inte ett giltigt val!")

#testspelare (avmarkea kommentar för att testa)        
spelare = Player("hej", 1, 1, 0)
spelare.addToInventory(Item("Svärd1", 1, 1, 1, 1))
spelare.addToInventory(Item("Svärd2", 1, 1, 1, 1))

#Startkommando för att sätta igång spelet (OBS MÅSTE ALLTID VARA SIST I KODEN!!!!!!)        
start()

#rubensTestSpelare = Player("Hej", 1, 1, 0)
#rubensTestSpelare.addToInventory(Item("Svärd1", 1, 1, 1, 1))
#rubensTestSpelare.addToInventory(Item("Svärd2", 1, 1, 1, 1))
#rubensTestSpelare.addToInventory(Item("Svärd7", 1, 1, 1, 1))
#rubensTestSpelare.addToInventory(Item("Svärd32", 1, 1, 1, 1))
#rubensTestSpelare.addToInventory(Item("Svärd27", 1, 1, 1, 1))
#rubensTestSpelare.showInventory()