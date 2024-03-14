import sys
import prova

args=sys.argv
if __name__=="__main__":
    frist_num =float(args[1])
    second_num=float(args[2])
else:
    frist_num=float(input("inserisci prino num: "))
    second_num=float(input("inserisci secondo num: "))
print(frist_num,second_num)
product=frist_num*second_num
print(product)

#per eseguire script da terminale: py molt_due_num.py 20 30 (da eseguire nella directory o indicando il percorso)
#prova non è eseguito completamente perchè importato come modulo e non eseguito come script