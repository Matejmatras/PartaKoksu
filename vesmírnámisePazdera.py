
import random
 
def uvod():
    print("Nacházíš se v opuštěné vesmírné stanici a máš tři možnosti.")
    print("1. Prozkoumat opuštěné UFO.")
    print("2. Jít do hangáru.")
    print("3. Jít k hlavní velitelské stanici.")
 
def UFO():
    print("\nVydal ses do opuštěného UFA. Všude blikají kontrolky a slyšíš divné zvuky.")
    volba = input("Vidíš ovládání UFA. Co uděláš? (1 = zkusit ho nastartovat, 2 = ignorovat ho a pokračovat dál): ")
    if volba == "1":
        if random.randint(1, 2) == 1:
            print("Nastarotvání UFA bylo úspěšné! Získáváš 2 body.")
            return 2
        else:
            print("Povedlo se ti uletět ze stanice. Získáváš 1 bod.")
            return 1
    elif volba == "2":
        print("Ignoroval jsi ovládání UFA a pokračoval dál. Ztrácíš bod.")
        return -1
    else:
        print("Neplatná volba! Šel si dál a našli tě mimozemšťani. Hra končí.")
        return -1
 
def hangar():
    print("\nVydal ses do hangáru. Vidíš odstavenou kosmickou loď, ale také slyšíš podivné skřípání.")
    volba = input("Chceš prozkoumat loď nebo se schovat? (1 = prozkoumat, 2 = schovat se): ")
    if volba == "1":
        if random.randint(1, 2) == 1:
            print("Dostal ses potají do lodi. Získáváš 2 body.")
            return 2
        else:
            volba = input("Kouknout se do skříně? (E = ano): ")
            print("Našel si schovanou zbraň na sebeobranu. Získáváš 2 body.")
            return 2
    elif volba == "2":
        print("Schoval ses za boxy a počkal, dokud nebude vzduch čistý. Získáváš 1 bod.")
        return 1
    else:
        print("Neplatná volba! Zůstal jsi stát na místě a mimozemšťani tě objevili. Hra končí.")
        return -1
 
def stanice():
    print("\nRozhodl ses jít do hlavní velitelské stanice. Nikde nikdo není, až na alarm.")
    volba = input("Vidíš hlavní velitelskou stanici. Co uděláš? (1 = hacknu dveře a vypnu alarm, 2 = hledat jinou cestu): ")
    if volba == "1":
        if random.randint(1, 2) == 1:
            print("Hacknul si bez problémů dveře a vypnul alarm. Získáváš 2 body. ")
            return 2
        else:
            print("Nepovedlo se ti vypnout alarm a mimozemšťani tě objevili")
            return -1
    elif volba == "2":
        print("Šel si jinou cestou a našel si šachtu, která vede do stanice. Získáváš 1 bod.")
        return 1
    else:
        print("Neplatná volba! Šel si dál a mimozemšťani tě objevili. Hra končí.")
        return -1
 
def hlavni():
    uvod()
    volba = input("Kam se vydáš? (1 = UFO, 2 = hangár, 3 = stanice): ")
    if volba == "1":
        vysledek = UFO()
    elif volba == "2":
        vysledek = hangar()
    elif volba == "3":
        vysledek = stanice()
    else:
        print("Neplatná volba! Ztratil jsi příležitost a hra končí.")
        return
 
    if vysledek > 0:
        print("Gratulujeme, úspěšně jsi zvládl svou vesmírnou misi!")
    else:
        print("Bohužel, tvoje mise skončila neúspěchem.")
 
hlavni()
