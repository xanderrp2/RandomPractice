##while True:
##    def FIND(NUMBER,LIST):
##        for i in range(len(LIST)):
##            if NUMBER == LIST[i]:
##                return i
##        return -1
##    print("what number are you looking for?")
##    A = int(input())
##    M = [10,20,30,2,4,5,6,7,111,44,56,43,23,67,54]
##    g = FIND(A,M)
##    if g == -1:
##        print("number not found")
##    else:
##        print(g)
##        print("NUMBER FOUND")
##Q = 0
##O = []
##R = [7777,8,7,6,5,4,3,2,1]
##while True:
##    print("what number are you looking for?")
##    A = int(input())
##    def BINARY(LIST,NUMBER):
##        MIN = 0
##        for I in LIST:
##            Q = Q + LIST[I]
##        R.sort()
##        
##        MAX = Q
##        while MIN<=MAX:
##            MID = (MAX+MIN)//2
##            if NUMBER == LIST[MID]:
##                print("working")
##                print("FOUND YOUR NUMBER", LIST[MID])
##                return MID
##            elif NUMBER > LIST[MID]:
##                print("working1")
##                MIN = MID + 1
##                print(MIN, " " ,MID)
##            elif NUMBER < LIST[MID]:
##                print("working2")
##                MAX = MID - 1
##        return -1
##                
##    G = BINARY(R,A)
##    if G == -1:


##R = [5,3,4,2,1]
##while True:
##    for A in range(len(R)):
##        for i in range(len(R)):
##            if i == len(R)-1:
##                R = R
##            elif R[i] >= R[i + 1]:
##                
##                R[i],R[i+1] = R[i+1],R[i]
##                print(R)

##R = [5,3,4,2,1]
##while True:
##    for A in range(len(R)-1,0,-1):
##        for i in range(A):
##            if R[i] >= R[i + 1]:
##                
##                R[i],R[i+1] = R[i+1],R[i]
##                print(R)


##R = [5,3,4,2,1,6,5,4,8,1234,65,234567,6543,78,987,54]
##Min = 0
##while True:
##    for A in range(len(R)):
##        Min = A
##        for I in range(A+1,len(R),1):
##            if R[Min] > R[I]:
##                Min = I
##        R[A],R[Min] = R[Min],R[A]
##        print(R)

##R = [4,2,1,5,3]
##q = int
##counter = 0
##while True:
##    for i in R:
##        print(i)
##        if i == len(R):
##            print("broken")
##        elif i >= R[counter+1]:
##            counter = counter + 1
##            q = i
##            print("working")
##            print(R)
##            for l in range(0,len(R),-1):
##                if q <= R[l]:
##                    print("less")
##                    print(R)
##                elif q >= R[l]:
##                    print(R)
##                    R[i].pop()
##                    R.insert(l,q)
##        if R == R.sort():
##            break

##
##
##R = [1,65,4,3,4,5,6,7,76,5432,34,567,876543,23,456,7654,34]
##
##def Sort(R):
##    for i in range(1,len(R),1):
##        A = i-1
##        while R[A] >= R[A+1] and A >= 0:
##            R[A],R[A+1] = R[A+1],R[A]
##            A = A -1
##            print(R)
##
##Sort(R)

##def Factorial():
##    print("please enter your number")
##    a = int(input())
##    m = []
##    c = 0
##    b = 1
##    for i in range(0,a,1):
##        c = c + 1
##        m.append(c)
##    for i in range(0,len(m),1):
##        b = b*m[i]
##    print(m)
##    print(b)

##def fore(Number):
##    if Number == 1:
##        return 1
##    else:
##        return Number*fore(Number-1)
##a = int(input())
##print(fore(a))

##def add(Number):
##    if Number <= 10:
##        return Number
##    else:
##        print(Number)
##        return ((Number%10) + add(Number//10))
##    
##a = int(input())
##print(add(a))

##def Reverse(String):
##    if len(String) == 0:
##        return String
##    else:
##        a = String[1:]
##        b = String[0]
##        return Reverse(a)+b
##c = input()
##print(Reverse(c))







