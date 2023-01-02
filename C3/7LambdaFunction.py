#given list
marks = [("CodeLab I",67),
         ("web Development", 75),
         ("CodeLabII",74),
         ("Smartphone Apps",68),
         ("Games Development",70),
         ("Responsive web",65)]

#using the sorted() function with the help of lambda (using the second index of the tuple as a key for sorting) 
#this is to organize the list based on marks
#storing it inside another variable
#printing the sorted list from lowest marks to highest marks
print("Lowest to highest marks:")
sortMark = sorted(marks, key=lambda x : x[1])
print(sortMark)

#printing the sorted list from highest marks to lowest marks by simply reversing the sorted list
print("Highest to lowest marks:")
rsortMark = sorted(marks, key=lambda x: x[1], reverse=True)
print(rsortMark)