import csv
from pyecharts import Bar, Line, Overlap

read = csv.reader(open('D:\GitHub\VisualizationProject\Assignment1\census2000.csv','r'))
census = []
for row in read:
    census.append(row)
census.pop(0)

attr = []
v119 = []; v219 = []; v120 = []; v220 = []
for i in census:
    if i[0] == '1' and i[1] == '1900':
        attr.append(i[2])
        v119.append(int(i[3]))
    elif i[0] == '1' and i[1] == '2000':
        v120.append(int(i[3]))
    elif i[0] == '2' and i[1] == '1900':
        v219.append(int(i[3]))
    elif i[0] == '2' and i[1] == '2000':
        v220.append(int(i[3]))

a19 = []; a20 = []
for i in range(len(v119)):
    temp = (v119[i] + v219[i])/2
    a19.append(temp)
for i in range(len(v120)):
    temp = (v120[i] + v220[i])/2
    a20.append(temp)

bar = Bar(title = "1900-2000", subtitle="男女人数比")
bar.add("1900男", attr, v119)
bar.add("1900女", attr, v219)
bar.add("2000男", attr, v120)
bar.add("2000女", attr, v220,
         xaxis_name = "年龄",
         yaxis_name = "人口",
         yaxis_name_gap = 70,)

line1 = Line()
line1.add("1900", attr, a19)
line1.add("2000", attr, a20)

overlop = Overlap(width = 1400, height = 700)
overlop.add(bar)
overlop.add(line1)
overlop.render()
