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
            