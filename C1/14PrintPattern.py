#for every row starting from 1 and ending to 7...
for x in range(1, 7):
    #...the number increments by 1 and is displayed next to it
    for y in range(1, x):
        print(y, end=" ")
    print("")