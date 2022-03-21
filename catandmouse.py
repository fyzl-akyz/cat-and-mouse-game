import random
import time
number = random.randint(1,200)
while True:
    input("Welcome to Cat And Mouse Game \nRules are very basic.If you see Meuse,than  answer the question.\nIf you wanna play press Enter")
    for x in range (0,50) :
        print("Mouse,   Mouse,  Mouse,  Mouse,  Mouse")
        time.sleep(0.5)
        if(number == x ):
            print("Meuse,   Mouse,  Mouse,  Mouse,  Mouse")
    z = str(input("Did you see Meuse ? (yes (Y) / no (N))"))
    if( z == "Y"):
        if(number < x ):
            print("You win !")
        else: print("You lose ! ")
    elif (z =="N"):
        if (number >x):
            print("You win !")
        else: print("You lose !")