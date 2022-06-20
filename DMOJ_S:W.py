a = int(input())
values = []
for i in range(0,a,1):
    o = input()
    b = o.split(" ")
    values.append(b)

for i in values:
    if int(i[0])*int(i[1]) != int(i[2]):
        print("16 BIT S/W ONLY")
    else:
        print("POSSIBLE DOUBLE SIGMA")
