"""
Ranged Dot Plot
-----------------
This example shows a ranged dot plot that uses 'layer' to convey changing life expectancy for the five most populous countries (between 1955 and 2000).
"""

import altair as alt
from vega_datasets import data

source = data.countries()


line = alt.Chart(source).mark_line(color='#db646f').encode(
    x = 'life_expect',
    y = 'country',
    detail = 'country'
    ).interactive()
line.transform = [{'filter': {"field": 'country', "oneOf": ["China", "India", "United States", "Indonesia", "Brazil"]}},
                  {'filter': {"field": 'year', "oneOf": [1955, 2000]}}]

point = alt.Chart(source).mark_point(size = 100, opacity = 1, filled = True).encode(
    x = 'life_expect',
    y = 'country',
    color=alt.Color('year:O',
        scale=alt.Scale(
            domain=['1955', '2000'],
            range=['#e6959c', '#911a24']
        )))

point.transform = [{'filter': {"field": 'country', "oneOf": ["China", "India", "United States", "Indonesia", "Brazil"]}},
                  {'filter': {"field": 'year', "oneOf": [1955, 2000]}}]

chart = line + point
#chart.transform = [{'filter': {"field": 'country', "oneOf": ["China", "India", "United States", "Indonesia", "Brazil"]}},
#                  {'filter': {"field": 'year', "oneOf": [1955, 2000]}}]
