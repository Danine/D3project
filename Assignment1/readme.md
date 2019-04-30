# Assignment 1  

姓名：代荣森&nbsp;&nbsp;&nbsp;&nbsp;学号：201618130133

## 图表
![图1](https://github.com/Danine/VisualizationProject/blob/master/Assignment1/census.png)
---
## 设计原理
利用 **条形图** 和 **折线图**，在同一张表上体现出了每个年龄段的分布情况及变化情况，突出展现了以下几个问题：

---
## 问题1：每个年龄段的人口分布
大概来看，20世纪每个年龄段人口逐渐递减，21世纪40岁以后的人口递减更快

---
## 问题2：每个年龄段的男女比例
20世纪每个年龄段男女比例基本均衡，21世纪30岁以前男性多于女性，30岁之后女性多于男性，且比例一直在增大

---
## 问题3：两个世纪人口老龄化情况
20世纪没有出现人口老龄化情况，而21世纪人口老龄化严重  

---
## 附录：源代码
```python
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
```