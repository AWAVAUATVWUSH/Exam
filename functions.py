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

def print_character_in_text(instring:str="", charToCheck:int=0):
    i:int = 0
    iMax:int = len(instring)
    if(iMax>=charToCheck):
        print(f"A szöveg {charToCheck}. karaktere {instring[charToCheck-1]} - {instring[charToCheck-1].upper()}{instring[charToCheck-1].upper()}{instring[charToCheck-1].upper()}")
    else:
        print(f"A szöveg nem tartalmaz {charToCheck}. karaktert")

def get_names_amount():
    numOfNames:int = 0
    while(True):
        name:str = input("Adj meg egy nevet vagy írj '@' a befejezéshez: ")
        if(name != '@'):
            numOfNames+=1
        else:
            return numOfNames
        
def play_rock_paper_scissors():
    listOfOptions:list = ["kő","papír","olló"]
    userpick:str = ""
    computerpick:str = listOfOptions[int(random.random()*3)]

    print("Játszunk kő papír ollót.")
    while(userpick != "kő" and userpick != "papír" and userpick != "olló"):
         userpick = input("Válassz! (Kő, Papír, Olló): ").lower()
    if(userpick == computerpick):
        print("Döntetlen!")
    elif((userpick == "kő" and computerpick == "olló") or (userpick == "papír" and computerpick == "kő") or (userpick == "olló" and computerpick == "papír")):
        print("Te nyertél!")
    else:
        print("Sajnos vesztettél")
