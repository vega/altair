from altair import *

data = load_dataset('cars')

v = Layer().encode(
    x=X('Horsepower:Q'),
    y=Y('Miles_per_Gallon:Q')
).mark_point()

expected_output = {'encoding': {'x': {'field': 'Horsepower', 'type': 'quantitative'},
                                'y': {'field': 'Miles_per_Gallon', 'type': 'quantitative'}},
                   'mark': 'point'}
