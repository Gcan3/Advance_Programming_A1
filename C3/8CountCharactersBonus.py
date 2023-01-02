string = input("Enter word(s): ")

#setting up counters and text values for vowels and consonants
vcount = 0
ccount = 0
scount = 0
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

#using for loop to iterate through the user's string input
for x in string.lower():
    if x in vowels:
        vcount += 1
    elif x in consonants:
        ccount += 1
    else:
        scount += 1

#printing the counts of every values inside the entered string
print(f"Length of string: {len(string)}\nVowels inside the string: {vcount}\nConsonants inside the string: {ccount}\nSpecial characters inside the string: {scount}")