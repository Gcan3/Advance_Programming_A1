import matplotlib.pyplot as plt
fig = plt.figure()
pollans = ['Game', 'Commercials', "Won't watch"]
male = [279, 81, 132]
female = [200, 156, 160]

tick_label = ['Game', 'Commercials', "Won't watch"]
color = ['skyblue', 'lightgreen', 'lightblue']

plt.bar(pollans, male, color='lightblue')
plt.bar(pollans, female, bottom= male, color='purple')

plt.xlabel('Poll Questions')
plt.ylabel('Number of Americans aged 18 and over')

plt.title('Answers to the poll')

plt.show()