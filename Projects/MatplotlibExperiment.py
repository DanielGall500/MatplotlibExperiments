import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,9,11]
y2 = [7,8,2,4,2]

fig1 = plt.bar(x, y, label='Bars1', color='r')
fig1.plt.bar(x2, y2, label='Bars2', color='b')

population_ages = [1,44,56,2,22,4,55,44,65,66,88,5,56,67,8,5,40,99,78,65,53]

ids = [x for x in range(len(population_ages))]

bins = [1,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages, bins, histtype='bar')


plt.xlabel('X')
plt.ylabel('Y')
plt.title('Title')

plt.grid(True)

fig1.show()