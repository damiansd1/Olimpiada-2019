from random import randint
from time import time
from math import sqrt
def NWW (a,b):
    i = 0
    if b%a == 0:
           i = b*a
    else:
        z = b-a
        x = int(a/2)+1
        for r in range(x,2,-z):
           if a%r == 0:
               if b%r == 0:
                  i = r
    return i
testli= []                
z = input()
z = int(z)
for m in range(z):
    #testli.append(randint(1,1000000000))
    testli.append(input())
t1=time()
print (testli)
for b in range(len(testli)):
    M = int(testli[b])
    pr = 0
    Check3 = True
    Check1 = True
    Check2 = True
    lista = []
    if M>100:
        Z = str(M)
        skr = sqrt(10**len(Z))
        if skr != int(skr):
            skr = sqrt((10**len(Z))*10)
    else: skr=M/2        
    while Check1==True:
        lista = []
        Check2 = True
        pr+=1
        x = 0
        kon = pr
        lista.append(pr+x)
        if pr>skr:
             print("NIE")
             Check1 = False
             Check2 = False
             lista = []           
             break
        if M%pr == 0:
            while Check2:
                x+=1    
                lista.append(pr+x)
                if M%(pr+x)==0:
                  #  if pr*(pr+x)< or M==NWW(kon,pr+x):
                   #     print (NWW(kon, pr+x))
                   #     Check1 = False
                        Check2 = False
                    else:
                        kon=NWW(kon,pr+x)
                else:
                     Check2 = False
    if len(lista) != 0:
        print(lista[0],lista[-1])
print(time()-t1)
