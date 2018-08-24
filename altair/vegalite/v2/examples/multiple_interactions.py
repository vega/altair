"""
Multiple Interations
==================
This example shows how multiple user inputs can be layered onto a chart. The four inputs have functionality as follows: 

* Dropdown: Allows the user to highlight cars from a particular country
* Slider: Filters the display so that only cars from a certain year of manufacture are shown
* Checkbox: toggles whether to size the points by the cars weight or not
* Mouse Drag and Scroll: Zooms the x and y scales to allow for panning. 


"""
# category: interactive charts
import altair as alt
from vega_datasets import data


cars = data.cars.url

input_dropdown = alt.binding_select(options=['Europe','Japan','USA'])
dropdown_selection = alt.selection_single(fields=['Origin'], bind=input_dropdown, name='Country of ')
color = alt.condition(selection,
                    alt.Color('Origin:N', legend=None),
                    alt.value('lightgray'))

scales_selection = alt.selection_interval(bind="scales")

year_slider = alt.binding_range(min=1969, max=1981, step=1)
slider_selection = alt.selection_single(bind=year_slider, fields=['Year'], name="Manufacture_")

input_checkbox = alt.binding_checkbox()
checkbox_selection = alt.selection_single( bind=input_checkbox, name="Highlight Heavy Vehicles")

size = alt.condition(checkbox_selection,
                    alt.SizeValue(40), 
                    alt.Size('Weight_in_lbs:Q', bin=True, legend=None)
                    )

scatter = alt.Chart(cars).mark_point(filled=True
    ).transform_calculate(
    Year="year(datum.Year)").transform_calculate(
    Heavy=alt.expr.inrange("dataum.Weight_in_lbs", 4000,10000)
).encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=color,
    tooltip='Name:N',
    size=size
).add_selection(
    selection
).add_selection(
    scales_selection
).add_selection(
    slider_selection
).add_selection(
    checkbox_selection
).transform_filter(
    slider_selection
)


scatter