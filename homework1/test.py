import csv
from pyecharts import Bar

read = csv.reader(open('D:\GitHub\VisualizationProject\homework1\census2000.csv','r'))
census = []
for line in read:
    census.append(line)


bar = Bar("测试")
bar.add("男")