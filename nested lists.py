import random

def show(A ):
    for a in A:
        for s in a:
            print(s, end=" ")
        print()

def rands(m, n):
    res = [[random.randint(0, 9) for i in range(n)] for j in range(m)]
    return res

def symbs(m, n):
    val='A'
    res=[['' for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            res[i][j]=val
            val=chr(ord(val)+1)
    return res

A=[[(j+1)*10+i+1 for i in range(5)] for j in range(3)]
print(f'List A: {A}')

show(A)
random.seed(5067325)
B=rands(3,8)

print(f'List B: {B}')
show(B)

C=symbs(4,5)
print(f'List C: {C}')
show(C)

size=[3, 7, 4, 5]

D=[['*' for k in range(s)] for s in size]
print(f'List D: {D}')
show(D)