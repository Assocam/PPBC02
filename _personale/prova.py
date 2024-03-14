N=4
for i in range (0,N): #riga
    for j  in range(2*N): #colonna
        if j<=N:
            if j>(N-i-1): #quando la colonna è maggiore di N - #riga -1
                print("*",end="")
            else:
                print(' ',end="")
        if j>N:
            if j+N>(2*(N-i)):  #quando la colonna è maggiore di N - #riga -1
                print("*",end="")
            else:
                print('.',end="")

    print("\n")

print("ciao")
if __name__== "__main__":
    print("sei nello script")
print(__name__)
#a