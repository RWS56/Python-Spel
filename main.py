
level10 = False

def spel():
    while level10 == False:
        print("1. Förråd")
        print("2. Statistic")
        print("3. Utforska")
        var = input("Ditt val:")
        if var == "1":
            pass
        elif var == "2":
            pass
        elif var == "3":
            pass
        else:
            pass


def credit():
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