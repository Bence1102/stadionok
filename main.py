from Stadion import Stadion
import fajlbeolvasas
import feladatok
stadionok=fajlbeolvasas.beolvas("stadionok.txt",[])
for i in range(0,len(stadionok),1):
    """print(stadionok[i])"""

print(f"Első stadion neve: {stadionok[0]}")

feladat1=feladatok.new_yorki_stadionok(stadionok)
print(f"A New Yorki stadionok száma: {feladat1}")

feladat0=feladatok.osszes_stadion(stadionok)
print(f"Az összes stadion száma: {feladat0}")

feladat2=feladatok.osszes_csapat(stadionok)
print(f"Az összes csapat száma: {feladat2}")


#feladat3=feladatok.lista_1900_elott(stadionok)
#print(f"Az stadionok amik 1900-01-01 előtt : {feladat3}")

feladat4=feladatok.ketezer(stadionok)
print(f"Azoknak a stadionoknak amelyikekben nem volt 2000-óta mérkőzésének a száma : {feladat4}")



feladat5=feladatok.buffalo(stadionok)
print(f"Hány csapat játszott Buffaloban: {feladat5}")