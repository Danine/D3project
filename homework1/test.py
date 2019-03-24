import csv
from pyecharts import Bar

read = csv.reader(open('D:\GitHub\VisualizationProject\homework1\census2000.csv','r'))
census = []
for line in read:
    census.append(line)
census.pop(0)

attr = []
v1 = []; v2 = []
for i in census:
    if i[0] == '1' and i[1] == '1900':
        attr.append(int(i[2]))
        v1.append(int(i[3]))
    elif i[0] == '2' and i[1] == '1900':
        v2.append(int(i[3]))

bar = Bar("1900")
bar.add("男", attr, v1, mark_point = ["average"])
bar.add("女", attr, v2, mark_line = ["min", "max"])
bar.render()