"""def NWW (inp):
    fragmenty = 1
    Części = []
    while inp/fragmenty!=0:
        cz = 2
        Check = False
        while Check == True:
            if (inp/fragmenty)%cz==0:
               Części.append(cz)
               fragmenty*cz == fragmenty
               Check = True
            else:
                cz+=1
            print ("good")
    return Części"""
def NWW (a,b):
    for i in range(b,(a*b)+1):
        if (i/a) == int(i/a):
            if (i/b)==int(i/b):
                return i
testli= []                
z = input()
z = int(z)
for m in range(z):
    testli.append(input())
for b in range(len(testli)):
    M = int(testli[b])
    pr = 0
    Check1 = True
    Check2 = True
    lista = []
    while Check1==True:
        lista = []
        Check2 = True
        pr+=1
        x = 0
        kon = pr
        lista.append(pr+x)
        if pr > M:
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
                    if M==NWW(kon,pr+x):
                        print (NWW(kon, pr+x))
                        Check1 = False
                        Check2 = False
                    else:
                        kon=NWW(kon,pr+x)
                    

                else:
                     Check2 = False

    print(lista[0],lista[-1])
            
                
                
                
