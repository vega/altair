"""
Multiple Interactions
=====================
This example shows how multiple user inputs can be layered onto a chart. The four inputs have functionality as follows:

* Dropdown: Filters the movies by genre
* Radio Buttons: Highlights certain films by Worldwide Gross
* Mouse Drag and Scroll: Zooms the x and y scales to allow for panning.



"""
# category: interactive charts
import altair as alt
from vega_datasets import data

movies = alt.UrlData(
    data.movies.url,
    format=alt.DataFormat(parse={"Release_Date":"date"})
)
ratings = ['G', 'NC-17', 'PG', 'PG-13', 'R']
genres = ['Action', 'Adventure', 'Black Comedy', 'Comedy',
       'Concert/Performance', 'Documentary', 'Drama', 'Horror', 'Musical',
       'Romantic Comedy', 'Thriller/Suspense', 'Western']

base = alt.Chart(movies, width=200, height=200).mark_point(filled=True).transform_calculate(
    Rounded_IMDB_Rating = "floor(datum.IMDB_Rating)",
    Hundred_Million_Production =  "datum.Production_Budget > 100000000.0 ? 100 : 10",
    Release_Year = "year(datum.Release_Date)"
).transform_filter(
    alt.datum.IMDB_Rating > 0
).transform_filter(
    alt.FieldOneOfPredicate(field='MPAA_Rating', oneOf=ratings)
).encode(
    x=alt.X('Worldwide_Gross:Q', scale=alt.Scale(domain=(100000,10**9), clamp=True)),
    y='IMDB_Rating:Q',
    tooltip="Title:N"
)

# A slider filter
year_slider = alt.binding_range(min=1969, max=2018, step=1, name="Release Year")
slider_selection = alt.selection_point(bind=year_slider, fields=['Release_Year'])

filter_year = base.add_params(
    slider_selection
).transform_filter(
    slider_selection
).properties(title="Slider Filtering")

# A dropdown filter
genre_dropdown = alt.binding_select(options=genres, name="Genre")
genre_select = alt.selection_point(fields=['Major_Genre'], bind=genre_dropdown)

filter_genres = base.add_params(
    genre_select
).transform_filter(
    genre_select
).properties(title="Dropdown Filtering")

#color changing marks
rating_radio = alt.binding_radio(options=ratings, name="Rating")
rating_select = alt.selection_point(fields=['MPAA_Rating'], bind=rating_radio)

rating_color = (
    alt.when(rating_select)
    .then(alt.Color('MPAA_Rating:N', legend=None))
    .otherwise(alt.value("lightgray"))
)

highlight_ratings = base.add_params(
    rating_select
).encode(
    color=rating_color
).properties(title="Radio Button Highlighting")

# Boolean selection for format changes
input_checkbox = alt.binding_checkbox(name="Big Budget Films ")
checkbox_selection = alt.param(bind=input_checkbox)

size_checkbox = (
    alt.when(checkbox_selection)
    .then(alt.Size('Big_Budget_Film:N', scale=alt.Scale(range=[25, 150])))
    .otherwise(alt.value(25))
)

budget_sizing = base.add_params(
    checkbox_selection
).encode(
    size=size_checkbox
).properties(title="Checkbox Formatting")

(filter_year | budget_sizing) & (highlight_ratings | filter_genres)
