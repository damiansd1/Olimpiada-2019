from sys import exit
l = input()
l = int(l)
txt = []
for P in range(l):
    txt.append(input())
for z in range(len(txt)):
    source = txt[z]
    source = str(source)
    try:
        file = open('Mickiewicz.txt', 'r')
        MI = file.read()
    finally: 
        file.close()
    MI = str(MI)
    MI = MI.split()
    source = str(source)
    source = source.split()
    for p in range(len(MI)-len(source)):
        if source[0]== MI[p]:
            check2 = True
            if len(source)<5:
                for x in range(len(source)):
                    if source[x]!=MI[p+x]:
                        check2 = False
                        break
            else:
                for x in range(1,5):
                    if source[x]!=MI[p+x]:
                        check2 = False
                        break
            if check2 == True:
                print("Mickiewicz")
                exit()
    
               
                
                
                
