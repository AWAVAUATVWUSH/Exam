from functions import get_even_num, randnum_gen, get_num_of_devis_by_three_in_list

print("Feldadat 1:")
num1 = get_even_num()

print("\nFeldadat 2:")
numlist:list = randnum_gen(13)
print(numlist)
devisByThree:int = get_num_of_devis_by_three_in_list(numlist)
print(f"A számok között {devisByThree} db 3-mal osztható van!")

