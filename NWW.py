from random import randint
from math import sqrt
def NWW (a,b):
    i = 0
    x = 1
    if b%a != 0:
        x = b%a
        if a%x!=0:
            y = x
            x = a%y
            while a%x!=0:
                z = x
                x = y%z
                if a%x==0:
                    break
                y = x
                x = z%y
    i = (b*a)/x
    return i
testli= []                
z = input()
z = int(z)
for m in range(z):
    testli.append(input())
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
        v = 0
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
                        if (pr+x)>kon:
                            v = NWW(kon, pr+x)
                        else:
                            v = NWW(pr+x, kon)
                        if M==v:
                            Check1 = False
                            Check2 = False
                        else:
                            kon=v
                else:
                     Check2 = False
    if len(lista) > 1:
        print(lista[0],lista[-1])
