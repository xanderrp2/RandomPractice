total = 0
while True:
    a = input()
    if a == "x" or a == "X":
        break
    else:
        b = a.split(" ")
        print(len(b))
        total = total + len(b)
    counter = 0
    for i in a:
        counter = counter + 1
        if i =="..........":
            print(counter)
    print(str(total) +  "Total")
