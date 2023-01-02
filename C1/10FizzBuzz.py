print("Hello, this will print all numbers but divisible by 3 as Fizz, by 5 as Buzz, and by both as FizzBuzz!")
#starting with a integer variable 1
num = 1
#while loop executes while the variable is still below 101
while num < 101:
    #if gates to verify if the number is both divisible by 3 and 5
    #it is placed first so that other "ifs" won't execute before the "FizzBuzz" (tested)
    if (num % 3 == 0) and (num % 5 == 0):
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
    #add the number for the next verification iteration
    num += 1