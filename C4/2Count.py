#setting counter variable
count = 0
#opening the text file
with open('sentences.txt') as file_handler:
    #creating a for-loop to read every line of the text
    for lines in file_handler.readlines():
        #for every line in the text, they are verified wether they are the same sentences
        #using .strip() function to remove attached whitespaces of the line to properly verify the line
        if lines.strip() == 'Hello my name is Amster Sani':
            count += 1
        else:
        #continuing the loop until it has ran out of lines to read
            continue

#displaying the final count
print("The number of times the sentence 'Hello my name is Amster Sani' occured is", count)