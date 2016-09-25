import csv
import numpy as np
with open('/Users/samir/Documents/exports/First ETA - SG.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    rowcounter=0;
    paxArray=[]
    for row in spamreader:
        for element in row:
            paxID = element.split(',')[1]
            paxArray.append(paxID);
        rowcounter+= 1
        print ', '.join(row)
        if(rowcounter>100):
            break
    x=np.array(paxArray)
    cumulativeSum=np.cumsum(x.astype(paxArray.float))
    print 'LTV:' + str(paxArray)
