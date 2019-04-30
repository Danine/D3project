# Assignment 3

姓名：代荣森&nbsp;&nbsp;&nbsp;&nbsp;学号：201618130133

## 图表链接
http://tysondai.me/

## 项目链接
https://github.com/Danine/VisualizationProject/tree/master/Assignment3 

## 设计原理
&emsp;&emsp;由于选择的数据集有关于10年来中日韩美四国的电影相关数据的发展，所以选择了最适合表示发展趋势的**Line Charts**作为基础，在其中增加交互技巧，从而完成本次任务。

## 如何选择交互技巧
&emsp;&emsp;由于部分国家电影发展情况十分接近，在数据集中会出现两条折线十分贴近的情况，于是增加了**鼠标滚轮放大区域**的交互，以便于查看这类国家间的具体数据。考虑到数据的可延续性，增加了**坐标轴拖动**交互，可以在未来数据量很大时能通过拖动来查看历年的信息。另外，便于同一年份各个国家间各项数据的对比，选择了**Multi-Line Tooltip**作为主要交互技巧。

## 开发过程

1.  寻找合适的数据集
2.  选择灵活好用的开发工具
3.  处理数据，转换格式
4.  将数据以折线图的方式添加到图表中
5.  添加合适的交互技巧


### 花费时间：
&emsp;&emsp;2周，约20小时  

### 花费时间最多的方面
&emsp;&emsp;大多时间花费在了选择一个合适的可视化工具，从*D3.js*到*pyecharts*，又换成了*Altair*，除此之外，寻找一个感兴趣并且能够可视化的数据集和学习相应可视化工具的语法也花费了较长的时间。


---
## 附录：源代码
```python
import csv
import altair as alt
import pandas as pd

def getData(path):
    read = csv.reader(open(path,'r'))
    Data = []
    for row in read:
        Data.append(row)
    Data.pop(0)
    Data = [list(map(int,i)) for i in Data]
    return Data

China = getData('film/China.csv')
Japan = getData('film/Japan.csv')
SouthKorea = getData('film/SouthKorea.csv')
US = getData('film/US.csv')

country = []; year = []; gross = []; ticketSold = []
avgPrice = []; screen = []
def prepare(data, countryName):
    for i in data:
        country.append(countryName)
        year.append(i[0])
        ticketSold.append(i[1])
        gross.append(i[2]/10**8)
        screen.append(i[3])
        avgPrice.append(i[4])

prepare(China, 'China')
prepare(Japan, 'Japan')
prepare(SouthKorea, 'SouthKorea')
prepare(US, 'US')


data = pd.DataFrame({
    'country' : country,
    'year' : year,
    'ticketSold' : ticketSold,
    'total gross(Billion CNY)':gross,
    'screen' : screen,
    'avgPrice' : avgPrice
})
print(data)

line = alt.Chart(data).mark_line().encode(
    alt.X(alt.repeat("column"), type='quantitative'),
    alt.Y(alt.repeat("row"), type='quantitative'),
    color = 'country',
)

nearest = alt.selection(type='single', nearest=True, on='mouseover',
                        fields=['year'], empty='none')

selectors = alt.Chart(data).mark_point().encode(
    x='year',
    opacity=alt.value(0),
).add_selection(
    nearest
)

points = line.mark_point().encode(
    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
)

text = line.mark_text(align='left', dx=5, dy=-5).encode(
    text=alt.condition(nearest, alt.Y(alt.repeat("row"), type='quantitative'), alt.value(' '))
)

rules = alt.Chart(data).mark_rule(color='gray').encode(
    x='year',
).transform_filter(
    nearest
)

chart = alt.layer(
    line, selectors, points, rules, text
).properties(
    width=600, height=300
).repeat(
    row=['ticketSold', 'total gross(Billion CNY)', 'screen', 'avgPrice'],
    column=['year']
).interactive()

chart.savechart('plot.html')
```