while True:
    a = int(input())
    k = a
    b = 0
    if a%2 == 0 or a%5 == 0:
        for i in range(0,int(a/4),1):
            for k in range(0,int(a/5),1):
                if (i*4) + (k*5) == a:
                    b = b + 1
    elif a%5 == 0:
        for i in range(0,a,1):
            for k in range(0,a,1):
                if (i*4) + (k*5) == a:
                    b = b + 1
    else:
        b = 1
        
    if a == 6 or a == 3 or a == 7 or a == 1 or a == 2 or a == 11:
        b = 0
            
        




        
            
    print(b)
