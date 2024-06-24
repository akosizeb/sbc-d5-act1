import os
os.system('cls')

#CORRUPT LTO

#queue
def naa():
    print(weapon)
    print("\nRemoved weapon: ", weapon[0])
    weapon.pop(0)
    print(weapon)
#stack
def wala():
    print(weapon)
    print("\nRemoved weapon: ", weapon[-1])
    weapon.pop(-1)
    print(weapon)

weapon = []

for w in range(5):
    w = input("\nEnter a Weapon : ") 
    weapon.append(w)

print("\nWeapons: ", weapon)

for c in range(len(weapon)):
    weapon_status = input("\nNaa ang Dealer? naa/wala: ")
    weapon_status.lower

    if weapon_status == "naa":
        naa()

    elif weapon_status == "wala":
        wala()

    else:
        print("Mali imong ge TYPE! taronga pag TYPE!!!")
        break