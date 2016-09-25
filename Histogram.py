from numpy import recfromcsv
import time
import datetime
from operator import itemgetter
from numpy import array
import numpy as np
import csv
import matplotlib.pyplot as plt
from matplotlib import pylab
from matplotlib.colors import LogNorm

def column(matrix, i):
    return [row[i] for row in matrix]



my_data = recfromcsv('/Users/samir/PycharmProjects/Scatterplot/SINGAPORE First eta band vs CR.csv', usecols=(0,1,2,3))
numrows = len(my_data)
print("number of rows :- " + str(numrows))
time_to_cancel = []
first_eta =[]
count=0
for row in range(numrows):
    time_to_cancel.append(my_data[row][3]/60)
    first_eta.append(my_data[row][2]/60)

bins = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

plt.ylabel('# of bookings cancelled')
plt.xlabel('FIRST ETA in mins')
plt.title('First ETA vs # of cancelled bookings',fontsize=24)
plt.hist(time_to_cancel,bins,histtype='bar',facecolor='g', alpha=0.75)
plt.axis([0, 20, 0, 50000])
plt.legend()
plt.grid(True)
plt.show()

