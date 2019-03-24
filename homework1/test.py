import csv
read = csv.reader(open('D:\GitHub\VisualizationProject\homework1\census2000.csv','r'))
census = []
for line in read:
    census.append(line)
for i in census:
    print(i[2])