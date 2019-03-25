import csv
from pyecharts import Bar

read = csv.reader(open('D:\GitHub\VisualizationProject\homework1\census2000.csv','r'))
census = []
for line in read:
    census.append(line)
census.pop(0)

attr = []
v119 = []; v219 = []; v120 = []; v220 = []
for i in census:
    if i[0] == '1' and i[1] == '1900':
        attr.append(int(i[2]))
        v119.append(int(i[3]))
    elif i[0] == '1' and i[1] == '2000':
        v120.append(int(i[3]))
    elif i[0] == '2' and i[1] == '1900':
        v219.append(int(i[3]))
    elif i[0] == '2' and i[1] == '2000':
        v220.append(int(i[3]))

bar = Bar(title = "1900-2000", subtitle="男女人数比", width = 1400, height = 700)
bar.add("1900男", attr, v119)
bar.add("1900女", attr, v219)
bar.add("2000男", attr, v120)
bar.add("2000女", attr, v220)
bar.render()