import matplotlib.pyplot as plt

names = ["ali", "maryam", "mehrac", "muslum", "nargiz"]
less_than_6 = 0
more_than_6 = 0

for name in names:
    if len(name) < 6:
        less_than_6 += 1
    else:
        more_than_6 += 1

colors = ['red', 'green']
sizes = [less_than_6, more_than_6]
labels = ['Shorter', 'Longer']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.show()
