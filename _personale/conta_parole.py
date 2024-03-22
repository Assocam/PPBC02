stringa = "Ciao come va meglio mai    dai  oggi?"
stringa_lista = stringa.split()    # dopo split diventa sewmpre una lista
stringa_lista = stringa.strip()

conteggio = stringa_lista.count(' ') + 1
print(conteggio)
    # Gestisci il caso speciale della stringa vuota.
    # if stringa == '':
    #     return 0

    # Conta gli spazi per contare il numero di parole.
    # Parole = Spazi + 1 (quindi inizializza il conteggio a 1)
# conteggio = 1
#     for carattere in stringa:
#         if carattere == ' ':
#             conteggio = conteggio + 1

    # Soluzione alternativa utilizzando il metodo .count() per le stringhe:
