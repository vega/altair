.. currentmodule:: altair

.. _user-guide-color:

Color Scales
============

Effective visualization of scientific data requires careful attention
to color selection. Choosing the right colors can be a complex task,
involving considerations such as color perception, accessibility,
and aesthetics. Fortunately, there are a number of resources available
to help simplify this process, including pre-designed color schemes
and tools for exploring and modifying color scales. In this guide,
we'll explore some of the basics of color selection for scientific 
data visualization, including different types of color scales and
examples of their use.

I. The Basics of Color Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Color selection is an essential aspect of creating clear and informative
visualizations of scientific data. To make the most effective choices,
it's important to understand the basics of color perception and theory.

A. Color Perception and Theory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. The importance of perceptually uniform color scales
------------------------------------------------------

Using colors that are perceptually uniform can help ensure that viewers
can accurately perceive the relative differences between data points. By
maintaining consistent differences in color perception across a scale, you
can create visualizations that are not only informative but also easy to
understand.

.. code-block:: none

    A comparison of perceptually uniform color scales and non-uniform
    scales, showing how the choice of color space can affect the perceived
    brightness and contrast of colors.

2. Different types of color spaces
----------------------------------

Different color spaces, such as RGB or HSL, offer different advantages and
can affect the perceived brightness and contrast of colors. By 
understanding the nuances of color spaces, you can create visualizations
that are not only informative but also visually appealing.

B. Accessibility and Aesthetics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Considerations for color-blind viewers
-----------------------------------------
   
Around 8% of men and 0.5% of women have some form of color vision deficiency.
To make sure your visualizations are accessible to all viewers, it's
important to choose colors that are distinguishable even for those with 
color vision deficiencies. By using colors that have a high degree of
contrast, you can create visualizations that are not only informative but
also inclusive.

.. code-block:: none

    A comparison of color schemes that are accessible to color-blind
    viewers versus those that are not.

2. Guidelines for creating visually appealing presentations
-----------------------------------------------------------

While accuracy is the primary goal of visualizations, aesthetics also play
an important role in engaging viewers and making data more memorable.
By using a limited color palette, choosing harmonious colors, and balancing
colors to create a sense of visual hierarchy, you can create visualizations
that are not only informative but also visually stunning.

.. code-block:: none
    
    A visualization that uses color to create a sense of visual hierarchy,
    such as a heatmap or a scatterplot.


II. Types of Color Scales
~~~~~~~~~~~~~~~~~~~~~~~~~

This sections presents the three primary color scales used in data
visualization: sequential, diverging, and categorical. The section
includes examples of data that can be visualized using each scale and
popular color schemes used in practice.

A. Sequential Scales
^^^^^^^^^^^^^^^^^^^^

1. Examples of sequential data
------------------------------

Sequential scales are best suited for data that has an inherent ordering,
such as data that varies from low to high, or over time. Examples of
sequential data include temperature or population density, where the
range of values is continuous and unbroken.

1. Example color schemes for sequential data
--------------------------------------------

.. code-block:: none
    
    Sequential color schemes.

B. Diverging Scales
^^^^^^^^^^^^^^^^^^^

1. Examples of diverging data
-----------------------------

Diverging scales are best suited for data that varies above and below a
center point, such as positive and negative deviations from a mean.
Examples of diverging data include measures of deviation, such as
temperature anomalies or changes in sea level.

1. Example color schemes for diverging data
-------------------------------------------

.. code-block:: none
    
    Diverging color schemes.


C. Categorical Scales
^^^^^^^^^^^^^^^^^^^^^

1. Examples of categorical data
-------------------------------

Categorical scales are best suited for data that is unordered, such as
different species or categories. Examples of categorical data include
the types of flowers in a garden, or different political affiliations.

1. Example color schemes for categorical data
---------------------------------------------

.. code-block:: none
    
    Categorical color schemes.

III. Using Tools for Color Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A. Pre-Designed Color Palettes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Example color palettes from the other packages
-------------------------------------------------

This subsection focuses on pre-designed color palettes that can be
used in data visualization from other sources.

B. Modifying Color Scales
^^^^^^^^^^^^^^^^^^^^^^^^^

1. Tools for adjusting brightness, saturation, and hue
------------------------------------------------------

This subsection provides an overview of the different ways in which
brightness, saturation, and hue can be modified to create custom color
scales. It explains how changing these attributes can help to emphasize
or de-emphasize certain aspects of the data being visualized.

2. Customizing color scales to match specific data requirements
---------------------------------------------------------------

This subsection explores the idea of creating custom color scales that
are tailored to the specific needs of the data being visualized. It
discusses how to use the tools introduced in III.B.1 to create color
scales that are better suited to representing the nuances of the data,
and provides examples of how this can be achieved in practice.

Conclusion
~~~~~~~~~~

By utilizing the tools and resources available for color selection,
data visualizers can create effective and visually appealing
presentations that accurately convey scientific data. Whether using
pre-designed color schemes or customizing color scales, it is
essential to consider factors such as accessibility, aesthetics,
and perceptual relationships in order to create the most effective
visualizations possible.