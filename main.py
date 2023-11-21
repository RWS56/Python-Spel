
def spel():
    pass

def credit():
    pass

def start():
    print("1. Starta äventyret")
    print("2. Credits")
    print("3. Avsluta äventyret")
    var = input("Ditt val:")
    try:
        if var == "1":
            spel()
        elif var == "2":
            credit()
        elif var == "3":
            exit()
    except:
        print("Du skrev inte in ett giltigt alternativ")

start()