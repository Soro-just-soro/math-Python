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
total=0
for x in NewData:
    total=total+x
mean=total/n
print('Average:',mean)