import csv
import altair as alt
import pandas as pd
# from vega_datasets import data
# source = data.stocks()
# print(source)

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

country = []; year = []; gross = []; ticketSold = []; avgPrice = []
def prepare(data, countryName):
    for i in data:
        country.append(countryName)
        year.append(i[0])
        ticketSold.append(i[1])
        gross.append(i[2]/10**8)
        avgPrice.append(i[4])

prepare(China, 'China')
prepare(Japan, 'Japan')
prepare(SouthKorea, 'SouthKorea')
prepare(US, 'US')


data = pd.DataFrame({
    'country' : country,
    'year' : year,
    'total gross(Billion CNY)':gross
})
print(data)

line = alt.Chart(data).mark_line(interpolate='basis').encode(
    x = 'year',
    y = 'total gross(Billion CNY)',
    color = 'country'
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
    text=alt.condition(nearest, 'total gross(Billion CNY)', alt.value(' '))
)

rules = alt.Chart(data).mark_rule(color='gray').encode(
    x='year',
).transform_filter(
    nearest
)

chart = alt.layer(
    line, selectors, points, rules, text
).properties(
    width=800, height=400
)

chart.serve()