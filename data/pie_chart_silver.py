import csv

import matplotlib.pyplot as plt

golds = []

silvers = []

bronzes = []




categories = []

with open('data/OlympicsWinter.csv') as csvfile:

		reader = csv.reader(csvfile)

		line_count = 0




		for row in reader:

			if line_count is 0:

				print("Welcome to pie chart")

				categories.append(row)

				line_count += 1



			else:

				if row[4] == "USA":

					if row[7] =="Silver":

						print("won a silver medal") 
						silvers.append(row[7])




					else:

						print("won a bronze medal")

						bronzes.append(row[7])



				print(line_count)

				line_count = 1

				

print(len(silvers))


print(len(bronzes))

labels = ["Silver", "Bronze"]

size = [len(silvers), len(bronzes)]

color = ['silver', 'darkgoldenrod']

explode = (0.02, 0.02)

plt.pie(size, explode=explode, colors=color, autopct='%.1f%%', shadow=True, startangle=140)


plt.axis('equal')



plt.legend(labels, loc=1)

plt.title("Percentage Of silver, Bronze medals won by USA (1924-2014)")

plt.show()