import sys


# path_script = sys.argv[0]
if len(sys.argv) != 3:
    print("Il numero di parametri passati non è corretto. Devi inserire 2 numeri.")
else:
    try:
        primo_numero = float(sys.argv[1])
        
    except ValueError


secondo_numero = float(sys.argv[2])
    risultato = primo_numero * secondo_numero
    print(f"il risultato di {primo_numero} per {secondo_numero} è uguale a {risultato}")
