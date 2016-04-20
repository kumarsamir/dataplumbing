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

my_data = recfromcsv('PassengerCohorts.csv', usecols=(0,1,2,3,4,5,6,7,8,9,10))
numrows = len(my_data)
print(numrows)

for row in range(numrows):
	array.append(my_data[row])

x = column(array,4)
y = column(array,10)
z = column(array,8)
#s = [50000**z[n] for n in range(len(z))]

plt.scatter(x, y, c=z, s=200, cmap=plt.cm.cool, edgecolors='None', alpha=0.75)
plt.xlim(0,3)
plt.ylim(0,9)
plt.title('Every Point is a Passenger')
plt.xlabel('Completed Rides/ Day')
plt.ylabel('Non-Unique Bookings/ Day')
plt.colorbar().set_label(r'Cancellation Rate', labelpad=-40, y=0.45)
plt.show()

# bins = np.linspace(-10, 10, 100)

# plt.hist(x, bins, alpha=0.5, label='x')
# plt.hist(y, bins, alpha=0.5, label='y')
# plt.legend(loc='upper right')
# plt.show()

# nx, ny = 5, 9
# H, _, _ = np.histogram2d(x, y, bins=(nx,ny), normed=True)
# pylab.imshow(H, interpolation='nearest')
# pylab.colorbar()
# pylab.show()

# H, xedges, yedges = np.histogram2d(x, y, bins=(9, 9), range=[[0,9],[0,9]], normed=True)
# extent = [yedges[0], yedges[-1], xedges[-1], xedges[0]]
# plt.imshow(H, extent=extent, interpolation='nearest', vmin=0.0, vmax=1.0)
# plt.set_cmap('hot')
# plt.colorbar()
# plt.title('XY Plot',fontsize=22)
# plt.show()