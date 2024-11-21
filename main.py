from Stadion import Stadion
import fajlbeolvasas

stadionok=fajlbeolvasas.beolvas("stadionok.txt",[])
for i in range(0,len(stadionok),1):
    """print(stadionok[i])"""

print(f"Első stadion neve: {stadionok[0]}")
