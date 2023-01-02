#making dictionary about three cities with three information (country, population, and fact)
cities = {"Al Ain's country" : "United Arab Emirates",
          "Al Ain's population" : "634,000",
          "Al Ain's fact" : "Second largest city in the country",
          "New York's country" : "United States of America",
          "New York's population" : "18,867,000",
          "New York's fact" : "City that never sleeps",
          "Paris's country" : "France",
          "Paris's population" : "2,140,000",
          "Paris's fact" : "Best tourist city in the world"}

print("Information about three cities (Al Ain, New York, and Paris:)")
#printing the keys and values using for loop
for keys,values in cities.items():
    print(f"{keys} : {values}\n")