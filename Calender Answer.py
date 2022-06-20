
   
entered = input()
startDay,monthLength = entered.split(" ")
startDayint = int(startDay)
monthLengthInt = (int(monthLength) + 1)
daysList = []
counter = startDayint
for i in range(0,(startDayint - 2) ,1):
    daysList.append(" ")
for i in range(1,(monthLengthInt + 2),1):
    daysList.append(i)
print("Sun" + "\t"+ "Mon" + "\t"+ "Tue" + "\t"+ "Wed" + "\t"+ "Thr" + "\t"+ "Fri" + "\t"+ "Sat")
for i in range(0,(len(daysList) + 4),1):
    if i <= (startDayint - 2):
        print("\t", end = "")
    else:
        if (daysList[i] + (startDayint - 2))%7 == 0:
            print("\n")
    if daysList[i] == monthLengthInt:
        break
    if daysList[i] == " ":
        print(daysList[i], end = "")
    else:
        print(daysList[i], end = "\t")
    counter = counter + 1
