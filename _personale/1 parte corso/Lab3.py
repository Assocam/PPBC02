#Parte 1 – Confronti, operatori relazionali e booleani
#03.1.1 Vero o Falso
# 

#03.1.2 Identikit della stringa
# print("\n #03.1.2 Identikit della stringa")
# E2Stringa=input("inserisci stinga ")
# E21=E2Stringa.isalpha()
# print(E2Stringa)
# print(f"contiene soltanto lettere                      {E21}")
# print(f"contiene soltanto lettere maiuscole            {E2Stringa.isupper()}")
# print(f"contiene soltanto lettere minuscole            { E2Stringa.islower()}")
# print(f"contiene soltanto cifre numeriche decimali;    { E2Stringa.isdecimal()}")
# print(f"contiene soltanto lettere e cifre              { E2Stringa.isalnum()}")
# print(f"inizia con una lettera maiuscola               {E2Stringa[0].isupper()}")
# print(f"termina con un punto                         ", E2Stringa[-1]==".")

#03.1.3 Stringhe e sottostringhe
# from sys import exit
# print("\n #03.1.3 Stringhe e sottostringhe")
# E3Stringa=input("inserisci DNA di 20 caratteri [A,C,T,G] ")
# if  E3Stringa.isalpha() or len(E3Stringa)==20:
#     E3Stringa2=input("inserisci DNA di 3 caratteri [A,C,T,G] ")
#     if  E3Stringa.isalpha() or len(E3Stringa)==20:
#         print(E3Stringa)
#         print(E3Stringa2)
#         if E3Stringa2 in E3Stringa:
#             print(f"la 'sequenza lunga' contiene la 'sequenza breve'                          ", E3Stringa2 in E3Stringa )
#             print(f" da quale posizione della 'sequenza lunga' è presente la 'sequenza breve' ", E3Stringa.find(E3Stringa2))
#             print(f"quante volte la sequenza 'lunga' contiene la sottostringa più breve'      ", E3Stringa.count(E3Stringa2))
#         else:
#             print(f"la 'sequenza lunga' non contiene la 'sequenza breve'                          ")
#     else:
#         exit("Dati non inseriti correttamente")
# else:
#     print ("Dati non inseriti correttamente")



# #03.1.5 Questione di logica
# print("\n #03.1.5 Questione di logica")
# from sys import exit
# E5V=input("inserisci un numero intero 'x' ")
# if not E5V.isdigit:
#     exit("Dati non inseriti correttamente")
# E5V=int(E5V)
# print("x=",E5V)
# print("I. x > 0 and x < 100             ",(E5V>0 and E5V<100))
# print("II. x > 0 or x < 100             ",(E5V>0 or E5V<100))
# print("III. x > 0 or 100 < x            ",(E5V>0 or 100<E5V))
# print("IV. x > 0 and x < 100 or x == -1 ",(E5V>0 and 100<E5V) or E5V==(-1) )


# #03.2.1 Andamenti
# print("\n #03.2.1 Andamenti")
# from sys import exit
# E21x1=input("inserisci un numero intero 'x1' ")
# if not E21x1.isdigit():
#     exit("Dati non inseriti correttamente")
# E21x2=input("inserisci un numero intero 'x2' ")
# if not E21x2.isdigit():
#     exit("Dati non inseriti correttamente")
# E21x3=input("inserisci un numero intero 'x3' ")
# if not E21x3.isdigit():
#     exit("Dati non inseriti correttamente")
# E21x1=int(E21x1)
# E21x2=int(E21x2)
# E21x3=int(E21x3)
# print("x1=",E21x1,"\n","x2=",E21x2,"\n","x3=",E21x3,"\n")
# if E21x3>E21x2>E21x1:
#     print("la sequenza è Strettamente crescente")
# elif E21x3<E21x2<E21x1:
#     print("la sequenza è Strettamente decrescente")
# else:
#     print("la sequenza non è ne crescente ne decrescente")

