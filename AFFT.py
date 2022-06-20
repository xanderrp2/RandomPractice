from AFF import *
print("do you whant to calculate a 1.Rectangle 2.Triangle 3.Cercle 4.Cube")
UI = input()
if UI == "1":
    print("what is the length?")
    L = int(input())
    print("what is the hight?")
    H =int(input())
    RA = R(L,H)
    print(RA)
elif UI == "2":
    print("what is the length?")
    L = int(input())
    print("what is the hight?")
    H =int(input())
    TA = T(L,H)
    print(TA)

elif UI == "3":
    print("what is your radius?")
    R = int(input())
    CA = C(R)
    print(CA)
elif UI == "4":
    print("what is your length?")
    L = int(input())
    
    CBA = CB(L)
    print(CBA)
else:
    print("go someware else")

