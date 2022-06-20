entered = input()
c,d = entered.split(" ")
a = int(c)
b = (int(d) + 1)
t = []
line = 0
counter = a
for i in range(0,(a - 2) ,1):
    t.append(" ")
for i in range(1,(b + 2),1):
    t.append(i)
print("Sun" + "\t"+ "Mon" + "\t"+ "Tue" + "\t"+ "Wed" + "\t"+ "Thr" + "\t"+ "Fri" + "\t"+ "Sat")
for i in range(0,(len(t) + 4),1):
    if i <= (a - 2):
        print("\t", end = "")
    else:
        if (t[i] + (a - 2))%7 == 0:
            print("\n")
    if t[i] == b:
        break
    if t[i] == " ":
        print(t[i], end = "")
    else:
        print(t[i], end = "\t")
    counter = counter + 1
