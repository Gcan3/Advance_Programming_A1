#function for recurring
def pow(base, power):
    #math logic: if power is 0, then the result is 1
    if power == 0:
        return 1
    else:
        #base number times the recusive function with the power going down by 1
        return base * pow(base, power - 1)

#getting user input
base = int(input("Enter the number: "))
power = int(input("Enter the power value: "))
#displaying the output based on the given data
print(f"The value of {base} to the power of {power} is {pow(base,power)}")