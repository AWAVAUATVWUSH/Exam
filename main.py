from functions import get_even_num, randnum_gen, get_num_of_devis_by_three_in_list, print_character_in_text, get_names_amount, play_rock_paper_scissors

print("Feldadat 1:")
num1 = get_even_num()

print("\nFeldadat 2:")
numlist:list = randnum_gen(13)
print(numlist)
devisByThree:int = get_num_of_devis_by_three_in_list(numlist)
print(f"A számok között {devisByThree} db 3-mal osztható van!")

print("\nFeladat 3:")
print_character_in_text("Megeszem a kalapom", 3)

print("\nFeladat 4:")
print(f"A felhasználó {get_names_amount()} nevet adott meg")

print("\nFeladat 5:")
play_rock_paper_scissors()