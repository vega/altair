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

.. altair-plot::
    :remove-code:
    :output: none

    import altair as alt
    import pandas as pd

    def chart_settings(scheme_name, dict_schemes, continuous):
        # check if the input is a defined or custom scheme
        custom_scheme = True if type(dict_schemes[scheme_name]) is list else False

        # define a data sequence of 300 for continuous color schemes
        if continuous:
            no_colors = 300
            data = alt.sequence(0, no_colors, as_="i")

        # define a data sequence using dict for defined schemes
        elif type(dict_schemes[scheme_name]) is int:
            no_colors = dict_schemes[scheme_name]
            data = alt.sequence(0, no_colors, as_="i")

        # define a dataframe for custom schemes (possible with Altair only?)
        else:
            no_colors = len(dict_schemes[scheme_name])
            colors_in_scheme = dict_schemes[scheme_name]
            data = pd.DataFrame({"i": range(no_colors), "hex": colors_in_scheme})

        # dynamic width
        w = 1.5 if continuous else 50 if no_colors <= 5 else 30 if no_colors <= 12 else 15

        # cornerRadius dependent on height-width ratio
        cr_l = 0 if continuous else int(w / 2.4)
        cr_s = 0 if continuous else 5

        return {
            "data": data,
            "width": w,
            "cornerRadius_large": cr_l,
            "cornerRadius_small": cr_s,
            "no_colors": no_colors,
            "custom": custom_scheme
        }

    def chart_color_scale(scheme_name, dict_schemes, continuous, custom, no):
        color_type = "quantitative" if custom and continuous else "ordinal"    
        scale_scheme = alt.Scale(range=dict_schemes[scheme_name]) if custom else alt.Scale(scheme=scheme_name)

        color_scale = (
            alt.Chart(alt.sequence(0, no, as_="i"))
            .mark_rect(height=alt.expr("0"), width=alt.expr("0"))
            .encode(alt.Color("i", type=color_type).scale(scale_scheme).legend(None))
        )    

        return color_scale

    def chart_normal_vision(data, h, w, expr_hex, my_y_axis, cr_l):
        normal_vision = (
            alt.Chart(data, height=h, width=alt.Step(w))
            .transform_calculate(
                hex=expr_hex,
                rgb="rgb(datum.hex)",
                lum="luminance(datum.hex)",
            )
            .mark_rect(cornerRadius=cr_l, discreteBandSize=w)
            .encode(
                x=alt.X("i:O").axis(None),
                y=alt.Y("normal vision:O").axis(my_y_axis),
                fill=alt.Fill("hex:O").scale(None).legend(None),
                stroke=alt.Stroke("hex:O").scale(None).legend(None),
                tooltip=[
                    alt.Tooltip("hex:O"),
                    alt.Tooltip("rgb:O"),
                    alt.Tooltip("lum:O", format=".2"),
                ],
            )
        )
        return normal_vision

    def chart_green_blindness(data, h, w, expr_hex, my_y_axis, cr_s):
        green_blindness = (
            alt.Chart(data, height=h, width=alt.Step(w))
            .transform_calculate(
                hex=expr_hex,
                rgb="rgb(datum.hex)",
                gb_r="pow((4211+0.667*pow(datum.rgb['g'], 2.2)+0.2802*pow(datum.rgb['r'], 2.2)),1/2.2)",
                gb_g="pow((4211+0.667*pow(datum.rgb['g'], 2.2)+0.2802*pow(datum.rgb['r'], 2.2)),1/2.2)",
                gb_b="pow((4211+0.95724*pow(datum.rgb['b'], 2.2)+0.02138*pow(datum.rgb['b'], 2.2)-0.02138*pow(datum.rgb['r'], 2.2)),1/2.2)",
                greenblind_rgb="rgb(datum.gb_r,datum.gb_g,datum.gb_b)",
            )
            .mark_rect(cornerRadius=cr_s)
            .encode(
                x=alt.X("i:O").axis(None),
                y=alt.Y("green-blindness:N").axis(my_y_axis),
                fill=alt.Fill("greenblind_rgb:N").scale(None).legend(None),
                stroke=alt.Stroke("greenblind_rgb:N").scale(None).legend(None),            
            )
        )    
        return green_blindness

    def chart_red_blindness(data, h, w, expr_hex, my_y_axis, cr_s):
        red_blindness = (
            alt.Chart(data, height=h, width=alt.Step(w))
            .transform_calculate(
                hex=expr_hex,
                rgb="rgb(datum.hex)",
                rb_r="pow((782.7+0.8806*pow(datum.rgb['g'], 2.2)+0.1115*pow(datum.rgb['r'], 2.2)),1/2.2)",
                rb_g="pow((782.7+0.8806*pow(datum.rgb['g'], 2.2)+0.1115*pow(datum.rgb['r'], 2.2)),1/2.2)",
                rb_b="pow((782.7+0.992052*pow(datum.rgb['b'], 2.2)-0.03974*pow(datum.rgb['b'], 2.2)+0.003974*pow(datum.rgb['r'], 2.2)),1/2.2)",
                redblind_rgb="rgb(datum.rb_r,datum.rb_g,datum.rb_b)",
            )
            .mark_rect(cornerRadius=cr_s)
            .encode(
                x=alt.X("i:O").axis(None),
                y=alt.Y("red-blindness:N").axis(my_y_axis),
                fill=alt.Fill("redblind_rgb:N").scale(None).legend(None),
                stroke=alt.Stroke("redblind_rgb:N").scale(None).legend(None),             
            )
        )  
        return red_blindness

    def chart_grayscale(data, h, w, expr_hex, my_y_axis, cr_s):
        grayscale = (
            alt.Chart(data, height=h, width=alt.Step(w))
            .transform_calculate(
                hex=expr_hex,
                rgb="rgb(datum.hex)",
                lumn_rgb="datum.rgb['r']*0.3+datum.rgb['g']*0.59+datum.rgb['b']*0.3",
                grayscale_rgb="rgb(datum.lumn_rgb,datum.lumn_rgb,datum.lumn_rgb)",
            )
            .mark_rect(cornerRadius=cr_s)
            .encode(
                x=alt.X("i:O").axis(None),
                y=alt.Y("grayscale:N").axis(my_y_axis),
                fill=alt.Fill("grayscale_rgb:N").scale(None).legend(None),
                stroke=alt.Stroke("grayscale_rgb:N").scale(None).legend(None),               

            )
        )
        return grayscale

    def plot_scheme(scheme_name, dict_schemes, continuous=False, cvd=False, grayscale=False):
        # determine chart settings
        chart_dict = chart_settings(scheme_name, dict_schemes, continuous)    

        # unpack chart_dict
        custom = chart_dict['custom']
        data = chart_dict['data']
        w = chart_dict['width']
        h_l = 50
        h_s = 20
        cr_l = chart_dict['cornerRadius_large']
        cr_s = chart_dict['cornerRadius_small']
        no = chart_dict['no_colors']

        # define color scale
        color_scale = chart_color_scale(scheme_name, dict_schemes, continuous, custom, no)

        # define how hex-codes can be derived, from datasource or using color scale
        expr_hex = "datum.hex" if custom and not continuous else "scale('color', datum.i)"

        # define styling for y-axis
        my_y_axis = alt.Axis(
            grid=False,
            ticks=False,
            labels=False,
            domain=False,
            titleAngle=0,
            titleAlign="right",
            titleBaseline="middle",
        )    

        # determine color pallettes for different color deficiencies
        normal_vision = chart_normal_vision(data, h_l, w, expr_hex, my_y_axis, cr_l)
        green_blindness = chart_green_blindness(data, h_s, w, expr_hex, my_y_axis, cr_s)
        red_blindness = chart_red_blindness(data, h_s, w, expr_hex, my_y_axis, cr_s)
        monochrome = chart_grayscale(data, h_s, w, expr_hex, my_y_axis, cr_s)

        # determine which color pallettes to return
        if cvd and grayscale:
            chart_concat = (normal_vision & green_blindness & red_blindness & monochrome & color_scale)
        elif cvd and not grayscale:
            chart_concat = (normal_vision & green_blindness & red_blindness & color_scale)
        else:
            chart_concat = (normal_vision & color_scale)

        # set configuration on concatenated chart object
        chart_comb = chart_concat.configure_concat(spacing=1).configure_view(stroke=None)    
        return chart_comb


