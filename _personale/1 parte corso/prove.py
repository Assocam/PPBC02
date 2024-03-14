import matplotlib.pyplot as plt

# Dati dei paesi principali
paesi = [
    "Giappone", "Germania", "Italia", "Stati Uniti", "Canada", 
    "Regno Unito", "Francia", "Cina", "India", "Brasile", 
    "Russia", "Messico", "Indonesia", "Nigeria", "Sudafrica"
]

dati_eta = [
    [48, 47, 47, 46, 46],   # Età media per Giappone
    [45, 44, 44, 43, 43],   # Età media per Germania
    [45, 45, 45, 44, 44],   # Età media per Italia
    [38.5, 38, 37.5, 37, 36.5],   # Età media per Stati Uniti
    [41, 40.5, 40, 39.5, 39],   # Età media per Canada
    [40.5, 40, 40, 39.5, 39],   # Età media per Regno Unito
    [41, 40.5, 40, 39.5, 39],   # Età media per Francia
    [38, 37.5, 37, 36.5, 36],   # Età media per Cina
    [28, 27.5, 27, 26.5, 26],   # Età media per India
    [33, 32.5, 32, 31.5, 31],   # Età media per Brasile
    [40.5, 40, 39.5, 39, 38.5],   # Età media per Russia
    [29, 28.5, 28, 27.5, 27],   # Età media per Messico
    [30, 29.5, 29, 28.5, 28],   # Età media per Indonesia
    [18, 17.5, 17, 16.5, 16],   # Età media per Nigeria
    [28, 27.5, 27, 26.5, 26]    # Età media per Sudafrica
]

dati_eta_perc = []
# Calcolo delle variazioni percentuali rispetto al 2016
for dati in dati_eta:
    variazioni_paese = []
    for eta in dati:
        variazione_percentuale = ((eta - dati[0]) / dati[0]) * 100
        variazioni_paese.append(variazione_percentuale)
    dati_eta_perc.append(variazioni_paese)
import matplotlib.pyplot as plt

# Anni
anni = range(2016, 2021)

# Grafico a linee per le variazioni percentuali rispetto al 2016 per ciascun paese
plt.figure(figsize=(12, 8))
for paese, variazioni in zip(paesi, dati_eta_perc):
    plt.plot(anni, variazioni, marker='o', label=paese)

plt.xlabel('Anno')
plt.ylabel('Variazione Percentuale rispetto al 2016 (%)')
plt.title('Variazione Percentuale dell\'Età Media rispetto al 2016 per Paese')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
