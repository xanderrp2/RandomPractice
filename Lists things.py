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

import threading
from threading import Thread
import random
li = []
for i in range(0,5,1):
    lo = []
    for I in range(0,10,1):
        a = random.randint(1,100)
        lo.append(a)
    li.append(lo)
print(li)

def pro(List):
    a = 1
    for i in List:
        a = a*i
        
    print(a)


        
Thread1 = Thread(target=pro, args=(li[0],))
Thread2 = Thread(target = pro, args=(li[1],))
Thread3 = Thread(target = pro, args=(li[2],))
Thread4 = Thread(target = pro, args=(li[3],))
Thread5 = Thread(target = pro, args=(li[4],))
Thread1.start()
print("")
Thread2.start()
print("")
Thread3.start()
print("")
Thread4.start()
print("")
Thread5.start()
print("")
Thread1.join()
##Thread2.join()
##Thread3.join()
##Thread4.join()
##Thread5.join()

print("finished?")
