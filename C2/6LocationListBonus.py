#given list
locations =['dubai','paris', 'switzerland', 'London', 'amsterdam', 'New York']

#displaying the list (using for-loop) and the length of the list (using len())
print("List of locations:")
for x in locations:
    print(x.title()) #.title to capitalize the first letter of each location names
print("\nThe length of this list is", len(locations))


#using .sorted() to properly sort the list
print("\nSorted list of locations (alphabetical order):")
#since sorted lists prioritizes capitalized words, lambda function as the key is used
#this is to convert all values inside the list to all lower case begin sorting it properly
for x in sorted(locations, key = lambda y : y.lower()):
    print(x.title())

#printing original for proof of no modifications
print("\nUnmodified list of locations:",locations)

print("\nReversed alphabetical order of the locations:")
#print alphabetical list but reversed order using reverse=True
for x in sorted(locations, key = lambda y : y.lower(), reverse=True):
    print(x.title())
    
#printing original for proof of no modifications
print("\nUnmodified list of locations:",locations)

#modifying to a reversed order list
locations.reverse()
print("Reversed list:", locations)

#modifying to an alphabetically ordered list
locations.sort(key = lambda y : y.lower())
print("Alphabetically sorted list:",locations)

#modifying to an alphabetically reversed order list
locations.sort(key = lambda y : y.lower(), reverse=True)
print("Alphabetically reversed list:", locations)