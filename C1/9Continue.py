#setting a counter 
count = 1
#executing a loop immediately 
while True:
    #getting user's input
    ans = input("press y to continue: ")
    #if the user doesn't type "y", increment the count and continue the loop 
    if ans == "y" or ans == "Y":
        count += 1
        continue
    #otherwise, break the loop
    else:
        break

#display the counter for the number of times the loop executed
print(f"The loop is finished and has executed {count} times")