# #03.2.2 Voti
# print("\n #03.2.2 Voti")
# from sys import exit
# E22x1=input("inserisci un voto ['A', 'B', 'C', 'D' e 'F'|+o-] ")
# if not E22x1[0].isalpha() or (len(E22x1)==2 and not (E22x1[1]=="+" or E22x1[1]=="-" )) or not (len(E22x1)==1 or len(E22x1)==2) :
#     exit("Dati non inseriti correttamente1")
# if not (E22x1[0].isupper) or (len(E22x1)==2 and E22x1[0]=="F") :
#     exit("Dati non inseriti correttamente2")
# print("il voto ",E22x1)
# if len(E22x1)==2:
#     if E22x1[1]=="+":
#         E22x1segno=+0.3
#     elif E22x1[1]=="-":
#         E22x1segno=-0.3
# else:
#     E22x1segno=0.0
# E22x1=E22x1[0]
# if E22x1 == "A":
#     E22x1Ris=4.0 
# elif E22x1 == "B":
#     E22x1Ris=3.0 + E22x1segno
# elif E22x1 == "C":
#     E22x1Ris=2.0 + E22x1segno
# elif E22x1 == "D":
#     E22x1Ris=1.0 + E22x1segno
# elif E22x1 == "F":
#     E22x1Ris=0.0
# else:
#      exit("Dati non inseriti correttamente3")
# if E22x1Ris>4:
#     E22x1Ris=4
# print("il voto equivale a ",E22x1Ris )

# #03.2.3 Cicli stagionali
# print("\n #03.2.3 Cicli stagionali")
# E23X=input("Inserisci data [GGMM] ")
# if not E23X[0].isdigit() or not len(E23X)==4:
#     exit("Dati non inseriti correttamente1")
# if  int(E23X[2:])<=0 or int(E23X[2:])>12:
#     exit("Dati non inseriti correttamente2")
# if int(E23X[2:])>0 and int(E23X[2:])<4:
#     E23XS="winter"
# elif int(E23X[2:])>3 and int(E23X[2:])<7:
#     E23XS="spring"
# elif int(E23X[2:])>6 and int(E23X[2:])<9:
#     E23XS="summer"
# elif int(E23X[2:])>8:
#     E23XS="fall"
# if int(E23X[2:])%3==0 and int(E23X[0:2])>=21:
#     if E23XS=="winter":
#         E23XS="spring"
#     elif E23XS=="spring":
#         E23XS="summer"
#     elif E23XS=="summer":
#         E23XS="fall"
#     elif E23XS=="fall":
#         E23XS="winter"
# print("la stagione è:",E23XS)

# #03.2.4 Anni bisestili
# print("\n #03.2.4 Anni bisestili")
# E24X=input("Inserisci un anno [XXXX >1582] ")
# if not E24X.isdigit() or not len(E24X)==4:
#     exit("Dati non inseriti correttamente1")
# if  int(E24X)<=1582:
#     exit("Dati non inseriti correttamente2")
# if int(E24X)%100==0 and not int(E24X)%400==0 :
#     E24XR="non è bisestile"
# elif int(E24X)%4==0:
#     E24XR="è bisestile"
# else:
#     E24XR="non è bisestile"
# print("l'anno ",E24X, E24XR )

# #03.2.5 Ancora voti
# print("\n #03.2.5 Ancora voti")
# from sys import exit
# E25x1=input("inserisci un voto [0.00:4.00] ")

# if float(E25x1)==0.00:
#     E25x1R="F"
# elif float(E25x1)>0.00 and float(E25x1)<0.7:
#     E25x1R="D-"
# elif float(E25x1)>=0.71 and float(E25x1)<1.01:
#     E25x1R="D"
# elif float(E25x1)>=1.01 and float(E25x1)<1.31:
#     E25x1R="D+"
# elif float(E25x1)>=1.31 and float(E25x1)<1.7:
#     E25x1R="C-"
# elif float(E25x1)>=1.71 and float(E25x1)<2.01:
#     E25x1R="C"
# elif float(E25x1)>=2.01 and float(E25x1)<2.31:
#     E25x1R="C+"
# elif float(E25x1)>=2.31 and float(E25x1)<2.7:
#     E25x1R="B-"
# elif float(E25x1)>=2.7 and float(E25x1)<3.01:
#     E25x1R="B"
# elif float(E25x1)>=3.01 and float(E25x1)<3.31:
#     E25x1R="B+"
# elif float(E25x1)>=3.3 and float(E25x1)<3.7:
#     E25x1R="A-"
# elif float(E25x1)>=3.7:
#     E25x1R="A"
# else:
#     print("Dati non inseriti correttamente2")
# print("il voto ",float(E25x1), "equivale a ",E25x1R)

