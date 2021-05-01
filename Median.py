import csv
with open('DataSet.csv',newline='')as F:
    reader=csv.reader(F)
    fileData=list(reader)
fileData.pop(0)
NewData=[]
for I in range(len(fileData)):
    num=fileData[I][1]
    NewData.append(float(num))
n=len(NewData)
NewData.sort()
if n%2==0:
    median1=float(NewData[n//2])
    median2=float(NewData[n//2-1])
    median=(median1+median2)/2
else:
    median=NewData[n//2]
print('Median:',median)