import csv
from pyecharts import Bar3D

read = csv.reader(open('D:\GitHub\VisualizationProject\homework1\census2000.csv','r'))
census = [line for line in read]
census.pop(0)

attr = []; v119 = []; v219 = []; v120 = []; v220 = []
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

data = []
v = [v119,v219,v120,v220]
for i in range(4):
    for j in range(len(attr)):
        temp = [j,i,v[i][j]]
        data.append(temp.copy())

bar3d = Bar3D(title = "1900-2000", subtitle="男女人数比", width = 1400, height = 700)
x_axis = attr
y_axis = ["1900男","1900女","2000男", "2000女"]
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
bar3d.add("", x_axis, y_axis, data,
    is_visualmap=True,
    visual_range=[0, 11700000],
    visual_range_color=range_color,
    grid3d_width=200,
    grid3d_depth=40,
    grid3d_shading="lambert",
    )
bar3d.render()