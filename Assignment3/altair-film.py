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