The Basics of Color Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Color selection is an essential aspect of creating clear and informative
visualizations of scientific data. To make the most effective choices,
it's important to understand the basics of color perception and theory.

Color Perception and Theory
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The importance of perceptually uniform color scales
---------------------------------------------------

Using colors that are perceptually uniform can help ensure that viewers
can accurately perceive the relative differences between data points. By
maintaining consistent differences in color perception across a scale, you
can create visualizations that are not only informative but also easy to
understand.

.. altair-plot::
    :hide-code:    
    :output: none

    percep_schemes = {
        "uniform": ["#542788", "#1f7abd", "#4dbd33", "#fdae61", "#d7191c"],
        "non-uniform": ["#FF0000", "#FF6600", "#FFFF00", "#00FF00", "#0000FF"]
    }    

.. list-table::
   :widths: 100
   :header-rows: 1

   * - Example
   * - Uniform color scheme

       .. altair-plot::
         :remove-code:

         plot_scheme("uniform", percep_schemes, cvd=True, continuous=True)

   * - **Non-uniform** color scheme

       .. altair-plot::
         :remove-code:

         plot_scheme("non-uniform", percep_schemes, cvd=True, continuous=True)

Different types of color spaces
-------------------------------

Different color spaces, such as RGB or HSL, offer different advantages and
can affect the perceived brightness and contrast of colors. By 
understanding the nuances of color spaces, you can create visualizations
that are not only informative but also visually appealing.

