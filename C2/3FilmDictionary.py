#setting up the dictionary
films = {"Name" : "avengers",
         "Director" : "joss whedon", 
         "Rating" : "10/10"}

#using for loop to iterate through the keys and values inside the dictionary (with the help of .items())
for key,values in films.items():
    #using .title() to keep proper nouns capitalized at the first letter
    print(f"{key}: {values.title()}")