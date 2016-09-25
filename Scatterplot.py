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

my_data = recfromcsv('ETA vs cancel GC-Manila.csv', usecols=(0,1,2,3))
numrows = len(my_data)
print(numrows)

for row in range(numrows):
	array.append(my_data[row])

x = column(array,3)
y = column(array,2)
colors = np.random.rand(numrows)

plt.scatter(x, y, c=colors, s=20, edgecolors='None', alpha=0.75)
plt.xlim(0,2000)
plt.ylim(0,2000)
plt.title('GC Manila:- Every point is a booking' )
plt.xlabel('Time to pax cancel (in seconds) ')
plt.ylabel('First ETA (in seconds)')
plt.show()
