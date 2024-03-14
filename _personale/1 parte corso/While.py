# numero=0 
# while numero<10: #esce dal ciclo quando la condizione è falsa
#     numero+=1
#     print(numero)
# print("fine")

# #for per stringhe
# stringa="ciao"
# for c in stringa:
#     print(c,c,sep='-',end='**')
# print("fine")

# #for per numeri int
# num=100
# for n in range(0,int(num/3),3): #3virgola step #al contrario range(int(num/3),0,-3)
#     print(n,n,sep='-',end='**')
# print("fine")

# #for per indici 
# for i in range(len(stringa)): 
#     print(stringa[i],stringa[i],sep='-',end='**')
# print("fine")

# for (i,j) in enumerate(stringa):
#     print(i,j,end=" ")
# print("fine")

N=3
for i in range(1,2*N):
    if i< N:
        for j in range(1,2*N):
            if j< N:
                print(f"{j*i:3}",end=" ")
            else:
                print(f"{(-j+2*N)*i:3}",end=" ")
    else:
        for j in range(1,2*N):
            if j< N:
                print(f"{j*(-i+2*N):3}",end=" ")
            else:
                print(f"{(-j+2*N)*(-i+2*N):3}",end=" ")
    print("\n")
print(f"{'Ciao'*20:1000}")
N=2
for i in range(1,2*N):
    if i< N:
        for j in range(1,2*N):
            if j< N:
                A=j*i
                print(f'{"*"*A:5}',end=" ")
            else:
                A=(-j+2*N)*i
                print(f'{"*"*A:5}',end=" ")
    else:
        for j in range(1,2*N):
            if j< N:
                A=(-i+2*N)*j
                print(f'{"*"*A:5}',end=" ")
            else:
                A=(-i+2*N)*(-j+2*N)
                print(f'{"*"*A:5}',end=" ")
    print("\n")
    