##print(1)
##layer = [1, 1]
##layers = 1
##while layers < 10:
##    for elem in layer:
##        print(elem,end='h')
##    print()
##    new_layer = []
##    for i in range(len(layer)-1):
##        num1 = layer[i]
##        num2 = layer[i+1]
##        new_layer.append(num1 + num2)
##    new_layer=[1] + new_layer + [1]
##    layer=new_layer
##    layers+=1

##print(1)
##R = [1,1]
##count = 1
##while count<10:
##    for i in R:
##        print(i,end=' ')
##    print("")
##    new_layer = []
##    for I in range(len(R)-1):
##        Num1 = R[I]
##        num2 = R[I+1]
##        new_layer.append(Num1 + num2)
##    new_layer=[1] + new_layer + [1]
##    R = new_layer
##    count = count + 1
##        


##print(1)
##R = [1,1]
##Number = 1
##def Tri(Number):
##    global R
##    if Number > 10:
##        return 0
##    if Number < 10:
##        for i in R:
##            print(i,end=' ')
##        print("")
##        new_layer = []
##        for I in range(len(R)-1):
##            Num1 = R[I]
##            num2 = R[I+1]
##            new_layer.append(Num1 + num2)
##        new_layer=[1] + new_layer + [1]
##        R = new_layer
##    return Tri(Number + 1)
##
##Tri(Number)

##print(1)
##R = [1,1]
##Number = 1
##def Tri(R):
##    global R
##    if len(R) > 10:
##        return 0
##    if len(R) < 10:
##        for i in R:
##            print(i,end=' ')
##        print("")
##        new_layer = []
##        for I in range(len(R)-1):
##            Num1 = R[I]
##            num2 = R[I+1]
##            new_layer.append(Num1 + num2)
##        new_layer=[1] + new_layer + [1]
##        R = new_layer
##    return Tri(R = new_layer)
##
##Tri(R)



##from math import factorial
##
##a = 6
##for i in range(0,5,1):
##    for I in range(0,(6-i+1),1):
##        print(end = "")
##    for A in range(0,i+1,1):
##        print(factorial(i)//(factorial(A)*factorial(i-A)),end="")
##    print("")


##from math import factorial
##
##def Try(number):
##    if number > 6:
##        print("done")
##    else:
##        for A in range(0,number+1,1):
##            print(factorial(number)//(factorial(A)*factorial(number-A)),end=" ")
##        print("")
##        return Try(number+1)
##
##Try(0)
##        

##
##import threading
##
##def funthing(Number):
##    for i in range(0,Number-1,1):
##        print("something")
##
##a = threading.Thread(target = funthing,args = (7,))
##a.start()
##a.join()
##print("thread completed")
##
##
##import threading
##
##def thing(Number):
##    for i in range(0,Number,1):
##        print("Hello world")
##
##def Other(newNumber):
##    for I in range(0,newNumber,1):
##        print("Bye world")
##
##a = threading.Thread(target = thing,args = (5,))
##b = threading.Thread(target = Other,args = (3,))
##a.start()
##a.join()
##b.start()
##b.join()
##
##print("both threads completed")


##from threading import Thread
##def prime_checker(num):
##    prime = True
##    for d in range(2, int(num**0.5) + 1, 1):
##        print('{} checked with {}'.format(num, d))
##        if num % d == 0:
##            prime = False
##        if prime == True:
##            print('{} is a prime number'.format(num))
##        else:
##            print('{} is a not prime number'.format(num))
##def primes(numbers):
##    for num in numbers:
##        t = Thread(target=prime_checker, args=(num,))
##        t.start()
##        t.join()
##        print('Completed check for {}!'.format(num))
##
##            
##prime_thread = Thread(target=primes, args=([4483, 4493], ))
##prime_thread.start()
##prime_thread.join()
##print('The program ended')

##from threading import Thread
##from time import sleep
##letters = ['A', 'B', 'C', 'D']
##def func():
##    for letter in letters:
##        print(letter)
##        sleep(2)
##
##thread = Thread(target=func)
##thread.start()
##print('E')

import random

li = []
lo = []
for i in range(0,4,1):
    for a in lo:
        lo.remove(a)
    for I in range(0,99,1):
        a = random.randint(0,100)
        lo.append(a)
    li.append(lo)
print(li)
