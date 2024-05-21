def fibonaci(sequenza):
    primo = 0
    secondo = 1
    lista_fibo = []
    for v in range(sequenza):
        fibo = primo + secondo
        primo = secondo
        secondo = fibo
        lista_fibo.append(fibo)
        
    return lista_fibo
print(fibonaci(10))