.. currentmodule:: altair

.. _user-guide-pivot-transform:

Pivot
~~~~~
The pivot transform is, in short, a way to convert long-form data to wide-form
data directly without any preprocessing (see :ref:`data-long-vs-wide` for more
information). Pivot transforms are useful for creating matrix or cross-tabulation
data, acting as an inverse to the :ref:`user-guide-fold-transform`.

Here is an example, using Olympic medals data:

.. altair-plot::

   import altair as alt
   import pandas as pd

   df = pd.DataFrame.from_records([
       {"country": "Norway", "type": "gold", "count": 14},
       {"country": "Norway", "type": "silver", "count": 14},
       {"country": "Norway", "type": "bronze", "count": 11},
       {"country": "Germany", "type": "gold", "count": 14},
       {"country": "Germany", "type": "silver", "count": 10},
       {"country": "Germany", "type": "bronze", "count": 7},
       {"country": "Canada", "type": "gold", "count": 11},
       {"country": "Canada", "type": "silver", "count": 8},
       {"country": "Canada", "type": "bronze", "count": 10}
   ])

   alt.Chart(df).transform_pivot(
       'type',
       groupby=['country'],
       value='count'
   ).mark_bar().encode(
       x='gold:Q',
       y='country:N',
   )

The pivot transform, when combined with other elements of the Altair grammar, enables some
very interesting chart types. For example, here we use pivot to create a single tooltip for
values on multiple lines:

.. altair-plot::

   import altair as alt
   from vega_datasets import data

   source = data.stocks()
   base = alt.Chart(source).encode(x='date:T')
   columns = sorted(source.symbol.unique())
   selection = alt.selection_point(
       fields=['date'], nearest=True, on='mouseover', empty='none', clear='mouseout'
   )

   lines = base.mark_line().encode(y='price:Q', color='symbol:N')
   points = lines.mark_point().transform_filter(selection)

   rule = base.transform_pivot(
       'symbol', value='price', groupby=['date']
   ).mark_rule().encode(
       opacity=alt.condition(selection, alt.value(0.3), alt.value(0)),
       tooltip=[alt.Tooltip(c, type='quantitative') for c in columns]
   ).add_params(selection)

   lines + points + rule


Transform Options
^^^^^^^^^^^^^^^^^
The :meth:`~Chart.transform_pivot` method is built on the :class:`~PivotTransform`
class, which has the following options:

.. altair-object-table:: altair.PivotTransform
