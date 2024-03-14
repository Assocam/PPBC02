#Esercizio piastrelle
Ldisp = 100
a =5 #Lato piastrella nera
b=5 #Lato piastrella bianca
c=(a+b) #Lunghezza coppia
MaxCoppiePiastrelle=((Ldisp-a)//c) #numero di coppie 
NPiastIncoppia=2*MaxCoppiePiastrelle #numero di piastrelle in coppia
Npiastrelle = NPiastIncoppia + 1 #numero di piastrelle tot
SpazioVuoto=((Ldisp-NPiastIncoppia*c/2-a)/2)
print("la piastrella nera è larga:",a)
print("la piastrella bianca è larga:",b)
print("la coppia di piastrelle sono larghe:",c)
print("il numero max di piastrelle inseribili è",Npiastrelle,"ossia 1 nera piu",MaxCoppiePiastrelle,"coppie di piastrelle(",NPiastIncoppia,")")
print("lo spazio vuoto rimasto è di", SpazioVuoto,"per lato")

print( "ciao\n**sda")