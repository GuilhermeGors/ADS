
# ex_semana3_vogal_consoante

vogals = ["a","e","i","o","u"]
consonants = ["b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
print("\n==========\nvogal validation\n==========")
letter = str(input("Enter any letter: "))

if letter not in vogals and letter not in consonants:
    print("That's not a letter!!")
elif letter  in vogals:
    print("That's a vogal!!")
    
elif letter in consonants:
    print("That's a consonant!!")
    
else: 
    print("What you have done??")