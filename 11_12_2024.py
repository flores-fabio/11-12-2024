registro = {
"1": {"nome": "Mario", "cognome": "Rossi", "media": 4},
"2": {"nome": "Luigi", "cognome": "Verdi", "media": 6} ,
"3": {"nome": "Waluigi", "cognome": "Viola", "media": 8}
}

z = True

while z:
    print("1. Aggiungi studente")
    print("2. Visualizza registro")
    print("3. Modifica studente")
    print("4. Rimuovi studente")
    print("""
        5 per calcolare la media della classe
        6 per mostrare solo gli studenti con media >= 6
        7 per contare il numero di studenti
        8 per eliminare l'intero registro
        9 per creare e stampare due liste, una per gli studenti bocciati e una per gli studenti promossi.
            nella lista promossi ci saranno i cognomi degli studenti con media >=6.""")
    print("0. Esci")

    scelta = int(input("Fai una scelta:"))
    if (scelta ==1):
        id = 0
        for chiave in registro.keys():
            id = int(chiave)
        id += 1
        id = str(id)
        nome = input("Inserisci il nome dello studente: ")
        cognome = input("Inserisci il il cognome dello studente: ")
        media = int(input("Inserisci la media dello studente: "))
        registro[id] ={"nome" : nome, "cognome": cognome, "media":  media}
    
    elif (scelta ==2):
        for chiave, valore in registro.items():
            print(chiave + ": " + str(valore))
            print()

    elif (scelta ==3):
        x = input("Quale studente vuoi modificare: ")
        for chiave, valore in registro.items():
            if valore["nome"] == x:
                valore["media"] = int(input("Inserisci un numero per cambiare la media dello studente: "))

    elif (scelta ==4):
        y = input("Quale studente vuoi eliminare dal registro: ")
        if y in registro.keys():
            registro.pop(y)
        else: 
            print("ID inserito non esiste")
    elif (scelta ==0):
        z = False
   
    elif (scelta ==5):
        l = len(registro)
        somma = 0
        for valore in registro.values():
            somma += valore["media"]
        media = somma / l
        print(media)

    elif (scelta ==6):
        for valore in registro.values():
            if valore["media"] >= 6:
                print(valore)
    
    elif (scelta ==7):
        print(len(registro)) #conta quanti studenti ci sono nel registro

    elif (scelta ==8):
        del registro
    
    elif (scelta ==9):
        promossi = []
        bocciati = []
        for valore in registro.values():
            if valore["media"] >= 6:
                promossi.append(valore["cognome"])
            else:
                bocciati.append(valore["cognome"])
        print("promossi"+ str(promossi))
        print("bocciati"+ str(bocciati))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    else:
        print("Non esiste questa opzione: ")