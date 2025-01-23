import random

def uvod():
    print("Stojíš na rozcestí a máš tři možnosti.")
    print("1. Jít do hor.")
    print("2. Vyrazit k hospodě.")
    print("3. Pochodovat k hotelu.")

def hory():
    print("\nVydal ses do hor. Je tu zima a slyšíš podivné zvuky, jako by něco padalo ze skal.")
    volba = input("Náhle se na tebe řítí kámen! Co uděláš? (1 = rychle uhnout, 2 = stát na místě): ")
    if volba == "1":
        print("Uhnul jsi právě včas a kámen tě minul! Přežil jsi a pokračuješ dál.")
        return 1
    elif volba == "2":
        if random.randint(1, 2) == 1:
            print("Měl jsi štěstí! Kámen spadl těsně vedle tebe, ale přišel jsi o batoh.")
            return 1
        else:
            print("Bohužel, kámen tě trefil. Hra končí.")
            return -1
    else:
        print("Neplatná volba! Kvůli nerozhodnosti tě kámen zasáhl. Hra končí.")
        return -1

def hospoda():
    print("\nVydal ses k hospodě. Uvnitř je útulno a místní ti nabízejí informace o okolí.")
    volba = input("Přijmeš jejich nabídku na pivo? (1 = ano, 2 = ne): ")
    if volba == "1":
        print("Pivo bylo dobré, ale nyní jsi trochu zmatený a ztratil jsi směr.")
        return -1
    elif volba == "2":
        print("Odmítl jsi pivo a místo toho jsi získal cenné informace o bezpečné cestě dál.")
        return 1
    else:
        print("Neplatná volba! Místní tě ignorují a nic jsi nezjistil.")
        return -1

def hotel():
    print("\nRozhodl ses jít k hotelu. Cesta je pohodlná, ale začíná se stmívat.")
    volba = input("Pokračuješ do hotelu nebo se vrátíš? (1 = pokračovat, 2 = vrátit se): ")
    if volba == "1":
        print("Dorazil jsi do hotelu včas a získal jsi úkryt na noc. Dobrá práce!")
        return 2
    elif volba == "2":
        print("Rozhodl ses vrátit zpět, ale cestou jsi ztratil energii a nic nezískal.")
        return -1
    else:
        print("Neplatná volba! Zůstal jsi nerozhodně stát a začalo pršet. Hra končí.")
        return -1

def hlavni():
    skore = 0
    while True:
        uvod()
        volba = input("Kam se vydáš? (1 = hory, 2 = hospoda, 3 = hotel): ")
        if volba == "1":
            vysledek = hory()
        elif volba == "2":
            vysledek = hospoda()
        elif volba == "3":
            vysledek = hotel()
        else:
            print("Neplatná volba! Ztratil jsi příležitost a hra končí.")
            break

        if vysledek > 0:
            skore += vysledek
            print(f"Pokračuješ dál! Tvoje aktuální skóre je: {skore}.")
        else:
            print(f"Bohužel, tvoje cesta skončila. Tvé konečné skóre je: {skore}.")
            break

hlavni()