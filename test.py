import csv
x=[]
y= []
data = list(csv.reader(open('/Users/samir/Documents/exports/average_fare_revenue_schemes.csv')))
numrows = len(data)
print numrows
for row in range(numrows):
    x = data[row][6]
    y = data[row][5]
    print x, ' , ', y
