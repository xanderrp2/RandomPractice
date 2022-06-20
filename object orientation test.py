##class test:
##    def __init__(self,name,ident,date):
##        self.name = name
##        self.ident = ident
##        self.date = date
##    def lift(self):
##        print(self.name)
##        print(self.ident)
##        print(self.date)
##card = test("xander",1871,1904)
####print(card.name)
####print(card.ident)
####print(card.date)
##tag = test("r",8371,1184)
####print(tag.name)
####print(tag.ident)
####print(tag.date)
##card.lift()
##tag.lift()
##class bank:
##    def __init__(self,name,accountNumber,bal):
##        self.name = name
##        self.accountNumber = accountNumber
##        self.bal = bal
##    def withdraw(self):
##        print("do you want to withdraw?")
##        a = input()
##        if a == "yes":
##            print("how much")
##            b = int(input())
##        self.bal = self.bal - b
##    def print(self):
##        print(self.name)
##        print(self.accountNumber)
##        print(self.bal)
##
##    
##
##acount = bank("ian",19958,3000)
##print(acount.name)
##print(acount.accountNumber)
##print(acount.bal)
##acount.withdraw()
##acount.print()
##class shopping():
##    def __init__(self,shop):
##        self.Slist = {}
##        self.shop = shop
##    def add(self):
##        for i in range(0,5,1):
##            print("do you whant to add items?")
##            ku = input()
##            if ku == "yes":
##                print("what do you whant to add?")
##                hu = input()
##                print("how many do you whant to add?")
##                amu = int(input())
##                self.Slist[hu] = amu
##        return self.Slist
##        
##    
##
##    def EDit(self):
##        print("do you whant to add or subtract anything?")
##        a = input()
##        if a == "yes" or a == "Yes":
##            print("what do you whant to change")
##            b = input()
##            print("how many do you whant to change?")
##            amount = int(input())
##            if self.Slist[b] == 1:
##                del (self.Slist[b])
##            else:
##                self.Slist[b] = self.Slist[b] - amount
##                
##            print(self.Slist)
##
##sheet = shopping("forteen_os")
##print(sheet.add())
##sheet.EDit()
##import random
##
##class phonebook():
##    numbers = {}
##    def __init__(self,numbers):
##        self.numbers = numbers
##        self.self = name
##
##    def add():
##        while True:
##            print("do you whant to add anyone to you phoneBook?")
##            a = input()
##            if a == yes:
##                print("who do you whant to add?")
##                b = input()
##                print("what is there number?")
##                k = int(input())
##                if b in numbers and k in numbers:
##                    print("this person is already in your phoneBook")
##                    print("do you whant to continue?")
##                    hshd = input
##                    if hshd == no:
##                        break
##                else:
##                    numbers[b] = k
##                    print(numbers)
##                    break
##    def rem():
##        his = random.randint(1,10000)
##        print("do you whant to remouve some one?")
##        hus = input
##        if hus == yes:
##            print("who do you whant to remouve")
##            remu = input()
##            if remu in numbers:
##                print("are you sure that you whant to remouve this personne")
##                print("if so enter this number", his)
##                hsm = int(input())
##                if hsm == his:
##                     del numbers[remu]
##        print(numbers)
##book = phonebook()
##book.add()
##book.rem() 
##class market():
##    def __init__(self,name,times):
##        self.name = name
##        self.times = times
##        self.item = {}
##    def items(self):
##        print("what do you whant in you store?")
##        aa = input()
##        print("how much?")
##        kk = int(input())
##        self.item[aa] = kk
##        print(self.item)
##        print("do you whant to add anything else?")
##        add = input()
##        if add == "yes":
##            self.items()
##        
##        
##    def sell(self):
##        print(self.item)
##        print("what do you whant to buy?")
##        a = input()
##        print("how much do you whant to buy?")
##        k = int(input())
##        if a in self.item:
##            print(self.item[a])
##            self.item[a] = self.item[a] - k
##            print(self.item)
##        else:
##            print("sorry we dont have any of those here.")
##    def returns(self):
##        print("would you like to return somthing?")
##        ut = input()
##        if ut == "yes":
##            print("is your item a dary product?")
##            husk = input()
##            if husk == "no":
##                print("what do you what to return?")
##                ku = input()
##                
##            
##                if ku in self.item:
##                    print("how many are you returning")
##                    hu = int(input())
##                    self.item[ku] = self.item[ku] + hu
##                    print(self.item)
##            else:
##                print("sorry you cannot return this item here.")
##            
##
##
##seveneleven = market("seveneleven","9-11")
##seveneleven.items()
##seveneleven.sell()
##seveneleven.returns()
##class Zoo():
##    def __init__(self):
##  ##      self.self = name
##        self.food = {}
##        self.animals = {}
##        self.habitats = {}
##    def add(self):
##        print("do you whant to add any animals?")
##        a = input()
##        if a == "yes":
##             print("what animal are you looking for?")
##             an = input()
##             print("how many animals are you adding?")
##             fan = int(input())
##             self.animals[an] = fan
##             print(self.animals)
##
##        
##        print("do you whant to add any food?")
##        b = input()
##        if b == "yes":
##            print("hi")
##            print("what animal are you looking for?")
##            san = input()
##            print("how much food are you adding?")
##            sfan = int(input())
##            self.food[san] = sfan
##            print(self.food)
##
##        
##        print("do you whant to change the habitats?")
##        k = input()
##        if k == "yes":
##            print("wich animals habitat are you changing?")
##            kue = input()
##            print("what are you changing it to?")
##            hue = input()
##            self.habitats[kue] = hue
##            print(self.habitats)
##        
##    def remove(self):
##        print("do you whant to remove any animals?")
##        a = input()
##        if a == "yes":
##            print("what animal are you looking for?")
##            an = input()
##            print("how many animals are you removing?")
##            fan = int(input())
##            if fan = 0:
##                del self.animals[an]
##                del self.food[an]
##                del self.habitats[an]
##            else:
##                self.animals[an] = fan
##            print(self.animals)
##
##        
##        print("do you whant to remove any food?")
##        b = input()
##        if b == "yes":
##            print("hi")
##            print("what animal are you looking for?")
##            san = input()
##            print("how much food are you removing?")
##            sfan = int(input())
##            self.food[san] = sfan
##            print(self.food)
##
##        
##        print("do you whant to change the habitats?")
##        k = input()
##        if k == "yes":
##            print("wich animals habitat are you changing?")
##            kue = input()
##            print("what are you changing it to?")
##            hue = input()
##            self.habitats[kue] = hue
##            print(self.habitats)                    
##     
##        
##
##
##Luke = Zoo()
##Luke.add()
##class parent():
##    def last_name(self):
##        print("rutherford-parish")
##class child(parent):
##    def first_name(self):
##        print("xander")
##    ##def last_name(self):
##       ## print("bananaman")
##kid = child()
##kid.last_name()
##class mario():
##    def me(self):
##        print("its a me a mario.")
##
##class shrooms():
##    def eat(self):
##        print("big chungus")
##class big_mario(mario,shrooms):
##    
##    pass
##uno = big_mario()
##uno.me()
##uno.eat()
       
    



























