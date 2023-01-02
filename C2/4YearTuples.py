#given tuple
year = (2017,2003,2011,2005,1987,2009,2020,2018,2009)

#accessing the value at index -3 (third last value)
print("The third last value of the tuple is:")
print(year[-3])

#reverse tuple using "::-1" (taking one step back starting from the last value)
reverseYear = year[::-1]

#printing original tuple
print("Original tuple:")
print(year)

#printing reversed tuple
print("Reversed tuple:")
print(reverseYear)

#using .count() to figure out how many times '2009' occurred in the tuple
print("The number of times '2009' occurred in the tuple is", year.count(2009))

#using .index() to figure out the index position of '2018'
print("The year '2018' is located inside the tuple at index", year.index(2018))

#using .len() to find the length of the tuple
print("The length of the tuple is", len(year))