# #03.2.7 Conversioni
# print("\n #03.2.7 Conversioni da SI a imperiale")
# from sys import exit
# E27x1=input("inserisci unità misura iniziale [ml, l, g, kg, mm, cm, m, km] ")
# if not (E27x1==("ml") or E27x1==("l") or E27x1==("g") or E27x1==("kg") or E27x1==("mm") or E27x1==("cm") or E27x1==("m") or E27x1==("km")):
#     exit("Dati non inseriti correttamente1")
# E27x2=input("inserisci unità misura finale [fl, gal, oz, lb, in, ft, mi] ")
# if not (E27x2==("fl") or E27x2==("ozl") or E27x2==("gal") or E27x2==("oz") or E27x2==("lb") or E27x2==("in") or E27x2==("ft") or E27x2==("m") or E27x2==("mi")):
#     exit("Dati non inseriti correttamente2")
# if (E27x1==("ml") or E27x1==("l")) and not(E27x2==("fl") or E27x2==("gal")):
#     exit("Unità non compatibili")
# if (E27x1==("g") or E27x1==("ml""kg")) and not(E27x2==("oz") or E27x2==("lb")):
#     exit("Unità non compatibili")
# if (E27x1==("mm") or E27x1==("cm") or E27x1==("m") or E27x1==("km")) and not(E27x2==("in") or E27x2==("ft") or E27x2==("m") or E27x2==("mi")):
#     exit("Unità non compatibili")

# I27x1=(input("inserisci numero da convertire: "))
# if not I27x1.isdigit():
#      exit("Dati non inseriti correttamente1")
# I27x1=float(I27x1)
# if E27x1==("l"):
#     E27x11=1000
# else:
#     E27x11=1
# if E27x1==("ml") or E27x1==("l"):
#     if E27x2==("fl"):
#         I27y1=I27x1/29.5735*E27x11
#     if E27x2==("gal"):
#         I27y1=I27x1/29.5735/128*E27x11

# if E27x1==("cm"):
#     E27x12=10
# elif E27x1==("m"):
#     E27x12=1000
# elif E27x1==("km"):
#     E27x12=1000*1000
# else:
#     E27x12=1
# if E27x1==("cm") or E27x1==("m")or E27x1==("km")or E27x1==("mm"):
#     if E27x2==("in"):
#         I27y1=I27x1/25.4*E27x12
#     if E27x2==("ft"):
#         I27y1=I27x1/25.4/12*E27x12
#     if E27x2==("mi"):
#         I27y1=I27x1/25.4/63360*E27x12

# if E27x1==("kg"):
#     E27x13=1000
# else:
#     E27x13=1
# if E27x1==("g") or E27x1==("kg"):
#     if E27x2==("oz"):
#         I27y1=I27x1/28.34952*E27x13
#     if E27x2==("lb"):
#         I27y1=I27x1/28.34952/16*E27x13

# print(I27x1,E27x1, "equivale a ", I27y1, E27x2)


# #03.2.8 Buoni spesa
# print("\n #03.2.8 Buoni spesa")
# from sys import exit
# E28x1=input("inserisci valore spesa ")
# if not E28x1.isdigit():
#     exit("Dati non inseriti correttamente1")
# E28x1=float(E28x1)
# if E28x1<10:
#     Buono=0
# elif 10<=E28x1<60:
#     Buono=8/100*E28x1
# elif 60<=E28x1<150:
#     Buono=10/100*E28x1
# elif 150<=E28x1<210:
#     Buono=12/100*E28x1
# elif E28x1>=210:
#     Buono=14/100*E28x1

# print("la sua spesa le ha generato un buono di ", Buono, "€")

# #03.2.9 Lunghezze d’onda
# print("\n 03.2.9 Lunghezze d’onda")
# from sys import exit
# E29x1=input("inserisci valore lunghezza d'onda ")
# # if not E29x1.isdigit():
# #     exit("Dati non inseriti correttamente1")
# E29x1=float(E29x1)
# if E29x1<10E-11:
#     onda="Raggi Gamma"
# elif 10E-11<=E29x1<10E-8:
#     onda="Raggi X"
# elif 10E-8<=E29x1<4*10E-7:
#     onda="Ultravioletti"
# elif 4*10E-7<=E29x1<7*10E-7:
#     onda="Luce visibile"
# elif 4*10E-7<=E29x1<10E-3:
#     onda="Infrarossi"
# elif 10E-3<=E29x1<10E-1:
#     onda="Microonde"
# elif E29x1>=10E-1:
#     onda="Onde Radio"

# print("la lunghezza d'onda rientra nel campo:", onda)

#03.2.10 Ritorno alla cometa
print("\n #03.2.10 Ritorno alla cometa")
from sys import exit
E210x1=input("inserisci velocità del salto: [Km/h]  ")
if not E210x1.isdigit():
    exit("Dati non inseriti correttamente1")
E210x1=float(E210x1)
G=6.67E-11 #Nm2/kg2
M=2.2E14 #kg
R=9.4*1000/2 #m
vescape=(2*G*M/R)**(1/2) 
if E210x1>=vescape:
    m=E210x1**2/G/2*R
    print("la velocità è troppo elevata, ci vorrebbe una massa pari a",m)
else:
    print("torni a terra!")

