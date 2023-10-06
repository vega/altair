.. currentmodule:: altair

.. _user-guide-image-marks:

Image
~~~~~~

Image marks allow external images, such as icons or photographs, to be included in Altair visualizations. Image files such as PNG or JPG images are loaded from provided URLs.

Image Mark Properties
^^^^^^^^^^^^^^^^^^^^^
An ``image`` mark can contain any :ref:`standard mark properties <mark-properties>`
and the following special properties:

.. altair-object-table:: altair.MarkDef
   :properties: url aspect align baseline

Scatter Plot with Image Marks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. altair-plot::
    import altair as alt
    import pandas as pd

    source = pd.DataFrame.from_records(
        [
            {
                "x": 0.5,
                "y": 0.5,
                "img": "https://vega.github.io/vega-datasets/data/ffox.png",
            },
            {
                "x": 1.5,
                "y": 1.5,
                "img": "https://vega.github.io/vega-datasets/data/gimp.png",
            },
            {
                "x": 2.5,
                "y": 2.5,
                "img": "https://vega.github.io/vega-datasets/data/7zip.png",
            },
        ]
    )

    alt.Chart(source).mark_image(width=50, height=50).encode(x="x", y="y", url="img")

Show Image Marks With Selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This example demonstrates how to display image marks with drag selection. We create two charts:
one with point marks and the other with image marks, applying the selection filter only to the latter.
By combining these two charts, we can achieve the desired result.

.. altair-plot::
    :hide-code:
    :div_class: properties-example

    import altair as alt
    import pandas as pd

    source = pd.DataFrame.from_records(
        [{'a': 1, 'b': 1, 'image': 'https://altair-viz.github.io/_static/altair-logo-light.png'},
        {'a': 2, 'b': 2, 'image': 'https://avatars.githubusercontent.com/u/11796929?s=200&v=4'},
        {'a': 3, 'b': 3, 'image': ''}]
    )

    brush = alt.selection_interval()
    point = alt.Chart(source, width=200, height=200).mark_circle(size=100).encode(
        x='a',
        y='b',
    ).add_params(
        brush
    )

    img = alt.Chart(source).mark_image(width=50, height=75).encode(
        x='a',
        y='b',
        url='image'
    ).transform_filter(
        brush
    )

    img_faceted = alt.Chart(source, width=50, height=75).mark_image().encode(
        url='image'
    ).facet(
        alt.Facet('image', title='', header=alt.Header(labelFontSize=0))
    ).transform_filter(
        brush
    )


    two_layered_chart = point + img
    faceted_chart = point | img_faceted

    alt.hconcat(
        two_layered_chart.properties(title="Two Layered Chart"),
        faceted_chart.properties(title="Faceted Chart"),
    ).configure_title(
        fontSize=10,
        anchor='start'
    )

In the layered chart, images may overlap one other, using the faceted chart instead can
avoid this issue.

If you are searching for image tooltip that can show image while hovering on a point, 
please see :ref:`Image Tooltip <gallery_image_tooltip>`.

Use Local Images As Image Marks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We could also show local images using Base64 encoding, replace the image path below
and create your own plot.

.. code-block::

    import altair as alt
    import pandas as pd
    from IPython.display import Image
    import base64, io, IPython
    from PIL import Image as PILImage

    # replace your image path here
    # recommend use raw string for absolute path; i.e. r'C:\Users\...\img00.jpg'
    images = ["./img00.jpg", "./img01.jpg", "./img02.jpg"]
    imgCode = []


    for imgPath in images:
        image = PILImage.open(imgPath)
        output = io.BytesIO()   
        # choose the right format
        image.save(output, format='JPEG')
        encoded_string = "data:image/jpeg;base64,"+base64.b64encode(output.getvalue()).decode()
        imgCode.append(encoded_string)

    x = [0.5, 1.5, 2.5]
    y = [0.5, 1.5, 2.5]
    source = pd.DataFrame({"x": x, "y": y, "img": imgCode})
    alt.Chart(source).mark_image(
        width=50,
        height=50
    ).encode(
        x='x',
        y='y',
        url='img'
    )