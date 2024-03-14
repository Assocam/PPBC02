#02.1.2 resistenze
#legge di Ohm V=RI; Rs=R1+R2 Rp=1/R1+1/Rn
print("\n"+"#02.1.2 resistenze")
R1=1
R2=2
R3=3
R23=(1/R2+1/R3)
Req=R1+R23
print("R1 =",R1)
print("R2 =",R2)
print("R3 =",R3)
print("La resitenza equivalente è:",round(Req,2))

#02.1.3 numero scomposto
print("\n"+"#02.1.3 numero scomposto")
N5cifre= 15236
StringaN5cifre=str(N5cifre)
print("il numero inserito è",StringaN5cifre)
print(StringaN5cifre[0]+"\n"+StringaN5cifre[1]+"\n"+StringaN5cifre[2]+"\n"+StringaN5cifre[3]+"\n"+StringaN5cifre[4])

#02.1.4 Auto ibrida
print("\n"+"#02.1.4 Auto ibrida ")
CostoAuto1= int(input("inserisci costo auto ")) #12000
CostoAuto2= 20000         #I. il costo di un’auto nuova;
KManno= int(input("inserisci km in un anno "))#25000            #II. la stima dei chilometri percorsi in un anno;
CostoCarburante = 1.8   #III. La stima del costo del carburante; km*
EffA1KMlitro = int(input("inserisci efficienza auto "))#10
EffA2KMlitro = 12            #IV. L’efficienza in chilometri al litro;1
numAnni=int(input("inserisci #anni "))#5             #V. La stima del valore di rivendita dell’auto usata dopo 5 anni
ValA1_5anni = int(input("inserisci valore a"+str(numAnni)+"anni "))#5
ValA2_5anni = 9000 
CostoTOT1 = CostoAuto1 +KManno*CostoCarburante/EffA1KMlitro*numAnni-ValA1_5anni
CostoTOT2 = CostoAuto2 +KManno*CostoCarburante/EffA2KMlitro*numAnni-ValA2_5anni

print("l'auto 1 costa in totale:", CostoTOT1, "\n"+ "l'auto 2 costa in totale:", CostoTOT2)

#02.1.5 Forza elettrica
print("\n"+"#02.1.5 Forza elettrica")

Q1 = 1E-4
Q2 = 2E-4
r=1
eps=8.854E-12
Felettrica= Q1*Q2/(4*3.14*eps*r**2)
print("la carica 1 è di",Q1,"Coulomb")
print("la carica 2 è di",Q2,"Coulomb")
print("la distanza tra loro è di",r,"metri")
print("la Forza elettromotrice è di",round(Felettrica,2),"Newton")

#02.2.1 Caratteri
print("\n"+"#02.2.1 Caratteri")

Stringa='Mississippi'
print(Stringa[0:3]+"..."+Stringa[-1:-4:-1])
Stringa1='Missi'
print(Stringa1[0:3]+"..."+Stringa1[-1:-4:-1])
Stringa2='Mi'
print(Stringa2[0:3]+"..."+Stringa2[-1:-4:-1])

#02.2.2 Numero telefonico
print("\n"+"#02.2.2 Numero telefonico")

Numtel=4155551212
strNumtel=str(Numtel)
print("("+strNumtel[0:3] +") "+strNumtel[3:6]+"-"+strNumtel[6:])

#02.2.3 Allineamento
print("\n"+"#02.2.3 Allineamento")

a = 23
b = 34
costanti=("Le costanti sono:")
somma=("A. la somma è:")
differenza=("B. la differenza è:")
prodotto=("C. il prodotto è:")
media=("D. la media è:")
distanza=("E. la distanza è:")
max1=("F. il max è:")
min1=("G. il min è:")


print(costanti+"\t",a,"e",b)
print(somma+" "*(len(costanti)-len(somma))+"\t",a+b)
print(differenza+" "*(len(costanti)-len(differenza))+"\t",a-b)
print(prodotto+" "*(len(costanti)-len(prodotto))+"\t",a*b)
print(media+" "*(len(costanti)-len(media))+"\t",(a+b)/2)
print(distanza+" "*(len(costanti)-len(distanza))+"\t",abs(a-b))
print(max1+" "*(len(costanti)-len(max1))+"\t",max(a,b))
print(min1+" "*(len(costanti)-len(min1))+"\t",min(a,b))

#02.2.4 Emoji
print("\n"+"#02.2.4 Emoji")

print("\nI. la posizione in classifica è 1",)
print("II. il Numero Unicode è U0001F618", )
print("III. il Nome Unicode è 'Face Throwing a Kiss'")
print("IV. l'emoji è","\U0001F618")

print("\nI. la posizione in classifica è 2",)
print("II. il Numero Unicode è U0001F602", )
print("III. il Nome Unicode è 'Face with Tears of Joy'")
print("IV. l'emoji è","\U0001F602")

print("\nI. la posizione in classifica è 3",)
print("II. il Numero Unicode è U0001F44D", )
print("III. il Nome Unicode è 'Thumbs Up Sign'")
print("IV. l'emoji è","\U0001F44D")
