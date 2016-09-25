from numpy.random import normal, uniform
from numpy import recfromcsv
import matplotlib.pyplot as plt


def column(matrix, i):
    return [row[i] for row in matrix]


print("Started to run")
my_data = recfromcsv('/Users/samir/PycharmProjects/Scatterplot/SINGAPORE First eta band vs CR.csv', usecols=(0,1,2,3))
numrows = len(my_data)
print("number of rows :- " + str(numrows))
gaussian_numbers = normal(size=1000)
uniform_numbers = uniform(low=-3, high=3, size=1000)
plt.hist(gaussian_numbers, bins=20, histtype='stepfilled', normed=True, color='b', label='Gaussian')
plt.hist(uniform_numbers, bins=20, histtype='stepfilled', normed=True, color='r', alpha=0.5, label='Uniform')
plt.title("Gaussian/Uniform Histogram")
plt.xlabel("Value")
plt.ylabel("Probability")
plt.legend()
plt.show()