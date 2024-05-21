import os
import json
nomeFile='_personale\\dati_di_base.csv'
nomeFile = os.path.abspath(nomeFile)
dizdati={}
with open(nomeFile,'r',encoding='utf-8') as fr:
    paperino= fr.read()
    righe=paperino.split('\n')
    dizdati = {}
    riga = 0
    for r in righe:
        colonne=r.split(';')
        if riga ==0:
            chiavi=colonne
        else:
            dizdati[riga]={}
            dizdati[riga][chiavi[0]] = colonne[0]
            dizdati[riga][chiavi[1]] = colonne[1]
            dizdati[riga][chiavi[2]] = colonne[2]
        riga = riga + 1
        jdata = json.dumps(dizdati)
        with open(nomeFile+'.json' , 'w',encoding= 'utf-8') as fw:
            fw.write(jdata)
# adesso faremo al contrario

#lego il file.json
with open('jdati_di_base.json' , 'r' , encoding='utf-8') as fr:
    buffer= fr.read()

    dicDatiNew = json.loads(buffer)
    print(dicDatiNew)
    chiavi=dicDatiNew.keys()
    print(chiavi)
    righe = 0
    file = []

    for k in chiavi:
        dicPiccolo = dicDatiNew[k]
        chiaviCSV = dicPiccolo.cheys()
        rigacsv = ''
        rigaintestazione = '' 
        if righe == 0:
            for k2 in chiaviCSV:
                rigaintestazione += k2 + ';'
            intestazione = rigaintestazione[:-1]
            intestazione = intestazione + '\n'
            file.append(intestazione)
            righe+= 1
        else:
            for k3 in chiaviCSV:
                rigacsv += dicPiccolo[k3] + ';'
                rigacsv = rigacsv[:-1] + '\n'
                file.append(rigacsv)
            print(file)
#devo scrivere il nuovo file csv
buffer = ''
for z in file:
    buffer += z
    buffer = buffer[:-1]
with open('nuovocsv.csv','w',encoding='utf-8')as fw:
    fw.write(buffer)



                






