# have fun playing jokenpô with your computer

import random as r

print("")
print("         LET'S PLAY JOKEMPÓ")
print("")
lista = [(1),(2),(3)]
print("[1] stone - [2] paper - [3] scissors")
print("=-"*18)
p = int(input('enter your option here: '))
randomm = r.choice(lista)
# pedra
if randomm == p:
    print("A TIE")
elif randomm == 1 and p == 2:
    print("you WON!")
elif randomm == 1 and p == 3:
    print("you LOST")
# papel
elif randomm == 2 and p == 3:
    print("you WON!")
elif randomm == 2 and p == 1:
    print("you LOST")
# tesoura
elif randomm == 3 and p == 2:
    print("you LOST")
elif randomm == 3 and p == 1:
    print("you WON!")
else:
    print("please enter only the numbers recommeded\nby the program")
print("")
