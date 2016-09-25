import csv
with open('List of completed bookings in the last 2 months.csv', 'rb') as csvfile:
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
    # for i in paxArray:
    #     abc= i +','
    print 'Pax array:' + str(paxArray)

def doesPaxExist(paxID):

