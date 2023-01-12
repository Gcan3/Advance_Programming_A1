#taking user's input
name = input("Input your name: ")
age = input("Input your age: ")
hometown = input("Input your hometown: ")

#adding the user's input into the file
with open('bio.txt', 'w') as file_handler:
    file_handler.write(f"Name: {name.title()}\n")
    file_handler.write(f"Age: {age}\n")
    file_handler.write(f"Hometown: {hometown.title()}")

#displaying the text file contents 
print("\nInformation about you:")
with open('bio.txt') as f:
    for line in f:
        print(line)
