#importing regex library
import re
#setting patterns for verification and a variable for counting attempts
patternsCharlower = '[a-z]'
patternsCharhigher = '[A-Z]'
patternsInt = '[0-9]'
patternsSpec = '[$, @, #]'
attempts = 5
#giving user rules before entering password
print("Hello user, to proceed, please enter your password.")
print("It must contain at least:\n1. One lower case letter\n2. One capital letter\n3. Anyone of these special characters: $, @, #\n4. Be at the minimum length of 6 and maximum of 12 characters")

#using while loop as long as there are still attempts for the user
#kicks the user out of this loop otherwise
while attempts > 0:
    #get user input every time the loop triggers
    password = input("Enter your password correctly: ")
    
    #in these series of if gates,
    #1- 'if/elif not' is used to easily verify a series of checks
    #2 - re.search() is used to check if the input is eligible on the pattern
    #3 - if it does NOT check any one of the rules, decrement the attempt and continue the loop again
    if len(password) < 6 and len(password) > 12:
        attempts -=1
        print(f"Incorrect password. Attempts left: {attempts}")
        continue
    elif not re.search(patternsCharlower, password):
        attempts -=1
        print(f"Incorrect password. Attempts left: {attempts}")
        continue
    elif not re.search(patternsCharhigher, password):
        attempts -=1
        print(f"Incorrect password. Attempts left: {attempts}")
        continue
    elif not re.search(patternsInt, password):
        attempts -=1
        print(f"Incorrect password. Attempts left: {attempts}")
        continue
    elif not re.search(patternsSpec, password):
        attempts -=1
        print(f"Incorrect password. Attempts left: {attempts}")
        continue
    elif re.search("\s", password):
        attempts -=1
        print(f"Incorrect password. Notice: No whitespaces. Attempts left: {attempts}")
        continue
    #4 - if it DOES check all of the rules, the loop will break and proceed with the next function
    else:
        break

#if gates depending on the attempts of the user
#the first if gate has a condition to alert all authorities when the user is out of attempts
if attempts == 0:
    print("You have ran out of attempts and the authorities are alerted!")
#else, the user would still have 1 or more attempts to proceed in this condition
else:
    print("You have entered the correct password (5 checks), welcome user!")