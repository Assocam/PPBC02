import csv
import os

# Ottiene il percorso assoluto dello script corrente
script_path = os.path.abspath(__file__)

# Ottiene la directory in cui risiede lo script
script_dir = os.path.dirname(script_path)

# Costruisce un percorso relativo alla directory dello script
file_absolute_path = os.path.join(script_dir, 'botteghe-storiche.csv')


# with open('C:/PPBC02/PPBC02/_lezioni/PPAC01/2024-05-02_/botteghe-storiche.csv', 'r', encoding='utf-8') as file_in:
# with open(r'C:\PPBC02\PPBC02\_lezioni\PPAC01\2024-05-02_\botteghe-storiche.csv', 'r', encoding='utf-8') as file_in:
with open(file_absolute_path, 'r', encoding='utf-8') as file_in:
    file_reader = csv.DictReader(file_in, delimiter=",")
    for linea in file_reader:
        if linea['ID'] in ['45', '64', '176', '204']:  # filtro
            print('ID:', linea['ID'])
            print('Ragione sociale:', linea['Ragione sociale'])
            print('Cap:', linea['Cap'])
            print('----------------------------')


print('__file__:', __file__)
print('CWD:', os.getcwd())
print('file_absolute_path:', file_absolute_path)