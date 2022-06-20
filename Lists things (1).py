##import random
##
##li = []
##lo = []
##for i in range(0,4,1):
##    for a in lo:
##        lo.remove(a)
##    for I in range(0,99,1):
##        a = random.randint(0,100)
##        lo.append(a)
##    li.append(lo)
##print(li)

##import threading
##from threading import Thread
##import random
##li = []
##for i in range(0,5,1):
##    lo = []
##    for I in range(0,10,1):
##        a = random.randint(1,100)
##        lo.append(a)
##    li.append(lo)
##print(li)
##
##def pro(List):
##    a = 1
##    for i in List:
##        a = a*i
##        
##    print(a)
##
##
##        
##Thread1 = Thread(target=pro, args=(li[0],))
##Thread2 = Thread(target = pro, args=(li[1],))
##Thread3 = Thread(target = pro, args=(li[2],))
##Thread4 = Thread(target = pro, args=(li[3],))
##Thread5 = Thread(target = pro, args=(li[4],))
##Thread1.start()
##print("")
##Thread2.start()
##print("")
##Thread3.start()
##print("")
##Thread4.start()
##print("")
##Thread5.start()
##print("")
##Thread1.join()
####Thread2.join()
####Thread3.join()
####Thread4.join()
####Thread5.join()
##
##print("finished?")

##import threading
##from threading import Thread
##def Reader(FILE):
##    r = open(FILE,"r")
##    a = 0
##    for i in r:
##        print(i)
##        a = a + 1
##    print(a)
##    print(str(FILE))
##
##
##thread = Thread(target = Reader,args=("The_otherthings.txt",))
##thread.start()
##thread.join()

##import random
##import threading
##from threading import Thread
##a = open("New_FILE","w")
##h = open("w_file","w")
##b = ["-","+","*","/"]
##for i in range(0,4,1):
##    q = random.randint(1,10)
##    j = random.randint(1,10)
##    u = random.choice(b)
##    if u == "-":
##        h.write(str(q-j) +"\n")
##    elif u == "+":
##        h.write(str(q+j) +"\n")
##    elif u == "*":
##        h.write(str(q*j) +"\n")
##    else:
##        h.write(str(q/j) +"\n")
##    
##    g = str(q)+u+str(j)
##    a.write(g + "\n")
##
##a.close()
##h.close()
##
##
##LE = []
##LA = []
##def EL(N):
##    d = open(N,"r")
##    for i in d:
##        i = i.strip()
##        LE.append(i)
##    print(LE)
##    d.close()
##
##    
##def AL(n):
##    d = open(n,"r")
##    for i in d:
##        i = i.strip()
##        LA.append(i)
##        
##    print(LA)
##    d.close()
##
##thread = Thread(target = EL,args=("New_FILE",))
##thread1 = Thread(target = AL,args=("w_file",))
##thread.start()
##thread1.start()
##thread.join()
##thread1.join()

##from threading import Thread
##import random
##def printt(m):
##    for i in range(0,30,1):
##        print(random.randint(0,100000))
##    if ME.is_alive():
##        print("the thread has completed the execution")
##ME = Thread(target = printt, args = (1,))
##ME.start()

##import random
##from threading import Thread
##a = []
##b = []
##c = []
##d = []
##e = []
##
##h = [chr(i) for i in range(97,123,1)]
##print(h)
##
##def LISTS(l,n):
##    for i in range(0,random.randint(0,100),1):
##        l.append(random.choice(h))
##    if n.is_alive():
##        print(l)
##
##
##T = Thread(target = LISTS, args = (a,"T"))
##T1 = Thread(target = LISTS, args = (b,"T1"))
##T2 = Thread(target = LISTS, args = (c,"T2"))
##T3 = Thread(target = LISTS, args = (d,"T3"))
##T4 = Thread(target = LISTS, args = (e,"T4"))
##T1.start()
##T.start()
##T2.start()
##T3.start()
##T4.start()




























    

