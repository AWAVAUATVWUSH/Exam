import random

def get_even_num():
    while(True):
        try:
            num:int = int(input("Adj meg egy páros egész számot: "))
            if(num%2==0):
                return num
            else:
                print("A megadott szám nem páros. Páros számot kérek: ")
        except ValueError:
            print("Helytelen input!")

def randnum_gen(numOfNums:int = 0):
    numlist:list = []
    i:int = 0
    while(i<numOfNums):
        numlist.append(int(random.random()*161-10))
        i+=1
    return numlist

def get_num_of_devis_by_three_in_list(inlist:list = []):
    numToRet:int = 0
    i:int = 0
    iMax:int = len(inlist)
    while(i<iMax):
        if(inlist[i]%3==0):
            numToRet+=1
        i+=1
    return numToRet
