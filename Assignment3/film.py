import csv
from pyecharts import options as opts
from pyecharts.charts import Page, Parallel

read = csv.reader(open('film/China.csv','r'))
China = []
for row in read:
    China.append(row[1:6])
China.pop(0)
China = [list(map(int,i)) for i in China]

read = csv.reader(open('film/Japan.csv','r'))
Japan = []
for row in read:
    Japan.append(row[1:6])
Japan.pop(0)
Japan = [list(map(int,i)) for i in Japan]

read = csv.reader(open('film/SouthKorea.csv','r'))
SouthKorea = []
for row in read:
    SouthKorea.append(row[1:6])
SouthKorea.pop(0)
SouthKorea = [list(map(int,i)) for i in SouthKorea]

read = csv.reader(open('film/US.csv','r'))
US = []
for row in read:
    US.append(row[1:6])
US.pop(0)
US = [list(map(int,i)) for i in US]

def parallel_base() -> Parallel:
    
    c = (
        Parallel()
        .add_schema(
            [
                {"dim": 0, "name": "售票量/k"},
                {"dim": 1, "name": "总票房"},
                {"dim": 2, "name": "银幕数量"},
                {"dim": 3, "name": "平均票价"},
                {"dim": 4, "name": "新电影上映数量"},
            ]
        )
        .add("US", US)
        .set_global_opts(title_opts=opts.TitleOpts(title="Parallel-基本示例"))
    )
    return c

a = parallel_base()
a.render()