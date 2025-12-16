def letter():
    a = input("Enter an alphabet character: ").lower()   # <-- MUST use () after lower
    
    if a in "aeiou":
        print("This is a vowel")
    else:
        print("This is a consonant")

letter()
