#given list
staff = ["Arshiya", "Usman", "Iftikhar", "Usman", "Anmol","Zainab","Iftikhar",
         "Arshiya","Jake","Iftikhar"]
print(staff)
print("Number of occurrences inside this list:")
#setting counter variables for each names in the list
countArshiya = 0
countJake = 0
countUsman = 0
countAnmol = 0
countZainab = 0
countIftikhar = 0

#using for loops to iterate through each elements inside the list and count them in the right name using if gates
for keys in staff:
    if keys == "Arshiya":
        countArshiya += 1
    elif keys == "Usman":
        countUsman += 1
    elif keys == "Jake":
        countJake += 1
    elif keys == "Anmol":
        countAnmol += 1
    elif keys == "Zainab":
        countZainab += 1
    elif keys == "Iftikhar":
        countIftikhar += 1

#using f-string to include all the counters and display them properly
print(f"Arshiya = {countArshiya}\nJake = {countJake}\nUsman = {countUsman}\nAnmol = {countAnmol}\nZainab = {countZainab}\nIftikhar = {countIftikhar}")