Accessibility and Aesthetics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Considerations for color-blind viewers
--------------------------------------
   
Around 8% of men and 0.5% of women have some form of color vision deficiency.
To make sure your visualizations are accessible to all viewers, it's
important to choose colors that are distinguishable even for those with 
color vision deficiencies. By using colors that have a high degree of
contrast, you can create visualizations that are not only informative but
also inclusive.

.. altair-plot::
    :hide-code:    
    :output: none

    color_vision_deficiency = {
        'tol_sunset_friendly': ['#364B9A', '#4A7BB7', '#6EA6CD', '#98CAE1', '#C2E4EF', '#EAECCC', '#FEDA8B', '#FDB366', '#F67E4B', '#DD3D2D', '#A50026'],
        'unfriendly' : ['#006400', '#228B22', '#00FF00', '#7FFF00', '#FFFF00', '#FFA500', '#FF0000']        
    }

.. list-table::
   :widths: 100
   :header-rows: 1

   * - Example
   * - Friendly diverging color scheme (`sunset` by Paul Ton, see section xx for more)

       .. altair-plot::
         :remove-code:

         plot_scheme("tol_sunset_friendly", color_vision_deficiency, cvd=True, continuous=True)

   * - **Unfriendly** diverging color scale

       .. altair-plot::
         :remove-code:

         plot_scheme("unfriendly", color_vision_deficiency, cvd=True, continuous=True)

Guidelines for creating visually appealing presentations
--------------------------------------------------------

While accuracy is the primary goal of visualizations, aesthetics also play
an important role in engaging viewers and making data more memorable.
By using a limited color palette, choosing harmonious colors, and balancing
colors to create a sense of visual hierarchy, you can create visualizations
that are not only informative but also visually stunning.

.. code-block:: none
    
    A visualization that uses color to create a sense of visual hierarchy,
    such as a heatmap or a scatterplot.


Types of Color Scales
~~~~~~~~~~~~~~~~~~~~~

