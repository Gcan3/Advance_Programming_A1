#opening the file
with open('sentences.txt') as file_handler:
    #storing the contents inside a variable using .read()
    texts = file_handler.read()

#splitting the contents inside the file into individual words
#this will be stored in a list in a new variable
newTexts = texts.split()

#creating an empty dictionary for storing the letters
letterDict = {}

#getting through every word stored by the list
for i in newTexts:
    #iterate through each letters of every word
    for letter in i:
        #if the letter is in the dictionary, increment the value by 1
        if letter in letterDict:
            letterDict[letter] += 1
        #else, set it as new key with a value of 1
        else:
            letterDict[letter] = 1

print("The number of occurrences of each letter in the file:")

#deleting the symbols from the dictionary to not include it inside the count
del letterDict["."]
del letterDict[","]
del letterDict["'"]
del letterDict["?"]
del letterDict['"']
del letterDict["!"]
#displaying the list using for-loop to iterate through each keys and its values
for key in letterDict.keys():
    print(f"{key} : {letterDict[key]}")