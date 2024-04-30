# Aprire il file
import os
import json

nomeFile = 'dati_di_base.csv' 
nomeFile = os.path.abspath(nomeFile)

with open(nomeFile,'r', encoding= 'utf-8') as fr:

# Leggere il file
    paperino = fr.read()

# Dividere per righe
    righe = paperino.split('\n')

# Costruire il dizionario
    dizdati = {}

# Dividere ogni riga per colonna

    riga = 0

    for r in righe:
        colonne = r.split(';')

        # print(r)
        # print(colonne)

        if riga == 0:
            chiavi = colonne

        else:
            dizdati[riga]= {}
            dizdati[riga][chiavi[0]] = colonne[0]
            dizdati[riga][chiavi[1]] = colonne[1]
            dizdati[riga][chiavi[2]] = colonne[2]


        riga = riga + 1

    # print(dizdati)

# Convertire il dizionario in JSON

    jdata = json.dumps(dizdati)

    #print('JSON -> ', jdata)
    #print('DIZIONARIO ->',dizdati)

# Scrivere i dati in formato JSON
    with open('jdati_di_base.json','w', encoding='utf-8') as fw:
        fw.write(jdata)

# adesso dobbiamo fare il contrario

#leggo il file .json
    with open('jdati_di_base.json','r', encoding='utf-8') as fr:
        buffer = fr.read()
        
#lo ritrasformo in un dizionario
    dicDatiNew = json.loads(buffer)
    print(dicDatiNew)
#rifaccio il file .csv

    #devo ottenere l'elenco delle chiavi del dizionario.
    chiavi = dicDatiNew.keys()
    print(chiavi)

    righe = 0

    file = []

    for k in chiavi:
        dicPiccolo = dicDatiNew[k]
        chiaviCSV = dicPiccolo.keys()

        rigaCSV = ''

        if righe == 0:
            #prima riga del file csv
            rigaintestazione = ''
            for k2 in chiaviCSV:
                rigaintestazione += k2 + ';'

            intestazione = rigaintestazione[:-1]
            intestazione = intestazione + '\n'

            file.append(intestazione)

            righe += 1

        else:
            
            for k3 in chiaviCSV:
                rigaCSV += dicPiccolo[k3] + ';'

            rigaCSV = rigaCSV[:-1] + '\n'

            file.append(rigaCSV)

    print(file)    

    # DEVO scrivere il nuovo file CSV
    buffer = ''
    for z in file:
        buffer += z

    buffer = buffer[:-1]

    with open('nuovoCSV.CSV', 'w',encoding='utf-8') as fw:
        fw.write(buffer)


