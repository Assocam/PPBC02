# #04.1.1 Numeri interi
# print("inserisci sequenza numerica, termina la sequenza con insermento di stringa vuota''")
# N=input("inserisci primo numero ")
# count=0
# somma=0
# min=9999999
# max=0
# countdisp=0
# while N!="":
#     print(N,end="-")
#     count+=1
#     N=(input("inserisci prossimo numero "))
#     if N!="":
#         somma+=int(N)
#         print(somma)
#         if int(N)<min:
#             min=int(N)
#         if int(N)>max:
#             max=int(N)
#         if int(N)%2!=0:
#             countdisp+=1
# print("il valore minimo è:",min)
# print("il valore massimo è:",max)
# print("il numero di valori inseriti è:",count)
# print("il numero di valori dispari inseriti è:",countdisp)

# #04.1.2 Analisi di una stringa.
# stringa=input("inserisci una stringa:")
# newstringa=""
# contnum=0
# upstringa=stringa.upper()
# print(upstringa)
# print("le sole lettere maiuscole sono:")
# for _ in stringa:
#     if _.isupper():
#         print(_)
# print("le lettere in posizione pari sono:")
# for i in range(len(stringa)):
#     if i%2==0:
#         print(stringa[i],end="-")
# print("\nle stringa senza vocali è:")
# for _ in upstringa:
#     if (_=="A") or (_=="E")or (_=="I")or (_=="O")or (_=="U"):
#         _="_"
#     newstringa=newstringa+_
# print(newstringa)
# print("i numeri presenti nella stringa sono:")
# for _ in stringa:
#     if _.isnumeric():
#         contnum+=1
# print(contnum)
# print("la posizione di tutte le vocali nella stringa è:")
# for j in range(len(upstringa)):
#     if (upstringa[j]=="A") or (upstringa[j]=="E") or (upstringa[j]=="I") or (upstringa[j]=="O") or (upstringa[j]=="U"):
#         print(j,end="-")
# print("fine")
    
#04.1.3 Lati  
N=4
for i in range(0,N):
    for j in range(0,N):      
        print(f'{"*"}',end=" ")
    print("\n")

for i in range(0,2*N):
    if i<N:
        for j in range(1,2*N):
            if j<(N-i):     
                print(f'{" "}',end=" ")
            elif j<=(N+i):
                print(f'{"*"}',end=" ")
        print("\n")
    if i>N:
        for j in range(1,2*N+1):
            if j<=(i-N):     
                print(f'{" "}',end=" ")
            elif j-N<(2*N-i):
                print(f'{"*"}',end=" ")
        print("\n")
    
#     #04.1.4 Parole al contrario.
# Stringa=input("inserisci stringa: ")
# print(Stringa)
# Stringarev=""
# Mairevstri=""
# for _ in Stringa[::-1]:
#     Stringarev=Stringarev+_
# print(Stringarev)
# for _ in Stringa[::-1]:
#     if _.isupper():
#         Mairevstri=Mairevstri+_
# print(Mairevstri)

# #04.1.5 Numeri primi.
# num=input("inserisci numero: ")
# num=int(num)
# a=0
# for n in range(2,num):
#     b=num%n
#     if b==0:
#         a=1
# if a!=1:
#     print(num,"il numero è primo")
# else:
#      print(num,"non è primo ") 

# #04.1.6 Numeri primi.
# num=input("inserisci numero: ")
# num=int(num)
# a=0
# nump=num-1
# for n in range(2,num):
#     b=num%n
#     if b==0:
#         a=1
# if a!=1:
#     print(num,"il numero è primo")
# else:
#      print(num,"non è primo ") 
# print("i numerI primi inferiori sono")
# for i in range(2,num):
#     a=0
#     for n in range(2,nump):
#         b=nump%n
#         if b==0:
#             a=1
#     if a!=1:
#         print(nump,end="-")
#     nump-=1

# #04.1.7 Parole a pezzi.
# Stringa=input("inserisci una stringa: ")
# for k in range(0,len(Stringa)):
#     for i in range(len(Stringa)-k):
#         print(Stringa[i:i+1+k])

# #04.1.8 Numeri duplicati
# Num=(input("inserisci il primo numero: "))
# num2=""
# Duplicati=""
# while Num!="":
#     Num1=(input("inserisci il prossimo numero: "))
#     if (Num1)==(Num) and Num1!=num2:
#         Duplicati+=f"{Num1} "
#     if (Num1)==(Num):
#         num2=Num1
#     Num=Num1
# print(Duplicati)

# #4.2.1 Il gioco di Nim.
# from random import randint

# def logicaPC(Biglrimaste,Intell):
#     if Intell==0:
#         mossaPC=randint(1,Biglrimaste//2)
#     if Intell==1:
#         if Biglrimaste//2>=31:
#             a=randint(1,4)
#             if a==1:
#                 mossaPC=1
#             elif a==2:
#                 mossaPC=3
#             elif a==3:
#                 mossaPC=15
#             elif a==4:
#                 mossaPC=31
#         elif Biglrimaste//2>=15:
#             a=randint(1,3)
#             if a==1:
#                 mossaPC=1
#             elif a==2:
#                 mossaPC=3
#             elif a==3:
#                 mossaPC=15
#         elif Biglrimaste//2>=3:
#             a=randint(1,2)
#             if a==1:
#                 mossaPC=1
#             elif a==2:
#                 mossaPC=3
#         else:
#             mossaPC=1 
#     return mossaPC

# totbigl=randint(10,100)
# print("il numero di biglie di partenza [10:100] è:",totbigl)
# Intel=randint(0,1)
# if Intel==0:
#     print("Giochi con il Pc stupido")
# else:
#     print("Giochi con il Pc intelligente")
# Start=randint(0,1)
# if Start==0:
#     Biglrim=totbigl
#     print("inizio io")
#     while Biglrim>1:
#         print("tocca a me")
#         PescaPC=logicaPC(Biglrim,Intel)
#         print("Prendo",PescaPC,"biglie")
#         Biglrim=Biglrim-PescaPC
#         print(f"rimangono {Biglrim} biglie")
#         if Biglrim==1:
#             print("hai perso")
#             exit
#         else:
#             print(f"tocca a te, puoi pescare da 1 a {Biglrim//2} biglie")
#             Xbigl=input(f"scegli quante biglie prelevare: [1:{Biglrim/2}]: ")
#             Biglrim=Biglrim-int(Xbigl)
#         print(f"rimangono {Biglrim} biglie")
#         if Biglrim==1:
#             print("ho perso")   
#             exit
# else:
#     print("inizi tu")
#     Xbigl=input(f"scegli quante biglie prelevare: [1:{totbigl//2}]: ")
#     Biglrim=totbigl-int(Xbigl)
#     print(f"rimangono {Biglrim} biglie")
#     while Biglrim>1:
#         print("tocca a me")
#         PescaPC=logicaPC(Biglrim,Intel)
#         print("Prendo",PescaPC,"biglie")
#         Biglrim=Biglrim-PescaPC
#         print(f"rimangono {Biglrim} biglie")
#         if Biglrim==1:
#             print("hai perso")
#             exit
#         else:
#             print(f"tocca a te, puoi pescare da 1 a {Biglrim//2} biglie")
#             Xbigl=input(f"scegli quante biglie prelevare: [1:{Biglrim//2}]: ")
#             Biglrim=Biglrim-int(Xbigl)
#         print(f"rimangono {Biglrim} biglie")
#         if Biglrim==1:
#             print("ho perso")  
#             exit





