import csv
import math
with open('data.csv',newline='')as F:
    reader=csv.reader(F)
    fileData=list(reader)
data=fileData[0]
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total=total+x
        mean=total/n
    return mean
squaredlist=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squaredlist.append(a)
sum=0
for x in squaredlist:
    sum=sum+x
result=sum/(len(data)-1)
standardDeviation=math.sqrt(result)
print('Standard Deviation is:',standardDeviation)