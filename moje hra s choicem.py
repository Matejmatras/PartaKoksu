def uvod():
    print("Venku prší a ty hledáš přístřešek.")
    print("Malá jeskyně. (vypadá jako medvědí nora)")

def jeskyne():
    print("Vlezl jsi do jeskyně. Je tu zima ale aspoň máš krytí před deštěm.")
    volba =  input("Vlezl jsi do vnitř a narazil na medvěda. Co uděláš? [1 - Nebudeš dělat prutké pohyby a pomalu zacouváš ven?, 2 - Otočíš se a začneš co nejrychleji utíkat]")
    if volba == "1":
        print("Medvěd na tebe kouká a vypadá jak kdyby neměl zájem. (Dneska máš štěstí nemá na tebe chuť ani náladu. Utekl jsi.)")

        return 0
    elif volba == "2":
        print("Prutce sebou trhneš a začneš utíkat. Medvěda si vylekal který tě pak po chvíli dohnal a roztrhal na kusy. (Zemřel jsi.)")
        return -1
        
    if random.randint(1, 2) == 1:
        print("")
    