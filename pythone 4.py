##print("what is your age?")
##Age = int(input())
##print("what is your grade?")
##Grade = int(input())
##
##if Age >= 8 and Grade >= 3 :
##    print("you can play this game")
##else :

##if n > Y:
##    print("where do you live?")
##A = input()
##if A == "California" or A == "Oregon" or A == "Washington" :
##    print("We suggest you go for a coastal drive")
##
##else :
##    print("You may be better off skiing")

##for i in range (0,21,1):
##    if i % 2 == 0:
##        print(i,"i = even")
##
##    else :
####        print(i,"i = Odd")
##import time 
##for i in range (4,0,-1):
##    print(i)
##    time.sleep(1)
##
##print("BLAST OFF!")

##
##for i in range(1,5,1):
##    
##
##    for j in range(1,6,1):
##        print("*",end = ' ')
##
##    print()
##    print()
##
##for i in range(1,5,1):
##    print("*"* i)
##    print()

##for i in range(100,0,-3):
##    
##    if 30 > i > 20:
##        print("tick tock")
##    else:
##        print(i)
##for b in range(0,3,1):
##    for a in range(0,3,1):
##        for i in range(0,8,1):
##            print("*",end="")
##            print()
##        print()
##    print()
##
##import random
##A = 0
##for i in range(1,21,1):
##    B = random.randint(1,100)
##    A = A + B
##    print(B,i)
##print(A)
##    

##
##import random
##A = 0
##D = 0
##Y = 0
##C = 0
##for i in range(1,21,1):
##    B = random.randint(-20,20)
##    print(B,i)
##    if 0 > B:
##         D = D + B
##         Y += 1
##    else:
##        A = A + B
##        
##
##C = D / Y
##print("posative",A)
##print("negative",C)
        

##print("hello can u give me a string?")
##A = input()
##B = 0
##for i in A:
##    print(i,B)
##    B += 1


##n = 1
##while n <= 50:
##    print(n)
##    n = n + 1

##import time
##import random
##
##while True:
##    time.sleep(3)
##    A = random.randint(1,1000)
##    B = random.random()
##    print(A)
##    print(B)
 
##import time
##A = 5
##while A >= 2:
##    time.sleep(1)
##    A = A - 1
##    print(A)
##time.sleep(1)
##print("Blast Off")

##import random
##import time
##print("how much would you like to deposit?")
##bal = int(input())
##
##
##def roll():
##    
##
##    while True:
##        print("do you whant to roll a dice?")
##        YN = input()
##        if YN == "y" or YN == "Y":
##            di1 = random.randint(1,6)
##            di2 = random.randint(1,6)
##            print("waiting a few seconds")
##            time.sleep(2)
##            if di1 == di2:
##                print("you won and your acount will be increast by 5$")
##                bal =+ 5
##            else:print("sorry you lost and your acount will be decreased by 1$")
##            bal =- 1
##            print("your bal = ",bal)
##               
##    
##        if 1 > bal:
##            print("thank you for playing")
##            break
##        elif YN == "n" or YN == "N":
##            print("thank you for your time")
##            
##            print(bal)
##            break
##
##roll()
##import random
##A = 1
##while True:
##    number = random.randint(100,999)
##
##    if number % 23 == 0:
##        print(number)
##        break
##    else:
##        A = A + 1
##        print(number,A)
## 
##while True:
##    print("what is the password")
##    A = input()
##    if A == "3o01":
##        print("AcCess Granted")
##        break
##    else:
##        print("Access Denied")
import random
I = 0
A = random.randint(20,30)
while True:
    print("what is the number?")
    b = int(input())
    
    if b == A:
        print("you got it correct")
        print(I)
        break

    else:
        I = I + 1
        print("your incorect")


        
        
        
    
    












