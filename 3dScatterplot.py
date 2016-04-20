from numpy import recfromcsv
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


my_data = recfromcsv('RR_CR_CancelTime_Small.csv', usecols=(3,4,5))
numofRows = len(my_data)
print("number of rows :- " + str(numofRows))
diff = []

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for row in range(numofRows):
    xs = my_data[row][0]
    ys = my_data[row][1]
    zs = my_data[row][2]
    print(round(xs,2),round(ys,2),round(zs,2))
    ax.scatter(xs, ys, zs, c='r',marker='o')

ax.set_xlabel('Time to cancellation')
ax.set_ylabel('Cancellation Rate')
ax.set_zlabel('Ride Rate')

plt.show()