This sections presents the three primary color scales used in data
visualization: sequential, diverging, and categorical. The section
includes examples of data that can be visualized using each scale and
popular color schemes used in practice.

Sequential Scales
^^^^^^^^^^^^^^^^^

Sequential scales are best suited for data that has an inherent ordering,
such as data that varies from low to high, or over time. Examples of
sequential data include temperature or population density, where the
range of values is continuous and unbroken.

.. altair-plot::
    :hide-code:    
    :output: none

    seqs_schemes = {
        "blues": 9,
        "tealblues": 9,
        "teals": 9,
        "greens": 9,
        "browns": 9,
        "greys": 9,
        "purples": 9,
        "warmgreys": 9,
        "reds": 9,
        "oranges": 9,
    }

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Scheme
     - Example
   * - .. code-block:: none
    
         blues

     - .. altair-plot::
         :remove-code:

         plot_scheme("blues", seqs_schemes, cvd=True, continuous=True)

   * - 
     - .. altair-plot::
         :remove-code:

         plot_scheme("blues", seqs_schemes, cvd=False, continuous=False)

   * - .. code-block:: none
    
         tealblues

     - .. altair-plot::
         :remove-code:

         plot_scheme("tealblues", seqs_schemes, cvd=True, continuous=True)

   * - 
     - .. altair-plot::
         :remove-code:

         plot_scheme("tealblues", seqs_schemes, cvd=False, continuous=False)

   * - .. code-block:: none
    
         teals

     - .. altair-plot::
         :remove-code:

         plot_scheme("teals", seqs_schemes, cvd=True, continuous=True)

   * - 
     - .. altair-plot::
         :remove-code:

         plot_scheme("teals", seqs_schemes, cvd=False, continuous=False)

   * - .. code-block:: none
    
         greens

     - .. altair-plot::
         :remove-code:

         plot_scheme("greens", seqs_schemes, cvd=True, continuous=True)

   * - 
     - .. altair-plot::
         :remove-code:

         plot_scheme("greens", seqs_schemes, cvd=False, continuous=False)

   * - .. code-block:: none
    
         browns

     - .. altair-plot::
         :remove-code:

         plot_scheme("browns", seqs_schemes, cvd=True, continuous=True)

   * - 
     - .. altair-plot::
         :remove-code:

         plot_scheme("browns", seqs_schemes, cvd=False, continuous=False)

   * - .. code-block:: none
    
         greys

     - .. altair-plot::
         :remove-code:

         plot_scheme("greys", seqs_schemes, cvd=True, continuous=True)

   * - 
     - .. altair-plot::
         :remove-code:

         plot_scheme("greys", seqs_schemes, cvd=False, continuous=False)

   * - .. code-block:: none
    
         purples

     - .. altair-plot::
         :remove-code:

         plot_scheme("purples", seqs_schemes, cvd=True, continuous=True)

   * - 
     - .. altair-plot::
         :remove-code:

         plot_scheme("purples", seqs_schemes, cvd=False, continuous=False)

   * - .. code-block:: none
    
         warmgreys

     - .. altair-plot::
         :remove-code:

         plot_scheme("warmgreys", seqs_schemes, cvd=True, continuous=True)

   * - 
     - .. altair-plot::
         :remove-code:

         plot_scheme("warmgreys", seqs_schemes, cvd=False, continuous=False)

   * - .. code-block:: none
    
         reds

     - .. altair-plot::
         :remove-code:

         plot_scheme("reds", seqs_schemes, cvd=True, continuous=True)

   * - 
     - .. altair-plot::
         :remove-code:

         plot_scheme("reds", seqs_schemes, cvd=False, continuous=False) 

   * - .. code-block:: none
    
         oranges

     - .. altair-plot::
         :remove-code:

         plot_scheme("oranges", seqs_schemes, cvd=True, continuous=True)

   * - 
     - .. altair-plot::
         :remove-code:

         plot_scheme("oranges", seqs_schemes, cvd=False, continuous=False)

