"""
Modified Box Plot with Outliers
-------------------------------
This example shows how to make a modified box plot using US Population data from 2000. 
By default, an outlier is defined as any point that is more than 1.5 IQRs outside the box. 
Outliers are mapped to points and the whiskers extend to the largest/smallest non-outliers.  
Users can adjust the outlier threshold using, for example, `mark_boxplot(extent=3.0)`
"""
# category: other charts
import altair as alt
from vega_datasets import data

source = data.population.url

alt.Chart(source).mark_boxplot().encode(
    x='age:O',
    y='people:Q'
)
