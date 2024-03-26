import csv
# #with open(r"C:\PPBC02\PPBC02\files_esercizi\botteghe-storiche.csv","r") as file_in:
# with open("./files_esercizi/botteghe-storiche.csv","r",encoding='utf-8') as file_in:
#     File_reader=csv.DictReader(file_in,delimiter=",")
#     for _ in range(10):
#         linea=next(file_in)
#         print(linea, end='')

with open("./files_esercizi/botteghe-storiche.csv","r",encoding='utf-8') as file_in:
    File_reader=csv.DictReader(file_in,delimiter=",")
    for _ in File_reader:
        if _['ID'] in ["45","46"]:
            print(_["ID"],_['Ragione sociale'])