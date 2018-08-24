"""
Multiple Interations
==================
This example shows how multiple user inputs can be layered onto a chart. The four inputs have functionality as follows: 

* Dropdown: Filters the movies by genre
* Radio Buttons: Highlights certain films by Worldwide Gross
* Mouse Drag and Scroll: Zooms the x and y scales to allow for panning. 



"""
# category: interactive charts

import altair as alt
from vega_datasets import data


movies = data.movies.url

ratings = ['G', 'NC-17', 'PG', 'PG-13', 'R']
genres = ['Action', 'Adventure', 'Black Comedy', 'Comedy',
       'Concert/Performance', 'Documentary', 'Drama', 'Horror', 'Musical',
       'Romantic Comedy', 'Thriller/Suspense', 'Western']



rating_radio = alt.binding_radio(options=ratings)


rating_select = alt.selection_single(fields=['MPAA_Rating'], bind=rating_radio)
rating_color_condition = alt.condition(rating_select,
                      alt.Color('MPAA_Rating:N', legend=None),
                      alt.value('lightgray'))

genre_dropdown = alt.binding_select(options=genres)
genre_select = alt.selection_single(fields=['Major_Genre'], bind=genre_dropdown)


alt.Chart(movies).mark_point().transform_calculate(
    Rounded_IMDB_Rating = "floor(datum.IMDB_Rating)"
).transform_filter(
    alt.datum.IMDB_Rating > 0
).transform_filter(
    alt.FieldOneOfPredicate(field='MPAA_Rating', oneOf=ratings)).encode(
x=alt.X('Worldwide_Gross:Q'),
y='IMDB_Rating:Q',
color=rating_color_condition

).add_selection(
    rating_select
).add_selection(
    genre_select
).transform_filter(
    genre_select
)

