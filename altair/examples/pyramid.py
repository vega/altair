"""
Pyramid Pie Chart
-----------------
Altair reproduction of http://robslink.com/SAS/democd91/pyramid_pie.htm
"""
# category: case studies
import altair as alt
import pandas as pd

category = ['Sky', 'Shady side of a pyramid', 'Sunny side of a pyramid']
color = ["#416D9D", "#674028", "#DEAC58"]
df = pd.DataFrame({'category': category, 'value': [75, 10, 15]})

alt.Chart(df, width=150, height=150).mark_arc(outerRadius=80).encode(
    alt.Theta('value:Q').scale(range=[2.356, 8.639]),
    alt.Color('category:N')
        .title(None)
        .scale(domain=category, range=color)
        .legend(orient='none', legendX=160, legendY=50),
    order='value:Q'
).configure_view(
    strokeOpacity=0
)
