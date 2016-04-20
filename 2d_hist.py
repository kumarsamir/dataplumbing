from numpy import recfromcsv
from operator import itemgetter
from numpy import array
import numpy as np
import csv
import matplotlib.pyplot as plt
from matplotlib import pylab
from matplotlib.colors import LogNorm

def column(matrix, i):
    return [row[i] for row in matrix]

array = []

my_data = recfromcsv('RR_CR_CancelTime.csv', usecols=(0,1,2,3,4,5))
numrows = len(my_data)
print(numrows)

for row in range(numrows):
	array.append(my_data[row])

x = column(array,3)
y = column(array,4)
z = column(array,5)

H, xedges, yedges = np.histogram2d(z, y, normed = True, range=[[0, 1], [0, 1]], bins=10)
extent = [yedges[0], yedges[-1], xedges[-1], xedges[0]]
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
im = ax.imshow(H, extent=extent,cmap=plt.get_cmap('hot'),interpolation = 'nearest')
fig.colorbar(im,ax=ax).set_label("Percentages")
plt.ylabel('Ride Rate')
plt.xlabel('Passenger Cancel Rate')
plt.title('P Cancel Rate vs. Ride Rate - GC SG',fontsize=22)
plt.gca().invert_yaxis()
plt.show()