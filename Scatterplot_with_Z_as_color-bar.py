from numpy import recfromcsv
from operator import itemgetter
from numpy import array
import numpy as np
import csv
import matplotlib.pyplot as plt
from matplotlib import pylab

def column(matrix, i):
    return [row[i] for row in matrix]

array = []

my_data = recfromcsv('RR_CR_CancelTime.csv', usecols=(0,1,2,3,4,5))
numrows = len(my_data)
print(numrows)

for row in range(numrows):
	array.append(my_data[row])

x = column(array,4)
y = column(array,5)
z = column(array,3)

plt.scatter(x, y, c=z, s=100, cmap=plt.cm.cool, edgecolors='None', alpha=0.75)
plt.xlim(0,1)
plt.ylim(0,1)
plt.title('Every Point is a Passenger')
plt.xlabel('P-cancel Rate')
plt.ylabel('Ride Rate')
plt.colorbar().set_label(r'Cancel Time', labelpad=-40, y=0.45)
plt.show()