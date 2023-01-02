print("Hello, this will print all even numbers!")
#setting up an integer variable starting from 0
x = 0
while x <= 100:
    #advance the number by 1 first before proceeding
    x += 1
    #if divisible by 2, then print the number
    if x % 2 == 0:
        print(x)
    #else, reiterate the loop with the same number
    else:
        continue