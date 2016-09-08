Altair: Declarative Visualization in Python
===========================================

Contents:

.. toctree::
   :maxdepth: 2

   API


A Couple Examples
-----------------

Here's an example of a plot in a webpage:

.. altair-plot::

    from altair import Chart, load_dataset
    cars = load_dataset('cars')

    Chart(cars).mark_point().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin'
    )

Here's a slightly more sophisticated plot:

.. altair-plot::

    from altair import Chart, Color, Formula, Scale
    from altair import load_dataset
    population = load_dataset('population')

    Chart(population).mark_bar().encode(
        x='age:O',
        y='sum(people):Q',
        color=Color('gender:N', scale=Scale(range=["#FF9800", "#03A9F4"]))
    ).transform_data(
        filter='datum.year==2000',
        calculate=[Formula(field='gender',
                           expr='datum.sex == 2 ? "Female" : "Male"')]
    )


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
