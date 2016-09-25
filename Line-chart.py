import matplotlib.pyplot as plt
import csv
x=[]
y= []
array =[]
data = list(csv.reader(open('/Users/samir/PycharmProjects/Scatterplot/First ETA - SG.csv')))
numrows = len(data)
print 'numrows = ' + str(numrows)
for row in range(numrows):
    x = data[row][1]
    y = data[row][2]
    array.append([x,y])
print array
plt.plot(array, 'ro')
plt.axis([0, 50, 0, 2])
plt.ylabel('rides/hr/dax')
plt.xlabel('payout/hr/dax')
plt.show()