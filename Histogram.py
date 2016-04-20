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

array = []

my_data = recfromcsv('PassengerCancelTimeGCJKT.csv', usecols=(0,1,2,3))
numrows = len(my_data)
print("number of rows :- " + str(numrows))
diff = []
for row in range(numrows):
    cancellation_time = time.mktime(datetime.datetime.strptime(my_data[row][3], "%Y-%m-%d %H:%M:%S.%f").timetuple())
    booking_time = time.mktime(datetime.datetime.strptime(my_data[row][2], "%Y-%m-%d %H:%M:%S.%f").timetuple())
    delta= round(((cancellation_time-booking_time)/60),2)
    diff.append(delta)
    array.append(my_data[row])

#y = column(array,0)
#z = column(array,0)
lessThanOneMinute =0;
oneToTwoMinutes =0;
twoToThreeMinutes =0;
threeToFourMinutes =0;
fourToFiveMinutes =0;
fiveToSixMinutes =0;
sixToSevenMinutes =0;
sevenToEightMinutes =0;

for element in diff:
    if (float(element) <1):
        lessThanOneMinute+=1
    elif (float(element)>1 and float(element)<=2):
        oneToTwoMinutes+=1
    elif (float(element) > 2 and float(element) <= 3):
        twoToThreeMinutes +=1
    elif (float(element) > 3 and float(element) <= 4):
        threeToFourMinutes +=1
    elif (float(element) > 4 and float(element) <= 5):
        fourToFiveMinutes +=1
    else:
        fiveToSixMinutes+=1

print(lessThanOneMinute, oneToTwoMinutes,twoToThreeMinutes,threeToFourMinutes, fourToFiveMinutes,  fiveToSixMinutes )
ratio=100*(lessThanOneMinute/numrows)
print ratio
plt.hist(diff, bins=range(10))
plt.ylabel('No of passengers')
plt.xlabel('Time to Cancellation')
plt.title('Pax Cancel Time - GC JKT',fontsize=24)
plt.axis([0, 10, 0, 25000])
plt.bar(10,10)
plt.show()


