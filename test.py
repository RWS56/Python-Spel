"""

ETT DOKUMENT FÖR ATT SNABBT OCH ENKELT TESTA LITE KOD
PRINT > DEBUGGER == TRUE

"""

import time

def AnimatePrint(string: str):
    for char in string:
        print(char, end="")
        time.sleep(0.15)

AnimatePrint("""HEJSAN
             JAG
             HETER
             RUBEN!""")