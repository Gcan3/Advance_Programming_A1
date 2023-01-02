#creating an empty list
numList = []
#opening the text file and storing it inside a variable
with open("numbers.txt") as file_handler:
    #iterate through every lines inside the text file
    for lines in file_handler.readlines():
        #add each of the lines inside the empty list using .append()
        #stripping the lines too to avoid including whitespaces
        numList.append(lines.strip())

#making a for loop to display contents inside the list as integers
print("The numbers inside the list:")
for num in numList:
    #making it in int format
    print(int(num))