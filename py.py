import csv
f=open('a30.csv','r')
d=csv.reader(f,delimiter="\t")
for i in d:
    print(i)
