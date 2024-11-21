from datetime import datetime
def new_yorki_stadionok(stadion_lista):
    db=0
    for i in range(0,len(stadion_lista),1):
        if stadion_lista[i].varos == "New York":
            db+=1
    return db


def osszes_stadion(stadion_lista):
    return len(stadion_lista)


def osszes_csapat(stadion_lista):
    db=0
    for i in range(0,len(stadion_lista),1):
        db+=stadion_lista[i].csapatok_szama
    return db



def lista_1900_elott(stadion_lista):
    eredmeny = []
    for stadion in stadion_lista:
        if stadion.elso_merk.strftime("%Y-%m-%d") < "1900-01-01":
            eredmeny.append(stadion)
    return eredmeny













def buffalo(stadio_lista):
    buffalo_db=0
    for i in range(0,len(stadio_lista),1):
        if stadio_lista[i].varos== "Buffalo":
            buffalo_db+=1
    return buffalo_db








