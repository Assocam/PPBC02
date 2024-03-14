# #& "openpyxl
# #& "C:/Program Files/Python310/python.exe" -m pip install XX
# aa=0.1
# bb= 0.2

# print(aa+bb)
# print(''' dsfs"dsdfsd''')

# from math import sqrt 
# #from math import *
# #from math import sqrt
# print(sqrt(10))

# Numeri primi

limite = int(input('Fino a quale valore vuoi arrivare? '))

for n in range(2,limite+1):
    # verifico se n è primo
    # uso il codice dell'esercizio precedente
    primo = True
    for i in range(2, n):
        if n % i == 0: 
            primo = False
    if primo:
        print(n)
