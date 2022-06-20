
##while True:
##    print("please enter a string")
##    k = input()
##    a = list(k)
##    print(a)
##
##a = ["h","j","k"]
##for i in range(0,len(a),1):
##    print(a[i])
##a = {"a":0,"b":2,"o":3,"r":4,"t":5}
##print("please enter a word")
##o = input()
##a["r"] = a["r"] + 4
##del(a["a"])
##a.pop("o")
##print(a)
##for i in a:
##    print(a[i])
##print(a.values())
import random
##b = []
##def a():
##    k = random.randint(1,20)
##    b.append(k)
##
##for i in range(0,5,1):
##    a()
##print(b)
##def p(a,s,d,g):
##    y = (a + s + d + g)/4
##    print(y)
##
##p(3,6,5,4)
##def p():
##    print("please enter a price.")
##    a = int(input())
##    print("please enter a tax percentage.")
##    b = float(input())
##    k = a-((b/100)*a)
##    return k
##
##print(p())
a = 5
def p():
    global a
    a = a + 5
    return a
print(p())
    
    
































