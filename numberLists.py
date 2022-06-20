b = []
k = int(input())
NumberOfLines = k
b.append(k)
for i in range(0,k,1):
    a = int(input())
    b.append(a)
b.sort()
for i in range(0,len(b),1):
    print(int(b[i]))