Diverging Scales
^^^^^^^^^^^^^^^^

Examples of diverging data
--------------------------

Diverging scales are best suited for data that varies above and below a
center point, such as positive and negative deviations from a mean.
Examples of diverging data include measures of deviation, such as
temperature anomalies or changes in sea level.

.. altair-plot::
    :hide-code:    
    :output: none

    divg_schemes = {
        "blueorange": 9,
        "brownbluegreen": 9,
        "purplegreen": 9,
        "pinkyellowgreen": 9,
        "purpleorange": 9,
        "redblue": 9,
        "redgrey": 9,
        "redyellowblue": 9,
        "redyellowgreen": 9,
        "spectral": 9,
    }

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Scheme
     - Example
   * - .. code-block:: none
    
         blueorange

     - .. altair-plot::
         :remove-code:

         plot_scheme("blueorange", divg_schemes, cvd=True, continuous=True)

   * - 
     - .. altair-plot::
         :remove-code:

         plot_scheme("blueorange", divg_schemes, cvd=False, continuous=False)

   * - .. code-block:: none
    
         brownbluegreen

     - .. altair-plot::
         :remove-code:

         plot_scheme("brownbluegreen", divg_schemes, cvd=True, continuous=True)

   * - 
     - .. altair-plot::
         :remove-code:

         plot_scheme("brownbluegreen", divg_schemes, cvd=False, continuous=False)

   * - .. code-block:: none
    
         purplegreen

     - .. altair-plot::
         :remove-code:

         plot_scheme("purplegreen", divg_schemes, cvd=True, continuous=True)

   * - 
     - .. altair-plot::
         :remove-code:

         plot_scheme("purplegreen", divg_schemes, cvd=False, continuous=False)

   * - .. code-block:: none
    
         pinkyellowgreen

     - .. altair-plot::
         :remove-code:

         plot_scheme("pinkyellowgreen", divg_schemes, cvd=True, continuous=True)

   * - 
     - .. altair-plot::
         :remove-code:

         plot_scheme("pinkyellowgreen", divg_schemes, cvd=False, continuous=False)

   * - .. code-block:: none
    
         purpleorange

     - .. altair-plot::
         :remove-code:

         plot_scheme("purpleorange", divg_schemes, cvd=True, continuous=True)

   * - 
     - .. altair-plot::
         :remove-code:

         plot_scheme("purpleorange", divg_schemes, cvd=False, continuous=False)

   * - .. code-block:: none
    
         redblue

     - .. altair-plot::
         :remove-code:

         plot_scheme("redblue", divg_schemes, cvd=True, continuous=True)

   * - 
     - .. altair-plot::
         :remove-code:

         plot_scheme("redblue", divg_schemes, cvd=False, continuous=False)

   * - .. code-block:: none
    
         redgrey

     - .. altair-plot::
         :remove-code:

         plot_scheme("redgrey", divg_schemes, cvd=True, continuous=True)

   * - 
     - .. altair-plot::
         :remove-code:

         plot_scheme("redgrey", divg_schemes, cvd=False, continuous=False)

   * - .. code-block:: none
    
         redyellowblue

     - .. altair-plot::
         :remove-code:

         plot_scheme("redyellowblue", divg_schemes, cvd=True, continuous=True)

   * - 
     - .. altair-plot::
         :remove-code:

         plot_scheme("redyellowblue", divg_schemes, cvd=False, continuous=False)

   * - .. code-block:: none
    
         redyellowgreen

     - .. altair-plot::
         :remove-code:

         plot_scheme("redyellowgreen", divg_schemes, cvd=True, continuous=True)

   * - 
     - .. altair-plot::
         :remove-code:

         plot_scheme("redyellowgreen", divg_schemes, cvd=False, continuous=False) 

   * - .. code-block:: none
    
         spectral

     - .. altair-plot::
         :remove-code:

         plot_scheme("spectral", divg_schemes, cvd=True, continuous=True)

   * - 
     - .. altair-plot::
         :remove-code:

         plot_scheme("spectral", divg_schemes, cvd=False, continuous=False)

