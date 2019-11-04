n = input()
n = int(n)
A= []
B = []
K = []
for X in range(n):
    A.append(input())
    B.append(input())
    K.append(input())
for Z in range(n):
    Check1 = True
    while Check1 == True:
        a = A[Z]
        b = B[Z]
        k = K[Z]
        c = []
        l = len(a)
        a = int(a)
        b = int(b)
        k = int(k)
        rs = (a-b)+1
        rs = str(rs)
        r = len(rs)
        if a/(10**l)<1:
            r-=1
        for W in range(r,l):
     !!!       c.append(a/10**(l-W))
        div = r    
        for Q in range(r):
            tb = b/10**div
            t = a/10**div-tb
            if t != 0:
                if k == 1:
                    c.append(tb-1)
                if k>1:
                    c.append(tb)
                k-=1
                if k == 0:
                    break
            elif t == 0:
                c.append(tb)
            div-=1
            
                
            
            
        
        
    
