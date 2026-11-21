.. _conceptual-guide:

Conceptual Guide
================

The User Guide explains how to build charts with Altair. This guide focuses on why we make particular visualization choices and how those choices affect what readers notice.

Choosing a Visual Encoding
--------------------------

A chart is useful when its visual form makes the answer to a question easy to see. Before choosing a mark or encoding, write down the question you want the chart to answer. Are you comparing groups, following a value over time, studying a relationship, or looking at how values are spread? The same dataset can support different charts because each chart answers a different question.

Start with the type of data. Quantitative values are amounts that can be measured. Nominal values are names or unordered groups. Ordinal values have a meaningful order, and temporal values represent dates or times. Altair uses these types to choose scales and legends; see :ref:`encoding-data-types` for details. Check that the inferred type matches the meaning of the column. A number such as a postal code is a label, not a measurement.

Use channels that make the important comparison easy. Position on a common axis is one of the most accurate ways to compare quantitative values. Length, as in a bar chart, can also support comparison when bars share a clear baseline. Color is useful for grouping, but people are generally less precise at comparing values by color intensity than by position. Keep the number of colors small enough that groups remain distinguishable.

Questions about time usually benefit from placing time in order along an axis. Questions about a relationship between two measurements often suit a scatter plot, where each point represents one observation. If the question is about variation within groups, show the distribution or individual observations instead of only a group average. An average can hide a wide spread or unusual values.

A small example shows how the question changes the encoding. The first chart compares average fuel efficiency by car origin. The second looks at the relationship between horsepower and fuel efficiency for individual cars.

.. altair-plot::

   import altair as alt
   from altair.datasets import data

   cars = data.cars()

   alt.Chart(cars).mark_bar().encode(
       x=alt.X("Origin:N", title="Car origin"),
       y=alt.Y("mean(Miles_per_Gallon):Q", title="Average miles per gallon"),
   )

.. altair-plot::

   alt.Chart(cars).mark_circle(opacity=0.6).encode(
       x=alt.X("Horsepower:Q", title="Horsepower"),
       y=alt.Y("Miles_per_Gallon:Q", title="Miles per gallon"),
       color=alt.Color("Origin:N", title="Car origin"),
       tooltip=["Name:N", "Origin:N", "Horsepower:Q", "Miles_per_Gallon:Q"],
   )

The bar chart summarizes each group, so it cannot show how much cars vary within an origin. The scatter plot preserves each car as a point and makes the relationship between two measurements visible. Neither chart is universally better; the question determines which evidence should be shown.

Color also carries meaning. Use distinct hues for categories, a single-hue sequence for values that move from low to high, and a diverging scheme when values are meaningfully above or below a reference point such as zero. A legend should make the mapping clear. Do not depend on color alone to distinguish groups; labels, position, or shape can provide another cue.

Finally, make comparisons fair. Use consistent scales when comparing panels, label units, and include the context needed to interpret the values. Avoid adding visual detail that does not help answer the question. When a design choice could change the conclusion a reader draws, explain it in the chart or its accompanying text.
