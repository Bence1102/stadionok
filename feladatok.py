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
    for i in range(0,len(stadion_lista),1):
        if stadion_lista[i].utolso_merk < datetime.strftime("1900-01-01","%Y-%m-%d"):
            eredmeny.append(stadion_lista)
    return eredmeny



def ketezer(stadion_lista):
    ketezres:int=0
    for i in range (1,len(stadion_lista)):
        if stadion_lista[i].utolso_merk <datetime.strptime("2000-01-01","%Y-%m-%d"):
            ketezres+=1
    return ketezres









def buffalo(stadio_lista):
    buffalo_db=0
    for i in range(0,len(stadio_lista),1):
        if stadio_lista[i].varos== "Buffalo":
            buffalo_db+=1
    return buffalo_db








