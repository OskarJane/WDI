import random
import time

x = random.randint(1,100)
liczba=0
zakres_dol=0
zakres_gora=100
i=0
print ("Wylosowana liczba",x)

while liczba != x:

	i=i+1

	liczba = random.randint(zakres_dol,zakres_gora)
	print("Wprowadź liczbę: ")
	time.sleep(1)
	print(liczba)
	time.sleep(1)

	if(liczba > x):
		print ("Liczba jest za duża")
		if(x<zakres_gora):
			zakres_gora=liczba
	if(liczba < x):
		print ("Liczba jest za mała")
		if(x>zakres_dol):
			zakres_dol=liczba
	if(liczba == x):
		print ("brawo, mój przyjacielu")
	time.sleep(1)
print("Zgadles liczbe w: ",i," ruchach")