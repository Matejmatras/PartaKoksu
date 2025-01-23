import random

def krcma():
    print("\nNarazil jsi na Krčmu u Šeptajícího lohu, kde lesní šepot pronikal do každé skuliny. Uvnitř seděli tichí lidé, oči jim zářily tajemstvím. Paní domácí ti jen naznačila: Ticho tady neklame.")
    volba = input("Stojíš u krčmy. Co uděláš? (1 = Přisedneš k místním, 2 = Vydáš se dál do lesa): ")
    
    if volba == "1":
        print("\nTiše si sedneš k místním. Oči všech se na tebe zaměřují, ale nikdo nic neříká. Cítíš, že jejich ticho je plné nevyřčených tajemství. Paní domáci ti donesla pivo.")
        pivo()
    elif volba == "2":
        print("\nVydáš se do lesa. Stíny stromů tě sledují, vzduch je chladný a napjatý. Každý krok je jako tichý souhlas s neviditelným pozváním, které tě vede dál.")
        
        if random.randint(1, 2) == 1:
            print("\nPo několika krocích se před tebou objeví podivná postava. Zastavíš se, ale ona ti jen tiše přikývne a pokračuje dál. Po chvíli si našel stopy.")
        else:
            print("\nNáhle se vzduch ochladí a les kolem tebe ztichne. Máš pocit, že tě něco sleduje z temného rohu lesa, ale když se otočíš, nic tam není. Po chvíli si našel stopy.")
        stopy()
    else:
        print("\nNeplatná volba, paní domácí tě zmlátila a nikdo tvoje tělo už nikdy nenašel. Hra končí.")

def pivo():
    print("\nNapil ses piva, získáváš 2 body")
    return 2


def napit_se_znovu():
    volba = input("\n Chceš se napít ještě jednoho piva? (1= Ano, 2 = Ne):")
    if volba =="1":
        print("\nNapil ses dalšího piva. Už máš dost, motá se ti hlava. Ztrácíš 1 bod.")
    return -1
krcma()

napit_se_znovu()



    
def stopy():
    print("\nRozhodl ses prozkoumat stopy, které vedou dál do lesa. Každý krok je obklopený tichým šepotem, jakoby samotný les ti něco naznačoval.")
    volba = input("Co uděláš? (1 = Pokračuješ sledovat stopy, 2 = Zastavíš se a podíváš se kolem): ")
    
    if volba == "1":
        print("\nSleduješ stopy dál, když náhle narazíš na ztracenou vesnici. Domy jsou zchátralé a v oknech se něco mihne. Máš pocit, že nejsi sám.")
        vesnice()
    elif volba == "2":
        print("\nZastavíš se a rozhlédneš se. V dálce se objeví temná silueta, která se pomalu přibližuje. Srdce ti začíná bušit.")
        silueta()
    else:
        print("\nNeplatná volba, paní domácí tě zmlátila a nikdo tvoje tělo už nikdy nenašel. Hra končí.")

def vesnice():
    volba = input("\nVstoupíš do ztracené vesnice? (1 = Vstoupíš do jednoho z domů, 2 = Prozkoumáš okolí vesnice): ")
    
    if volba == "1":
        print("\nVstoupíš do domu. V jeho vnitřku je chladno a prázdno. Všude jsou podivné symboly a vzduch je těžký, jakoby někdo tu dlouho nebyl. Získal si 1 bod.")
        return 1
    elif volba == "2":
        print("\nProzkoumáš vesnici a objevíš starý hřbitov. Na některých náhrobcích jsou zcela neznámé symboly a některé hroby jsou čerstvé.")
    else:
        print("\nNeplatná volba, Stal si se nezvěstným. Hra končí.")
    silueta()

def silueta():
    volba = input("\nSilueta se blíží. Co uděláš? (1 = Přistoupíš k siluetě, 2 = Skrýváš se a čekáš): ")
    
    if volba == "1":
        print("\nPřistoupíš k siluetě, která se ukáže být starým poutníkem. Oči má plné smutku, ale říká: 'Vítej, dám ti 3 body, když mi doneseš pivo.'")
        volba = input("\nDoneseš mu pivo nebo ne (1 = Ano, 2 = Ne):")
        if volba == "1":
            print("\nVracíš se po svých stopách do Krčmy u Šeptajícího lohu, vzal si pivo a neseš ho starému poutníkovi.")
            return 3
        elif volba == "2":
            print("\nVykašlal ses na poutníka a ten na tebe vyslal kletbu Rudého Měsíce, budeš se měnit ve vlkodlaka.")
        else: 
            print("\nNechal ses pohltit starým poutníkem, když ses na něj díval až moc dlouho.")
    elif volba == "2":
        print("\nSkrýváš se za stromem. Silueta tě míjí, ale tvůj strach roste. Když se otočíš, zjistíš, že tvé místo už není bezpečné. Začneš utíkat a najednou si vyšel z lesa")
    else:
        print("\nUž si přestal bavit starého poutníka, vyslal na tebe všechny své kouzla a kletby. Umřel jsi a jsi nezvěstný.")

krcma()

