Bored = [[],[],[],[],[]]
Copy = []
for i in Bored:
    for b in range(0,4,1):
        c = []
        a = input()
        c = a.split(" ")
        for k in c:
            i.append(int(k))
Copy = Bored
    
for i in Bored:
    j = max(i)
    endgame = False
    if endgame:
        i.clear()
        i.append(j)
            
    else:
        counter = -1
        while True:
            counter = counter + 1
            if counter == len(i) + 20:
                break
            for k in range(0,len(i),1):
                for b in range(k+1,len(i),1):
                    if k == b: break
                    if i[k] == i[b]:
                        I = (2*i[k])
                        i.pop(b)
                        i.pop(k)
                        i.append(I)

                        counter = 0
                        break
                
                    
                    
for i in range(0,5,1):
        print(max(Bored[i]))
            

                

