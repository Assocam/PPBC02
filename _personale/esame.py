from csv import DictReader

file_path = '../../files_esercizi/botteghe-storiche.csv'  # percorso del file

col_names = ['ID', 'Ragione sociale', 'Comune', 'Cap']  # colonne da estrarre
record_ids = ['45', '64', '176', '204']                 # record da estrarre
sep_rec = '----------------------------'                # separatore visivo da usare

with open(file=file_path, mode='r', encoding='utf-8') as file_in:
    file_reader = DictReader(file_in, delimiter=",")
    for linea in file_reader:
        if linea['ID'] in record_ids:  # filtro
            for col_name in col_names:
                print(col_name+':', linea[col_name])
            print(sep_rec)
        else:
            pass