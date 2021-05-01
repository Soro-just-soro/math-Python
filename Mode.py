from collections import Counter
import csv
with open('DataSet.csv',newline='')as F:
    reader=csv.reader(F)
    fileData=list(reader)
fileData.pop(0)
NewData=[]
for I in range(len(fileData)):
    num=fileData[I][1]
    NewData.append(float(num))
data=Counter(NewData)
modeForrange={
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height,occurence in data.items():
    if 50<float(height)<60:
        modeForrange["50-60"]+=occurence
    elif 60<float(height)<70:
        modeForrange["60-70"]+=occurence
    elif 70<float(height)<80:
        modeForrange["70-80"]+=occurence
modeRange,modeOccurence=0,0