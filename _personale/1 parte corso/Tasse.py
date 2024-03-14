#Esercizio aliquote
soglia1=15000
soglia2=28000
soglia3=50000
S1Tasse=23
S2Tasse=25
S3Tasse=35
S4Tasse=43

RAL=float(input("inserire RAL: "))
Nmesi=float(input("inserire numero mensilità: "))
ContrInps=round(RAL*9.19/100,2)
RedImp=round(RAL-ContrInps,2)


if RedImp<=soglia1:
    Irpef=RedImp*S1Tasse/100
    dertidip=1380
    print(f"le tasse da pagare sono {Irpef}, in soglia {S1Tasse}%")
elif RedImp<=soglia2:
     T1=soglia1*S1Tasse/100
     T2=(RedImp-soglia1)*S2Tasse/100
     Irpef=T1+T2
     dertidip=1910+(1910*(soglia2-RAL)/13000)
     print(f"le tasse da pagare sono {Irpef}, \n {T1} in soglia {S1Tasse}%,\n {T2} in soglia {S2Tasse}%")   
elif RedImp<=soglia3:
     T1=soglia1*S1Tasse/100
     T2=(soglia2-soglia1)*S2Tasse/100
     T3=(RedImp-soglia2)*S3Tasse/100
     Irpef=T1+T2+T3 
     dertidip=1910+(1910*(soglia3-RAL)/22000)

     print(f"le tasse da pagare sono {Irpef}, \n {T1} in soglia {S1Tasse}%,  \n {T2} in soglia {S2Tasse}%,\n {T3} in soglia {S3Tasse}%")   
else:
    T1=soglia1*S1Tasse/100
    T2=(soglia2-soglia1)*S2Tasse/100
    T3=(soglia3-soglia2)*S3Tasse/100
    T4=(RedImp-soglia3)*S4Tasse/100
    Irpef=T1+T2+T3+T4
    dertidip=0
    print(f"le tasse da pagare sono {Irpef}, \n {T1} in soglia {S1Tasse}%,  \n {T2} in soglia {S2Tasse}%,  \n {T3} in soglia {S3Tasse}%, \n {T4} in soglia {S4Tasse}%")
Detr=round(dertidip,2)#+detrX
AddReg=0.9/100*RedImp
AddCom=1/100*RedImp
ImpLord=Irpef+AddReg+AddCom
ImpNetta=round(ImpLord-Detr,2)
RedNetto=round(RedImp-ImpNetta,2)#+bonusR
Tperc=round((ImpLord+ContrInps)/RAL*100,2)
RedMensNetto=round(RedNetto/Nmesi,2)
print(f"la percentuale totale di tasse sul reddito da pagare equivale a: {Tperc}%")
print(f"il tuo reddito netto è di {RedNetto}€, \n Reddito mensile: {RedMensNetto}€")