Categorical Scales
^^^^^^^^^^^^^^^^^^

Examples of categorical data
----------------------------

Categorical scales are best suited for data that is unordered, such as
different species or categories. Examples of categorical data include
the types of flowers in a garden, or different political affiliations.


.. altair-plot::
    :hide-code:    
    :output: none

    catg_schemes = {
        "accent": 8,
        "category10": 10,
        "category20": 20,
        "category20b": 20,
        "category20c": 20,
        "dark2": 8,
        "paired": 12,
        "pastel1": 9,
        "pastel2": 8,
        "set1": 9,
        "set2": 8,
        "set3": 12,
        "tableau10": 10,
        "tableau20": 20,
    }

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Scheme
     - Example
   * - .. code-block:: none
    
         accent

     - .. altair-plot::
         :remove-code:

         plot_scheme("accent", catg_schemes, cvd=True, continuous=False)

   * - .. code-block:: none
    
         category10

     - .. altair-plot::
         :remove-code:

         plot_scheme("category10", catg_schemes, cvd=True, continuous=False)

   * - .. code-block:: none
    
         category20

     - .. altair-plot::
         :remove-code:

         plot_scheme("category20", catg_schemes, cvd=True, continuous=False)

   * - .. code-block:: none
    
         category20b

     - .. altair-plot::
         :remove-code:

         plot_scheme("category20b", catg_schemes, cvd=True, continuous=False)

   * - .. code-block:: none
    
         category20c

     - .. altair-plot::
         :remove-code:

         plot_scheme("category20c", catg_schemes, cvd=True, continuous=False)

   * - .. code-block:: none
    
         dark2

     - .. altair-plot::
         :remove-code:

         plot_scheme("dark2", catg_schemes, cvd=True, continuous=False)

   * - .. code-block:: none
    
         paired

     - .. altair-plot::
         :remove-code:

         plot_scheme("paired", catg_schemes, cvd=True, continuous=False)

   * - .. code-block:: none
    
         pastel1

     - .. altair-plot::
         :remove-code:

         plot_scheme("pastel1", catg_schemes, cvd=True, continuous=False)

   * - .. code-block:: none
    
         pastel2

     - .. altair-plot::
         :remove-code:

         plot_scheme("pastel2", catg_schemes, cvd=True, continuous=False)

   * - .. code-block:: none
    
         set1

     - .. altair-plot::
         :remove-code:

         plot_scheme("set1", catg_schemes, cvd=True, continuous=False)

   * - .. code-block:: none
    
         set2

     - .. altair-plot::
         :remove-code:

         plot_scheme("set2", catg_schemes, cvd=True, continuous=False)

   * - .. code-block:: none
    
         set3

     - .. altair-plot::
         :remove-code:

         plot_scheme("set3", catg_schemes, cvd=True, continuous=False)

   * - .. code-block:: none
    
         tableau10

     - .. altair-plot::
         :remove-code:

         plot_scheme("tableau10", catg_schemes, cvd=True, continuous=False)

   * - .. code-block:: none
    
         tableau20

     - .. altair-plot::
         :remove-code:

         plot_scheme("tableau20", catg_schemes, cvd=True, continuous=False)

Using Tools for Color Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pre-Designed Color Palettes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example color palettes from the other packages
----------------------------------------------

This subsection focuses on pre-designed color palettes that can be
used in data visualization from other sources.

Modifying Color Scales
^^^^^^^^^^^^^^^^^^^^^^

Tools for adjusting brightness, saturation, and hue
---------------------------------------------------

This subsection provides an overview of the different ways in which
brightness, saturation, and hue can be modified to create custom color
scales. It explains how changing these attributes can help to emphasize
or de-emphasize certain aspects of the data being visualized.

Customizing color scales to match specific data requirements
------------------------------------------------------------

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