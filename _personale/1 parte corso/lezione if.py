#esercizio sconti
# PrezzoSconto1=128
# sconto1=8
# sconto2=16


# prezzo=int(input("quanto costa? "))
# Costo1=prezzo*(100-sconto1)/100
# Costo2=prezzo*(100-sconto2)/100
# if prezzo<PrezzoSconto1:
#     print(f"Il costo è {Costo1} scontato del {sconto1}%, risparmi {prezzo-Costo1}")
# else:
#     print(f"Il costo è {Costo2} scontato del {sconto2}%, risparmi {prezzo-Costo2}")

#Esercizio aliquote
NCreddito1=32000
NCiTasse1=10
NCsoglia1=32000
NCfTasse2=3200
NCiTasse2=25
NCsoglia2=32000
NCal1="10%"
NCal2=f"10% fino a 32000 + 3200 + 25% della differenza"

Creddito1=64000
CiTasse1=10
Csoglia1=32000
CfTasse2=6400
CiTasse2=25
Csoglia2=64000
Cal1="10%"
Cal2=f"10% fino a 64000 + 6400 + 25% della differenza"

Reddito=float(input("inserire reddito: "))
Stato=input("sei coniugato? [si/no]").upper()
print(Stato)
if Stato=="SI":
    if Reddito<Creddito1:
        tasse=Reddito*CiTasse1/100
        aliquota=Cal1
    else:
        tasse=Reddito*CiTasse1/100+CfTasse2+(Reddito-Creddito1)*CiTasse2/100
        aliquota=Cal2
else:
    if Reddito<NCreddito1:
        tasse=Reddito*NCiTasse1/100
        aliquota=NCal1
    else:
        tasse=Reddito*NCiTasse1/100+NCfTasse2+(Reddito-NCreddito1)*NCiTasse2/100
        aliquota=NCal2
print(f"le tasse da pagare sono {tasse},con l'aliquota {aliquota}" )

