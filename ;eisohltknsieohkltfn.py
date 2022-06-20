a = 5
def b():
    global a 
    a = a + 5
    return a
for i in range (0,3,1):
    b()
    print(a)
