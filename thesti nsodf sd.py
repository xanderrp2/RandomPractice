a = input("do you whant to make a new file?")
import os.path
def o():
    if a == "yes" or a == "yes":
        print("what do you whant it to be named?")
        c = input()
        if os.path.isfile(c):
            print("Sorry your file name already exists.")
            o()
        K = open(c,"w")
    elif a == "no" or a == "No":
        print("what file do you whant to open?")
        i = input()
        K = open(i,"w")
o()
S = []

print("what do you whant to put in?")
D = input()


PDH = 0
V = []
HT = {}
HT = D.split(".")
lenHT = int(len(HT))
just = 0
for J in K:
    K.wite(J,just + "\n")
    just = just + 1

    if J == just:
        HT = D.split(".")
        print(HT[:])
        print("",end ="")
        V = HT[0:2]
        XV = "".join(V)
        K.write(srt(XV) +"\n")
        


K.close()
