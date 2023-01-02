import numpy as np
#using numpy to make it into an array
a = np.array([20,23,82,40,32,15,67,52])
#using the numpy keyword .where() to find the even numbers of that array
x = np.where(a % 2 == 0)
print("The indices where the even number occurs are at:")
for y in x[0]:
    print(y)

#using numpy keyword .sort() to sort the array automatically
print("This is the sorted array:",np.sort(a))
#series of slicing the array in different ways (same method as slicing lists etc.)
print("This is the array sliced from index 3 onwards:", a[3:])
print("This is the array sliced from index 0 to 4:", a[0:4])
print("This is the array that only contains [32 15 67]:", a[-4:-1])